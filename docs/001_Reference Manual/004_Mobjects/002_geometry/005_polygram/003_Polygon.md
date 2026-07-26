---
{
  "title": "Polygon",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "polygram",
    "Polygon"
  ],
  "scraped_at": "2026-07-10T15:59:06"
}
---

# Polygon

Qualified name: `manim.mobject.geometry.polygram.Polygon`

class Polygon(*\*vertices*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/polygram.html)
:   Bases: [`Polygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygram.html)

    A shape consisting of one closed loop of vertices.

    Parameters:
    :   - **vertices** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The vertices of the [`Polygon`](#manim.mobject.geometry.polygram.Polygon).
        - **kwargs** (*Any*) – Forwarded to the parent constructor.

    Examples

    Example: PolygonExample

    ![../_images/PolygonExample-1.png](https://docs.manim.community/en/stable/_images/PolygonExample-1.png)

    ```
    class PolygonExample(Scene):
        def construct(self):
            isosceles = Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-3.5, -2, 0])
            position_list = [
                [4, 1, 0],  # middle right
                [4, -2.5, 0],  # bottom right
                [0, -2.5, 0],  # bottom left
                [0, 3, 0],  # top left
                [2, 1, 0],  # middle
                [4, 3, 0],  # top right
            ]
            square_and_triangles = Polygon(*position_list, color=PURPLE_B)
            self.add(isosceles, square_and_triangles)
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

    \_original\_\_init\_\_(*\*vertices*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **vertices** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **kwargs** (*Any*)

        Return type:
        :   None
