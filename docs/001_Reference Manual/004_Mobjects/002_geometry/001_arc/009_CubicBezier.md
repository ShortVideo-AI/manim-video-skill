---
{
  "title": "CubicBezier",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CubicBezier.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "arc",
    "CubicBezier"
  ],
  "scraped_at": "2026-07-10T15:58:47"
}
---

# CubicBezier

Qualified name: `manim.mobject.geometry.arc.CubicBezier`

class CubicBezier(*start\_anchor*, *start\_handle*, *end\_handle*, *end\_anchor*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    A cubic Bézier curve.

    Example

    Example: BezierSplineExample

    ![../_images/BezierSplineExample-1.png](https://docs.manim.community/en/stable/_images/BezierSplineExample-1.png)

    ```
    class BezierSplineExample(Scene):
        def construct(self):
            p1 = np.array([-3, 1, 0])
            p1b = p1 + [1, 0, 0]
            d1 = Dot(point=p1).set_color(BLUE)
            l1 = Line(p1, p1b)
            p2 = np.array([3, -1, 0])
            p2b = p2 - [1, 0, 0]
            d2 = Dot(point=p2).set_color(RED)
            l2 = Line(p2, p2b)
            bezier = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
            self.add(l1, d1, l2, d2, bezier)
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
    :   - **start\_anchor** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **start\_handle** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **end\_handle** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **end\_anchor** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*start\_anchor*, *start\_handle*, *end\_handle*, *end\_anchor*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **start\_anchor** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **start\_handle** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **end\_handle** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **end\_anchor** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **kwargs** (*Any*)

        Return type:
        :   None
