import argparse
import hashlib
import json
import re
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urldefrag, urlparse

import requests
from bs4 import BeautifulSoup, Tag
from markdownify import markdownify as md


@dataclass
class NavNode:
    title: str
    url: Optional[str] = None
    children: list["NavNode"] = field(default_factory=list)


INVALID_FILENAME_CHARS = r'<>:"/\\|?*'
VIDEO_EXTS = (".mp4", ".mov", ".webm", ".gif")


def normalize_text(text: str) -> str:
    text = text.replace("¶", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def safe_name(name: str, max_len: int = 80) -> str:
    name = normalize_text(name)
    for ch in INVALID_FILENAME_CHARS:
        name = name.replace(ch, "_")
    name = name.replace("\n", " ").strip(" ._")
    name = re.sub(r"_+", "_", name)

    if not name:
        name = "untitled"

    if len(name) > max_len:
        digest = hashlib.md5(name.encode("utf-8")).hexdigest()[:8]
        name = name[: max_len - 9].rstrip(" ._") + "_" + digest

    return name


def normalize_url(url: str, base_url: str) -> str:
    abs_url = urljoin(base_url, url)
    abs_url, _frag = urldefrag(abs_url)
    return abs_url


def is_same_site_doc(url: str, start_url: str) -> bool:
    u = urlparse(url)
    s = urlparse(start_url)
    return u.scheme in {"http", "https"} and u.netloc == s.netloc


def normalize_code_for_dedupe(code: str) -> str:
    """
    Manim/Sphinx 示例里经常有：
    1. from manim import * + class XxxScene
    2. class XxxScene
    这两个其实是同一个示例。去重时忽略开头的 from manim import *。
    """
    lines = [line.rstrip() for line in code.splitlines()]
    lines = [line for line in lines if line.strip()]

    while lines and lines[0].strip() == "from manim import *":
        lines.pop(0)

    text = "\n".join(lines).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def remove_empty_video_links(article: Tag) -> None:
    """
    删除空视频链接，例如 markdownify 后会变成：[](./DefaultAddScene-1.mp4)
    """
    for a in list(article.find_all("a", href=True)):
        href = a.get("href", "")
        text = normalize_text(a.get_text(" ", strip=True))

        if text:
            continue

        clean_href = href.lower().split("?")[0].split("#")[0]
        if not clean_href.endswith(VIDEO_EXTS):
            continue

        parent = a.parent
        if parent and isinstance(parent, Tag):
            parent_text = normalize_text(parent.get_text(" ", strip=True))
            # 父节点只有空视频链接时，删父节点，避免残留空段落
            if not parent_text:
                parent.decompose()
                continue

        a.decompose()


def dedupe_code_blocks(article: Tag) -> None:
    """
    删除重复代码块，主要处理 Manim API 页面中同一 Example 出现两份代码的问题。
    """
    seen: set[str] = set()

    # Sphinx/Pygments 常见代码块。用 list 固定快照，避免边遍历边删的问题。
    blocks = list(article.select("div.highlight, div[class*='highlight-']"))

    for block in blocks:
        pre = block.find("pre")
        if not pre:
            continue

        code_text = pre.get_text("\n", strip=False)
        key = normalize_code_for_dedupe(code_text)

        # 太短的代码不去重，避免误删签名/小片段
        if len(key) < 80:
            continue

        if key in seen:
            block.decompose()
        else:
            seen.add(key)


def clean_markdown_text(markdown: str) -> str:
    markdown = markdown.replace("¶", "")

    # 删除空视频链接残留
    markdown = re.sub(
        r"\n*\[\]\([^)]+\.(?:mp4|mov|webm|gif)\)\n*",
        "\n\n",
        markdown,
        flags=re.IGNORECASE,
    )

    # 常见页面噪声
    noise_patterns = [
        r"View this page\s*",
        r"Edit this page\s*",
        r"Back to top\s*",
        r"Skip to content\s*",
    ]
    for p in noise_patterns:
        markdown = re.sub(p, "", markdown, flags=re.IGNORECASE)

    # Sphinx Methods/Attributes 表格常出现空表头，改成可读一点
    markdown = markdown.replace(
        "|  |  |\n| --- | --- |",
        "| Name | Description |\n| --- | --- |",
    )

    # 去掉连续太多空行、行尾空格
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)

    return markdown.strip() + "\n"


