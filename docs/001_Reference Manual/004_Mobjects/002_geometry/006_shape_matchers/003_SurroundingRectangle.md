---
{
  "title": "SurroundingRectangle",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "shape_matchers",
    "SurroundingRectangle"
  ],
  "scraped_at": "2026-07-10T15:59:14"
}
---

# SurroundingRectangle

Qualified name: `manim.mobject.geometry.shape\_matchers.SurroundingRectangle`

class SurroundingRectangle(*\*mobjects*, *color=ManimColor('#FFFF00')*, *buff=0.1*, *corner\_radius=0.0*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/shape_matchers.html)
:   Bases: [`RoundedRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RoundedRectangle.html)

    A rectangle surrounding a [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)

    Examples

    Example: SurroundingRectExample

    ![../_images/SurroundingRectExample-1.png](https://docs.manim.community/en/stable/_images/SurroundingRectExample-1.png)

    ```
    class SurroundingRectExample(Scene):
        def construct(self):
            title = Title("A Quote from Newton")
            quote = Text(
                "If I have seen further than others, \n"
                "it is by standing upon the shoulders of giants.",
                color=BLUE,
            ).scale(0.75)
            box = SurroundingRectangle(quote, color=YELLOW, buff=MED_LARGE_BUFF)

            t2 = Tex(r"Hello World").scale(1.5)
            box2 = SurroundingRectangle(t2, corner_radius=0.2)
            mobjects = VGroup(VGroup(box, quote), VGroup(t2, box2)).arrange(DOWN)
            self.add(title, mobjects)
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

    Parameters:
    :   - **mobjects** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
        - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
        - **buff** (*float* *|* *tuple**[**float**,* *float**]*)
        - **corner\_radius** (*float*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*\*mobjects*, *color=ManimColor('#FFFF00')*, *buff=0.1*, *corner\_radius=0.0*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobjects** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
            - **buff** (*float* *|* *tuple**[**float**,* *float**]*)
            - **corner\_radius** (*float*)
            - **kwargs** (*Any*)

        Return type:
        :   None
