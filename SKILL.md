---
name: manim-video
description: Generate Manim Community Edition Python scenes, look up bundled Manim reference docs when needed, and render the generated code into video files with the provided script.
---

# Manim Video

Use this skill when the user asks for a mathematical, educational, diagrammatic, data, geometry, animation, or explainer video that can be authored with Manim Community Edition.

## What This Skill Provides

- Local Manim reference docs under `docs/`.
- A render helper at `scripts/run_manim_script.py`.
- A repeatable workflow for generating Manim code, rendering it, reading the structured result, and fixing render errors.

## Directory Map

- `SKILL.md`: this operating guide.
- `docs/001_Reference Manual/_index.md`: top-level Manim reference index.
- `docs/001_Reference Manual/001_Animations/`: animation classes such as `Create`, `FadeIn`, `Transform`, `AnimationGroup`, and updaters.
- `docs/001_Reference Manual/004_Mobjects/`: visible objects such as shapes, text, axes, graphs, tables, SVGs, images, and 3D objects.
- `docs/001_Reference Manual/005_Scenes/`: `Scene`, `MovingCameraScene`, `ThreeDScene`, `ZoomedScene`, and scene file writer APIs.
- `docs/001_Reference Manual/003_Configuration/`: configuration options.
- `docs/001_Reference Manual/006_Utilities and other modules/`: colors, rate functions, paths, space operations, images, sound helpers, and other utilities.
- `scripts/run_manim_script.py`: writes generated code into a job directory, invokes `python -m manim`, and returns JSON with paths, logs, and success state. Manim's high-churn temporary media is rendered outside the workspace, then the final video is copied back into the job directory.

## Output Isolation Rules

- Treat this skill directory as read-only during normal use.
- Never write generated scenes, job folders, render logs, media, or videos under the installed skill directory.
- If the runtime prompt provides `workspace_relative_job_dir`, use that path as the job root for the current task.
- The preferred job layout is `sessions/<session_id>/jobs/<job_slug>/`.
- Put every render task under the current job root or one of its segment subdirectories:

```text
<job_dir>/segments/<segment-id>/
```

- If no runtime job directory is provided, create a unique directory under `sessions/<unknown-session>/jobs/<job_slug>/`.
- Use only that job directory for generated source, logs, result metadata, and final videos. The helper may use a temporary directory outside the workspace for Manim partial media during rendering.
- Never create render outputs directly under the workspace root. Do not use root-level `segments/`, `source/`, `output/`, `media/`, or `jobs/` as deliverable locations.

## Required Workflow

1. Understand the video request: topic, audience, duration, aspect ratio if stated, visual style, and whether transparent background is explicitly requested.
2. Search local docs before guessing unfamiliar APIs:
   - Use `rg "ClassOrFunctionName" <skill_dir>/docs`.
   - Start at `docs/001_Reference Manual/_index.md` when you need to discover the right module.
   - Prefer the bundled docs over memory when API details matter.
3. Write a single Python file containing one primary Manim scene class.
4. Save the draft source under the current job directory, such as `<job_dir>/segments/001/input_scene.py`.
5. Render through the helper script, not by calling `manim` directly, so the agent receives structured JSON and a stable output layout.
6. Pass `--job-dir <job_dir>/segments/<segment-id>` or another subdirectory of the current job; never pass a path under the installed skill directory.
7. If rendering fails, inspect `render_log_tail` and `output/render.log`, update the code, and rerender.
8. Return the final `video_path`, plus any important notes about quality, background transparency, or unresolved render limitations.

## Command Safety Rules

- Do not run `manim`, `python -m manim`, or any direct Manim CLI command.
- Always use `<skill_dir>/scripts/run_manim_script.py` for rendering.
- Direct Manim commands write high-churn `media/`, `partial_movie_files/`, `texts/`, and cache files under the workspace by default. That can overwhelm the host file watcher and can crash long-running sessions.
- If you need a different Manim option, add or use an option on the helper script instead of bypassing it.
- If a direct Manim command has already created `media/` under the workspace, treat it as disposable cache. Do not use it as the canonical output path.

## Duration Contract