class ManimReferenceCrawler:
    def __init__(
        self,
        start_url: str,
        out_dir: Path,
        delay: float = 0.2,
        timeout: int = 30,
        prefix_index: bool = True,
    ):
        self.start_url = start_url
        self.out_dir = out_dir.resolve()
        self.delay = delay
        self.timeout = timeout
        self.prefix_index = prefix_index

        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 ManimReferenceCrawler/1.1 "
                    "(for local knowledge base building)"
                )
            }
        )

        self.visited: set[str] = set()
        self.manifest: list[dict] = []

    def fetch(self, url: str) -> str:
        for attempt in range(3):
            try:
                resp = self.session.get(url, timeout=self.timeout)
                resp.raise_for_status()
                resp.encoding = resp.apparent_encoding or "utf-8"
                return resp.text
            except Exception:
                if attempt == 2:
                    raise
                time.sleep(1 + attempt)

        raise RuntimeError(f"failed to fetch: {url}")

    def get_sidebar_root(self, soup: BeautifulSoup) -> Tag:
        selectors = [
            "aside.sidebar-drawer",
            "div.sidebar-drawer",
            "nav.sidebar",
            "div.sidebar-tree",
            "div.sidebar-scroll",
            "nav",
            "aside",
        ]

        for selector in selectors:
            node = soup.select_one(selector)
            if node:
                return node

        return soup

    def find_reference_manual_li(self, soup: BeautifulSoup) -> Optional[Tag]:
        sidebar = self.get_sidebar_root(soup)

        for a in sidebar.find_all("a", href=True):
            text = normalize_text(a.get_text(" ", strip=True))
            href = a.get("href", "")

            if text == "Reference Manual":
                li = a.find_parent("li")
                if li:
                    return li

            if "reference.html" in href and "Reference" in text:
                li = a.find_parent("li")
                if li:
                    return li

        return None

    def direct_link_before_nested_ul(self, li: Tag) -> Optional[Tag]:
        for child in li.children:
            if isinstance(child, Tag):
                if child.name == "ul":
                    break
                if child.name == "a" and child.get("href"):
                    return child
                nested = child.find("a", href=True, recursive=False)
                if nested:
                    return nested

        return li.find("a", href=True)

    def parse_li(self, li: Tag, base_url: str) -> Optional[NavNode]:
        a = self.direct_link_before_nested_ul(li)

        if not a:
            return None

        title = normalize_text(a.get_text(" ", strip=True))
        url = normalize_url(a["href"], base_url)

        node = NavNode(title=title, url=url)

        for ul in li.find_all("ul", recursive=False):
            child_lis = ul.find_all("li", recursive=False)
            for child_li in child_lis:
                child_node = self.parse_li(child_li, base_url)
                if child_node:
                    node.children.append(child_node)

        return node

    def parse_reference_tree(self, html: str) -> NavNode:
        soup = BeautifulSoup(html, "html.parser")
        ref_li = self.find_reference_manual_li(soup)

        if ref_li:
            root = self.parse_li(ref_li, self.start_url)
            if root and root.children:
                return root

        # fallback：如果没找到完整左侧树，就按 reference/reference_index URL 做一个扁平树
        print("[WARN] 没找到完整 Reference Manual 左侧树，启用 URL 过滤 fallback。")

        sidebar = self.get_sidebar_root(soup)
        seen: set[str] = set()
        root = NavNode(title="Reference Manual", url=None)

        for a in sidebar.find_all("a", href=True):
            title = normalize_text(a.get_text(" ", strip=True))
            url = normalize_url(a["href"], self.start_url)

            if not title or url in seen:
                continue

            if not is_same_site_doc(url, self.start_url):
                continue

            path = urlparse(url).path
            if "/reference/" in path or "/reference_index/" in path or path.endswith("/reference.html"):
                seen.add(url)
                root.children.append(NavNode(title=title, url=url))

        return root

    def clean_page_to_markdown(self, html: str, url: str, tree_path: list[str]) -> tuple[str, str]:
        soup = BeautifulSoup(html, "html.parser")

        # 更精确地取正文。Manim 使用的是 Sphinx/PyData 文档主题。
        article = (
            soup.select_one("article.bd-article")
            or soup.select_one("article[role='main']")
            or soup.select_one("article")
            or soup.select_one("main")
            or soup.select_one("div.document")
            or soup.body
            or soup
        )

        title_node = article.find("h1") or soup.find("h1")
        title = normalize_text(title_node.get_text(" ", strip=True)) if title_node else tree_path[-1]

        # 只在 article 内部清理，避免影响左侧树解析逻辑；这里已经是单页清洗阶段。
        remove_selectors = [
            "script",
            "style",
            "noscript",
            "button",
            "form",
            "nav",
            "aside",
            ".headerlink",
            ".copybtn",
            ".copy-button",
            ".sd-sphinx-override",
            ".only-light",
            ".only-dark",
            ".toggle-hidden",
            ".sphinx-tabs-tablist",
            ".prev-next-area",
            ".edit-this-page",
            ".view-this-page",
            ".bd-header-article",
            ".bd-footer-article",
        ]

        for selector in remove_selectors:
            for node in list(article.select(selector)):
                node.decompose()

        remove_empty_video_links(article)
        dedupe_code_blocks(article)

        # 绝对化链接，方便后续知识库回溯；同时删掉 title，避免 markdown 过长。
        for a in article.find_all("a", href=True):
            href = a["href"]
            if not href.startswith("#"):
                a["href"] = normalize_url(href, url)
            if a.has_attr("title"):
                del a["title"]

        for img in article.find_all("img", src=True):
            img["src"] = normalize_url(img["src"], url)

        markdown = md(
            str(article),
            heading_style="ATX",
            bullets="-",
            strip=["span"],
        )

        markdown = clean_markdown_text(markdown)

        front_matter = {
            "title": title,
            "source_url": url,
            "tree_path": tree_path,
            "scraped_at": datetime.now().isoformat(timespec="seconds"),
        }

        fm = "---\n" + json.dumps(front_matter, ensure_ascii=False, indent=2) + "\n---\n\n"

        return title, fm + markdown

    def output_path_for_node(
        self,
        parent_dir: Path,
        node: NavNode,
        index: int,
        has_children: bool,
    ) -> tuple[Path, Path]:
        name = safe_name(node.title)

        if self.prefix_index:
            name = f"{index:03d}_{name}"

        if has_children:
            node_dir = parent_dir / name
            md_path = node_dir / "_index.md"
            return node_dir, md_path

        md_path = parent_dir / f"{name}.md"
        return parent_dir, md_path

    def save_node(
        self,
        node: NavNode,
        parent_dir: Path,
        tree_path: list[str],
        index: int = 1,
    ):
        has_children = bool(node.children)
        node_dir, md_path = self.output_path_for_node(parent_dir, node, index, has_children)

        current_tree_path = tree_path + [node.title]

        if node.url:
            if node.url in self.visited:
                pass
            else:
                self.visited.add(node.url)

                print(f"[FETCH] {' > '.join(current_tree_path)}")
                print(f"        {node.url}")

                html = self.fetch(node.url)
                title, markdown = self.clean_page_to_markdown(
                    html=html,
                    url=node.url,
                    tree_path=current_tree_path,
                )

                node_dir.mkdir(parents=True, exist_ok=True)
                md_path.write_text(markdown, encoding="utf-8")

                self.manifest.append(
                    {
                        "title": title,
                        "nav_title": node.title,
                        "source_url": node.url,
                        "tree_path": current_tree_path,
                        "file_path": str(md_path),
                    }
                )

                time.sleep(self.delay)

        if has_children:
            node_dir.mkdir(parents=True, exist_ok=True)
            for i, child in enumerate(node.children, start=1):
                self.save_node(child, node_dir, current_tree_path, i)

    def run(self):
        self.out_dir.mkdir(parents=True, exist_ok=True)

        html = self.fetch(self.start_url)
        root = self.parse_reference_tree(html)

        # root 是 Reference Manual
        root_dir = self.out_dir
        self.save_node(root, root_dir, [], 1)

        manifest_path = self.out_dir / "manifest.jsonl"
        with manifest_path.open("w", encoding="utf-8") as f:
            for item in self.manifest:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")

        print("\n[DONE]")
        print(f"saved pages: {len(self.manifest)}")
        print(f"output dir : {self.out_dir}")
        print(f"manifest   : {manifest_path}")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--start-url",
        default="https://docs.manim.community/en/stable/reference_index/animations.html",
        help="任意一个 Manim docs 页面，脚本会从左侧树中找到 Reference Manual。",
    )

    parser.add_argument(
        "--out-dir",
        default="../docs",
        help="输出目录。",
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=0.2,
        help="每个页面请求之间的间隔秒数。",
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="单个请求超时时间。",
    )

    parser.add_argument(
        "--no-prefix-index",
        action="store_true",
        help="不在目录/文件名前加 001_ 这种顺序前缀。",
    )

    args = parser.parse_args()

    crawler = ManimReferenceCrawler(
        start_url=args.start_url,
        out_dir=Path(args.out_dir),
        delay=args.delay,
        timeout=args.timeout,
        prefix_index=not args.no_prefix_index,
    )

    crawler.run()


if __name__ == "__main__":
    # Manim docs version: v0.20.1
    main()