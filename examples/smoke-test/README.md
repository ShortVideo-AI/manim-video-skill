# Smoke Test Example

[中文](README.zh-CN.md)

This example verifies that the render helper can complete the full render flow:

1. Read the Manim scene code.
2. Copy it into the specified job directory.
3. Invoke Manim.
4. Return structured JSON with `video_path`.

## Run

From the repository root:

```powershell
python scripts/run_manim_script.py `
  --job-dir sessions/smoke-test/jobs/basic/segments/001 `
  --code-file examples/smoke-test/input_scene.py `
  --quality ql `
  --timeout 180
```

If your default `python` environment does not have Manim installed, pass the Manim executable explicitly:

```powershell
python scripts/run_manim_script.py `
  --job-dir sessions/smoke-test/jobs/basic/segments/001 `
  --code-file examples/smoke-test/input_scene.py `
  --quality ql `
  --timeout 180 `
  --manim-command "C:\Path\To\manim.exe"
```

The helper writes generated source, logs, metadata, and video output under the supplied `--job-dir`. The root `sessions/` directory is ignored by git.

## Expected Result

A successful run returns JSON similar to:

```json
{
  "success": true,
  "scene_name": "GeneratedScene",
  "video_path": ".../output/video/GeneratedScene.mp4"
}
```

The checked-in `GeneratedScene.mp4` is a small sample output rendered from `input_scene.py`.

https://github.com/ShortVideo-AI/manim-video-skill/blob/main/examples/smoke-test/GeneratedScene.mp4
