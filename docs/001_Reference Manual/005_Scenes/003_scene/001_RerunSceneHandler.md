---
{
  "title": "RerunSceneHandler",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.scene.scene.RerunSceneHandler.html",
  "tree_path": [
    "Reference Manual",
    "Scenes",
    "scene",
    "RerunSceneHandler"
  ],
  "scraped_at": "2026-07-10T16:00:49"
}
---

# RerunSceneHandler

Qualified name: `manim.scene.scene.RerunSceneHandler`

class RerunSceneHandler(*queue*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html)
:   Bases: `FileSystemEventHandler`

    A class to handle rerunning a Scene after the input file is modified.

    Methods

    |  |  |
    | --- | --- |
    | [`on_modified`](#manim.scene.scene.RerunSceneHandler.on_modified) | Called when a file or directory is modified. |

    Parameters:
    :   **queue** (*Queue**[*[*SceneInteractAction*](https://docs.manim.community/en/stable/reference/manim.scene.scene.html)*]*)

    on\_modified(*event*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html)
    :   Called when a file or directory is modified.

        Parameters:
        :   **event** (`DirModifiedEvent` or `FileModifiedEvent`) – Event representing file/directory modification.

        Return type:
        :   None