- When the user or a higher-level workflow provides a target duration, make the Manim code's total `run_time` plus `wait` time match that target within +/- 2 seconds.
- Use explicit timing for every animation: `self.play(..., run_time=<seconds>)`.
- Use explicit waits: `self.wait(<seconds>)`.
- Do not claim a duration from the storyboard. Report the actual rendered duration from the render result or a media probe.
- For finished video production, prefer letting `video-production-skill` own voiceover, subtitles, final muxing, and final duration QA.
- For voiceover segments, target duration means the probed narration duration. The Manim clip itself must fill that duration; do not create an 8-second visual for an 18-second voiceover and expect the composer to fix it.
- Keep a meaningful final visual state on screen until the voiceover is almost finished. Do not use `FadeOut(*self.mobjects)`, `self.clear()`, or equivalent full-scene removal before `target_duration - 0.5`.
- If a full fade-out is appropriate, schedule it only in the last 0.3 to 0.5 seconds. Otherwise end with the key diagram/title still visible and use `self.wait(remaining_seconds)` to hold it.
- Before rendering, sum the planned `run_time` and `wait` values. The sum should be within 0.15 seconds of the segment target when the clip will be composed with voiceover.
- Divide voiceover segments into 2 to 4 visual states. Each state should have its own duration budget and one self-contained layout.
- Transition between states with `ReplacementTransform`, `FadeOut(old_group) + FadeIn(new_group)`, or a deliberate camera/position change. Do not keep adding new state content to old state content.
- Distribute the target duration across states before writing animations. Do not reveal all states quickly and put all remaining time into the final state.
- For 3 states, default to roughly `target_duration / 3` per state. For 4 states, default to roughly `target_duration / 4` per state.
- A single state should not consume more than 45% of the segment duration unless the narration explicitly needs an extended final summary.

Use this timing pattern for generated voiceover segments:

```python
target_duration = 18.0  # replace with probed voice duration
state_durations = [6.0, 6.0, 6.0]  # sum must match target_duration


self.play(FadeIn(title), run_time=1.0)
self.wait(max(0, state_durations[0] - 1.0))

self.play(ReplacementTransform(state_1, state_2), run_time=0.8)
self.wait(max(0, state_durations[1] - 0.8))

self.play(ReplacementTransform(state_2, state_3), run_time=0.8)
self.wait(max(0, state_durations[2] - 0.8))
```

## Manim Code Rules

- Use `from manim import *` unless a narrower import is clearly better.
- Define exactly one primary scene class for the requested video, usually named `GeneratedScene`.
- Subclass one of `Scene`, `MovingCameraScene`, `ThreeDScene`, or `ZoomedScene`.
- Put all animation logic inside `construct(self)`.
- Keep the first render simple enough to compile, then refine.
- Use `Text` or `MarkupText` for ordinary labels. Use `MathTex` only when LaTeX is needed and likely available.
- For Chinese text, prefer `Text("Chinese text here", font="Microsoft YaHei")` on Windows when a specific font is needed; replace the sample text with the requested Chinese copy.
- Avoid interactive calls, network access, blocking input, absolute user-specific asset paths, and nondeterministic external dependencies.
- Keep objects inside the camera frame with `.scale()`, `.to_edge()`, `.next_to()`, `.arrange()`, and `.move_to()`.
- Add `self.wait()` at meaningful beats so the output is watchable.
- For segment clips, the last frame must not be empty unless the narration has also ended. Prefer holding the final summary, diagram, or keyword group on screen.
- Avoid ending normal voiceover segments with `self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=...)`. That pattern often creates a long blank freeze when the audio is longer than the visible animation.
- Avoid a catch-all final wait such as `hold = target_duration - elapsed; self.wait(hold)` after short earlier states. Distribute wait time into every visual state.
- Avoid cumulative screen construction. Do not leave more than one major content group visible unless the layout was designed as a comparison.
- Avoid raw absolute placement for many independent objects. Prefer building one `VGroup`, arranging it, fitting it, then animating that group.
- Never put important content in the bottom subtitle band when the finished video may include subtitles.
- Default to a normal non-transparent video. Do not use `--transparent` unless the user explicitly asks for transparent background or alpha output.
- For transparent-background clips, avoid relying on a solid scene background unless the user asked for one.

## Horizontal Video Layout Rules

Use these rules for all generated videos by default. Always produce horizontal 16:9 video, including for Douyin, Kuaishou, Bilibili, YouTube, and other platforms, unless the user explicitly asks for a different aspect ratio.

