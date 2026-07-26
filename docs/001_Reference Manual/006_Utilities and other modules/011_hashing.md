---
{
  "title": "hashing",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.hashing.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "hashing"
  ],
  "scraped_at": "2026-07-10T16:01:33"
}
---

# hashing

Utilities for scene caching.

Functions

get\_hash\_from\_play\_call(*scene\_object*, *camera\_object*, *animations\_list*, *current\_mobjects\_list*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/hashing.html)
:   Take the list of animations and a list of mobjects and output their hashes. This is meant to be used for scene.play function.

    Parameters:
    :   - **scene\_object** ([*Scene*](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html)) – The scene object.
        - **camera\_object** ([*Camera*](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html) *|* *OpenGLCamera*) – The camera object used in the scene.
        - **animations\_list** (*Iterable**[*[*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)*]*) – The list of animations.
        - **current\_mobjects\_list** (*Iterable**[*[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]*) – The list of mobjects.

    Returns:
    :   A string concatenation of the respective hashes of camera\_object, animations\_list and current\_mobjects\_list, separated by \_.

    Return type:
    :   `str`

get\_json(*obj*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/hashing.html)
:   Recursively serialize object to JSON using the `CustomEncoder` class.

    Parameters:
    :   **obj** (*Any*) – The dict to flatten

    Returns:
    :   The flattened object

    Return type:
    :   `str`
