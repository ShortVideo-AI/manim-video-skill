---
{
  "title": "scene",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.scene.scene.html",
  "tree_path": [
    "Reference Manual",
    "Scenes",
    "scene"
  ],
  "scraped_at": "2026-07-10T16:00:48"
}
---

# scene

Basic canvas for animations.

Type Aliases

class SceneInteractAction
:   ```
    MethodWithArgs | 'SceneInteractContinue' | 'SceneInteractRerun'
    ```

Classes

| Name | Description |
| --- | --- |
| [`RerunSceneHandler`](https://docs.manim.community/en/stable/reference/manim.scene.scene.RerunSceneHandler.html) | A class to handle rerunning a Scene after the input file is modified. |
| [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) | A Scene is the canvas of your animation. |
| [`SceneInteractContinue`](https://docs.manim.community/en/stable/reference/manim.scene.scene.SceneInteractContinue.html) | Object which, when encountered in `Scene.interact()`, triggers the end of the scene interaction, continuing with the rest of the animations, if any. |
| [`SceneInteractRerun`](https://docs.manim.community/en/stable/reference/manim.scene.scene.SceneInteractRerun.html) | Object which, when encountered in `Scene.interact()`, triggers the rerun of the scene. |
