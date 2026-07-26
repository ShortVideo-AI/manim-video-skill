---
{
  "title": "ImageMobjectFromCamera",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.types.image_mobject.ImageMobjectFromCamera.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "types",
    "image_mobject",
    "ImageMobjectFromCamera"
  ],
  "scraped_at": "2026-07-10T16:00:27"
}
---

# ImageMobjectFromCamera

Qualified name: `manim.mobject.types.image\_mobject.ImageMobjectFromCamera`

class ImageMobjectFromCamera(*camera*, *default\_display\_frame\_config=None*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/image_mobject.html)
:   Bases: [`AbstractImageMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.image_mobject.AbstractImageMobject.html)

    Methods

    |  |  |
    | --- | --- |
    | `add_display_frame` |  |
    | `get_pixel_array` |  |
    | `interpolate_color` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `depth` | The depth of the mobject. |
    | `height` | The height of the mobject. |
    | `width` | The width of the mobject. |

    Parameters:
    :   - **camera** ([*MovingCamera*](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html))
        - **default\_display\_frame\_config** (*dict**[**str**,* *Any**]* *|* *None*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*camera*, *default\_display\_frame\_config=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **camera** ([*MovingCamera*](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html))
            - **default\_display\_frame\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            - **kwargs** (*Any*)

        Return type:
        :   None
