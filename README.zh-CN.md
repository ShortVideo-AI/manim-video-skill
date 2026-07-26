# Manim Video Skill

[English](README.md)

用于生成并渲染 Manim 数学、科普、解释类动画视频的 skill。

## 功能

- 引导模型编写 Manim Community Edition 场景代码。
- 内置 Manim 参考文档，方便离线查 API。
- 通过 `scripts/run_manim_script.py` 渲染，避免直接调用 Manim 时把大量临时文件写到项目根目录。
- 输出结构化 JSON，包含渲染状态、日志路径和最终视频路径。

## 安装

把这个仓库克隆或复制到兼容的 skills 目录，然后用 `$manim-video` 调用。

如果是 Codex，通常可以放到：

```powershell
git clone https://github.com/ShortVideo-AI/manim-video-skill.git ~/.codex/skills/manim-video-skill
```

如果是 opencode、OpenClaw 或其他兼容的 agent 运行时，把这个目录放到对应运行时的 skills 目录即可。

## 环境要求

- Python
- Manim Community Edition

默认情况下，渲染脚本会调用：

```powershell
python -m manim
```

如果默认 `python` 环境里没有安装 Manim，可以用 `--manim-command` 指定 Manim 可执行文件路径。

## 示例

示例视频：

https://github.com/ShortVideo-AI/manim-video-skill/blob/main/examples/smoke-test/GeneratedScene.mp4

见 `examples/smoke-test/`：

- `input_scene.py`：最小 Manim 场景
- `GeneratedScene.mp4`：示例渲染结果
- `README.md`：英文复现命令和预期输出
- `README.zh-CN.md`：中文复现命令和预期输出

## 第三方内容

本仓库在 `docs/` 下打包了一份由 Manim Community 参考文档生成的 markdown 副本，用于本地 API 查询。来源和许可归属见 `NOTICE`。
