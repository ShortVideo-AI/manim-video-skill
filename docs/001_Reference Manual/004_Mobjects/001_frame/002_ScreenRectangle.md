---
{
  "title": "ScreenRectangle",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.frame.ScreenRectangle.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "frame",
    "ScreenRectangle"
  ],
  "scraped_at": "2026-07-10T15:58:41"
}
---

# ScreenRectangle

Qualified name: `manim.mobject.frame.ScreenRectangle`

class ScreenRectangle(*aspect\_ratio=1.7777777777777777*, *height=4*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/frame.html)
:   Bases: [`Rectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Rectangle.html)

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | [`aspect_ratio`](#manim.mobject.frame.ScreenRectangle.aspect_ratio) | The aspect ratio. |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    Parameters:
    :   - **aspect\_ratio** (*float*)
        - **height** (*float*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*aspect\_ratio=1.7777777777777777*, *height=4*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **aspect\_ratio** (*float*)
            - **height** (*float*)
            - **kwargs** (*Any*)

        Return type:
        :   None

    property aspect\_ratio: float
    :   The aspect ratio.

        When set, the width is stretched to accommodate
        the new aspect ratio.