- Set horizontal config at the top of the generated code:

```python
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_width = 16
config.frame_height = 9
```

- Design for horizontal composition first. Use left/right layouts, center-stage diagrams, and top-to-bottom information hierarchy as appropriate.
- Keep all important content inside a safe area:
  - max width: `config.frame_width * 0.88`
  - max height: `config.frame_height * 0.72` when subtitles may be present
  - max height: `config.frame_height * 0.82` only when subtitles are disabled
  - edge margin: at least `0.45` frame units
- Treat the bottom `config.frame_height * 0.15` as a subtitle-safe band. Do not place core labels, summary text, callouts, arrows, or boxes there in narrated videos.
- Limit each scene to one main idea, one title, and at most three dense visual elements.
- Limit each visual state to one title and at most three content items. If the script needs more, create another state instead of another row.
- Split long text into short lines. Do not create one full-width `Text` object for long Chinese or English sentences.
- Use body font sizes around 30-42 and titles around 48-68 for 1920x1080 scenes.
- For dense technical videos, prefer body font sizes 26-34 and avoid more than 18 Chinese characters per line.
- Never place title, subtitle, diagram, and bullet list at the same coordinates. Build one `VGroup` and arrange it.
- After building a group, always fit it before animating:
  - if too wide, `scale_to_fit_width(config.frame_width * 0.88)`
  - if too tall, `scale_to_fit_height(config.frame_height * 0.72)` for narrated videos with subtitles
  - then `move_to(ORIGIN)` or a deliberate safe position
- Use split-screen layouts only when both sides remain readable within the 16:9 safe area.
- For split-screen layouts, each side gets at most one heading plus three short rows. Use `scale_to_fit_width(config.frame_width * 0.38)` for each column group.
- Prefer replacing dense paragraphs with 2-4 keyword chips or staged reveals.

Use this helper pattern in generated horizontal scenes:

```python
SUBTITLE_SAFE_HEIGHT = config.frame_height * 0.72


def fit_safe(mob, max_width=None, max_height=None):
    max_width = max_width or config.frame_width * 0.88
    max_height = max_height or SUBTITLE_SAFE_HEIGHT
    if mob.width > max_width:
        mob.scale_to_fit_width(max_width)
    if mob.height > max_height:
        mob.scale_to_fit_height(max_height)
    return mob


def safe_stack(*mobs, buff=0.35):
    group = VGroup(*mobs).arrange(DOWN, buff=buff)
    fit_safe(group)
    group.move_to(UP * 0.25)
    return group


def safe_text(text, font_size=34, color=WHITE, max_chars=18):
    chunks = [text[i:i + max_chars] for i in range(0, len(text), max_chars)]
    return Text("\n".join(chunks), font="Microsoft YaHei", font_size=font_size, color=color, line_spacing=0.9)
```

Before rendering, review the scene code and check:

- Every text-heavy screen uses `safe_stack` or equivalent fitting.
- No group is intentionally wider than `config.frame_width * 0.92`.
- No group is intentionally taller than `config.frame_height * 0.72` when subtitles are present.
- Dense content is revealed in stages instead of all at once.
- Each major visual state has a single `VGroup` variable such as `state_1`, `state_2`, or `current_state`.
- The code does not keep old state groups visible while adding unrelated new state groups.
- The code does not place important content with `to_edge(DOWN)` or `move_to(DOWN * 3...)` in narrated videos.

## Anti-Overlap Protocol

Use this protocol for narrated explainer segments by default:

1. Build visual states as separate `VGroup`s.
2. Assign each state a duration budget before writing `self.play` calls.
3. Fit each state with `fit_safe`.
4. Show only one state at a time, except deliberate two-column comparisons.
5. Replace old states before adding new states.
6. Hold every state for its own budget. Do not put all leftover time on the final state.

Recommended pattern:

```python
target_duration = 19.5
state_durations = [6.5, 6.5, 6.5]

state_1 = safe_stack(title_1, chips_1)
state_2 = safe_stack(title_2, comparison_group)
state_3 = safe_stack(title_3, takeaway)

intro = 0.8
self.play(FadeIn(state_1), run_time=intro)
self.wait(max(0, state_durations[0] - intro))

transition = 0.8
self.play(ReplacementTransform(state_1, state_2), run_time=transition)
self.wait(max(0, state_durations[1] - transition))

self.play(ReplacementTransform(state_2, state_3), run_time=transition)
self.wait(max(0, state_durations[2] - transition))
```

