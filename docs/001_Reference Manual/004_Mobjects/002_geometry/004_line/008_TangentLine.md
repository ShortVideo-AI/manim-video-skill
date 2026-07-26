---
{
  "title": "TangentLine",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.TangentLine.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "line",
    "TangentLine"
  ],
  "scraped_at": "2026-07-10T15:59:03"
}
---

# TangentLine

Qualified name: `manim.mobject.geometry.line.TangentLine`

class TangentLine(*vmob*, *alpha*, *length=1*, *d\_alpha=1e-06*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
:   Bases: [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html)

    Constructs a line tangent to a [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) at a specific point.

    Parameters:
    :   - **vmob** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)) – The VMobject on which the tangent line is drawn.
        - **alpha** (*float*) – How far along the shape that the line will be constructed. range: 0-1.
        - **length** (*float*) – Length of the tangent line.
        - **d\_alpha** (*float*) – The `dx` value
        - **kwargs** (*Any*) – Additional arguments to be passed to [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html)

    See also

    [`point_from_proportion()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    Examples

    Example: TangentLineExample

    ![../_images/TangentLineExample-1.png](https://docs.manim.community/en/stable/_images/TangentLineExample-1.png)

    ```
    class TangentLineExample(Scene):
        def construct(self):
            circle = Circle(radius=2)
            line_1 = TangentLine(circle, alpha=0.0, length=4, color=BLUE_D) # right
            line_2 = TangentLine(circle, alpha=0.4, length=4, color=GREEN) # top left
            self.add(circle, line_1, line_2)
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

    \_original\_\_init\_\_(*vmob*, *alpha*, *length=1*, *d\_alpha=1e-06*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **vmob** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))
            - **alpha** (*float*)
            - **length** (*float*)
            - **d\_alpha** (*float*)
            - **kwargs** (*Any*)

        Return type:
        :   None
