---
{
  "title": "Ellipse",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Ellipse.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "arc",
    "Ellipse"
  ],
  "scraped_at": "2026-07-10T15:58:49"
}
---

# Ellipse

Qualified name: `manim.mobject.geometry.arc.Ellipse`

class Ellipse(*width=2*, *height=1*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
:   Bases: [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html)

    A circular shape; oval, circle.

    Parameters:
    :   - **width** (*float*) – The horizontal width of the ellipse.
        - **height** (*float*) – The vertical height of the ellipse.
        - **kwargs** (*Any*) – Additional arguments to be passed to [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html).

    Examples

    Example: EllipseExample

    ![../_images/EllipseExample-1.png](https://docs.manim.community/en/stable/_images/EllipseExample-1.png)

    ```
    class EllipseExample(Scene):
        def construct(self):
            ellipse_1 = Ellipse(width=2.0, height=4.0, color=BLUE_B)
            ellipse_2 = Ellipse(width=4.0, height=1.0, color=BLUE_D)
            ellipse_group = Group(ellipse_1,ellipse_2).arrange(buff=1)
            self.add(ellipse_group)
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

    \_original\_\_init\_\_(*width=2*, *height=1*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **width** (*float*)
            - **height** (*float*)
            - **kwargs** (*Any*)

        Return type:
        :   None
