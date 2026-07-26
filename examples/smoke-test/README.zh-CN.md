# Smoke Test 示例

[English](README.md)

这个示例用于验证渲染脚本是否能正常完成完整流程：

1. 读取 Manim 场景代码。
2. 复制到指定 job 目录。
3. 调用 Manim 渲染。
4. 返回包含 `video_path` 的结构化 JSON。

## 运行

在仓库根目录执行：

```powershell
python scripts/run_manim_script.py `
  --job-dir sessions/smoke-test/jobs/basic/segments/001 `
  --code-file examples/smoke-test/input_scene.py `
  --quality ql `
  --timeout 180
```

如果默认 `python` 环境里没有安装 Manim，可以显式指定 Manim 可执行文件：

```powershell
python scripts/run_manim_script.py `
  --job-dir sessions/smoke-test/jobs/basic/segments/001 `
  --code-file examples/smoke-test/input_scene.py `
  --quality ql `
  --timeout 180 `
  --manim-command "C:\Path\To\manim.exe"
```

渲染脚本会把生成源码、日志、元数据和视频输出写到 `--job-dir` 下面。仓库根目录的 `sessions/` 已经被 `.gitignore` 忽略，不会误提交。

## 预期结果

成功时会返回类似 JSON：

```json
{
  "success": true,
  "scene_name": "GeneratedScene",
  "video_path": ".../output/video/GeneratedScene.mp4"
}
```

本目录中的 `GeneratedScene.mp4` 是由 `input_scene.py` 渲染出的一个小体积示例视频。