For generated code, assert or comment the timing sum:

```python
# Timing: sum(state_durations) == target_duration, within 0.15s.
```

Do not use this risky pattern for dense videos:

```python
self.play(FadeIn(group_a))
self.play(FadeIn(group_b))
self.play(FadeIn(group_c))
self.play(FadeIn(group_d))
```

That cumulative pattern is only acceptable when all groups were arranged together in one fitted parent `VGroup` before animation.

Also avoid this front-loaded timing pattern:

```python
elapsed = 0
# many short animations...
hold = max(0, target_duration - elapsed)
self.wait(hold)  # creates a long final freeze
```

## Render Command

Create or choose a job directory for the current task, then run:

```powershell
python <skill_dir>/scripts/run_manim_script.py `
  --job-dir <job_dir>/segments/001 `
  --code-file <job_dir>/segments/001/input_scene.py `
  --quality ql
```

Useful options:

- `--scene-name GeneratedScene`: use when the scene class name cannot be auto-detected.
- `--quality ql`: fast preview render.
- `--quality qm`: medium render for a better preview.
- `--quality qh` or `--quality qk`: slower final render.
- `--transparent`: render with alpha channel, usually as `.mov`; use only when the user explicitly asks for transparency.
- `--no-transparent`: force a normal non-transparent render. This is the default and usually produces `.mp4`.
- `--timeout 300`: increase for complex 3D or high-quality renders.
- `--manim-command <command>`: use a specific Manim executable when the default `python -m manim` environment does not have Manim installed.

The helper copies the supplied code into:

```text
<job-dir>/source/generated_scene.py
```

It writes output metadata, logs, and the final video into:

```text
<job-dir>/output/render_result.json
<job-dir>/output/render.log
<job-dir>/output/video/
```

Manim partial movie files are intentionally rendered in a temporary directory outside the workspace to avoid overwhelming the host file watcher during rerenders. Do not depend on `output/media/...` paths; use the `video_path` field from `render_result.json`.

## Bundled Reference Docs

The bundled `docs/` directory contains a local markdown copy of the Manim Community reference manual for quick API lookup. It was generated from Manim Community docs v0.20.1 with `build_docs/crawl_manim_reference.py`. See `NOTICE` for third-party attribution.

## Render Result Contract

The script prints JSON and writes the same JSON to `render_result.json`.

Important fields:

- `success`: true only when Manim exits successfully and a video file is found.
- `scene_name`: scene class used for rendering.
- `video_path`: final `.mov`, `.mp4`, or `.webm` path when available.
- `code_path`: copied source file rendered by Manim.
- `log_path`: full render log.
- `render_log_tail`: last part of the render log, useful for quick debugging.
- `result_path`: JSON result file path.
- `elapsed_seconds`: render duration.

## Minimal Example

```python
from manim import *


class GeneratedScene(Scene):
    def construct(self):
        title = Text("Vector Addition", font_size=44).to_edge(UP)
        plane = NumberPlane().scale(0.75)
        a = Vector([2, 1], color=BLUE)
        b = Vector([1, 2], color=GREEN).shift(a.get_end())
        c = Vector([3, 3], color=YELLOW)
        label = MathTex(r"\vec a + \vec b").next_to(c.get_end(), RIGHT)

        self.play(FadeIn(plane), Write(title))
        self.play(Create(a))
        self.play(Create(b))
        self.play(Create(c), FadeIn(label))
        self.wait(1)
```

## Troubleshooting

- `ModuleNotFoundError: manim`: Manim is not installed in the Python environment used by `python`. If another Manim executable is available, rerun with `--manim-command <path-to-manim>`.
- `LaTeX error` or `latex not found`: replace `Tex`/`MathTex` with `Text`, or simplify formulas.
- `No video file generated`: read `render_log_tail` first, then `output/render.log`.
- Scene not found: pass `--scene-name`, or rename the main scene class to `GeneratedScene`.
- Text missing or boxes appear: specify a font available on the machine, especially for Chinese text.
- Very slow render: switch to `--quality ql`, reduce object count, reduce 3D surface resolution, or shorten long animations.
