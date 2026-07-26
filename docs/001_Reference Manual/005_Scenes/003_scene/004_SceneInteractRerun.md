---
{
  "title": "SceneInteractRerun",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.scene.scene.SceneInteractRerun.html",
  "tree_path": [
    "Reference Manual",
    "Scenes",
    "scene",
    "SceneInteractRerun"
  ],
  "scraped_at": "2026-07-10T16:00:51"
}
---

# SceneInteractRerun

Qualified name: `manim.scene.scene.SceneInteractRerun`

class SceneInteractRerun(*sender*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html)
:   Bases: `object`

    Object which, when encountered in `Scene.interact()`, triggers
    the rerun of the scene. This object can be queued in `Scene.queue`
    for later use in `Scene.interact()`.

    Parameters:
    :   - **sender** (*str*)
        - **kwargs** (*Any*)

    sender
    :   The name of the entity which issued the rerun of the scene, such as
        `"gui"`, `"keyboard"`, `"play"` or `"file"`.

        Type:
        :   str

    kwargs
    :   Additional keyword arguments when rerunning the scene. Currently,
        only `"from_animation_number"` is being used, which determines the
        animation from which to start rerunning the scene.

        Type:
        :   dict[str, Any]

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | [`sender`](#manim.scene.scene.SceneInteractRerun.sender) |  |
    | [`kwargs`](#manim.scene.scene.SceneInteractRerun.kwargs) |  |
