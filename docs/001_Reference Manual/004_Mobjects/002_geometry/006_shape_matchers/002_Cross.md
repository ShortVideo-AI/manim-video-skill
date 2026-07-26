---
{
  "title": "Cross",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.Cross.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "shape_matchers",
    "Cross"
  ],
  "scraped_at": "2026-07-10T15:59:13"
}
---

# Cross

Qualified name: `manim.mobject.geometry.shape\_matchers.Cross`

class Cross(*mobject=None*, *stroke\_color=ManimColor('#FC6255')*, *stroke\_width=6.0*, *scale\_factor=1.0*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/shape_matchers.html)
:   Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    Creates a cross.

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) *|* *None*) – The mobject linked to this instance. It fits the mobject when specified. Defaults to None.
        - **stroke\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html)) – Specifies the color of the cross lines. Defaults to RED.
        - **stroke\_width** (*float*) – Specifies the width of the cross lines. Defaults to 6.
        - **scale\_factor** (*float*) – Scales the cross to the provided units. Defaults to 1.
        - **kwargs** (*Any*)

    Examples

    Example: ExampleCross

    ![../_images/ExampleCross-1.png](https://docs.manim.community/en/stable/_images/ExampleCross-1.png)

    ```
    class ExampleCross(Scene):
        def construct(self):
            cross = Cross()
            self.add(cross)
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*mobject=None*, *stroke\_color=ManimColor('#FC6255')*, *stroke\_width=6.0*, *scale\_factor=1.0*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) *|* *None*)
            - **stroke\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
            - **stroke\_width** (*float*)
            - **scale\_factor** (*float*)
            - **kwargs** (*Any*)

        Return type:
        :   None
