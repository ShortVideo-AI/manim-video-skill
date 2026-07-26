---
{
  "title": "SceneInteractContinue",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.scene.scene.SceneInteractContinue.html",
  "tree_path": [
    "Reference Manual",
    "Scenes",
    "scene",
    "SceneInteractContinue"
  ],
  "scraped_at": "2026-07-10T16:00:51"
}
---

# SceneInteractContinue

Qualified name: `manim.scene.scene.SceneInteractContinue`

class SceneInteractContinue(*sender*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html)
:   Bases: `object`

    Object which, when encountered in `Scene.interact()`, triggers
    the end of the scene interaction, continuing with the rest of the
    animations, if any. This object can be queued in `Scene.queue`
    for later use in `Scene.interact()`.

    Parameters:
    :   **sender** (*str*)

    sender
    :   The name of the entity which issued the end of the scene interaction,
        such as `"gui"` or `"keyboard"`.

        Type:
        :   str

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | [`sender`](#manim.scene.scene.SceneInteractContinue.sender) |  |
