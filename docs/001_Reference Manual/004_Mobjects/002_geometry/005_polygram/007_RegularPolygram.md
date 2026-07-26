---
{
  "title": "RegularPolygram",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygram.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "polygram",
    "RegularPolygram"
  ],
  "scraped_at": "2026-07-10T15:59:09"
}
---

# RegularPolygram

Qualified name: `manim.mobject.geometry.polygram.RegularPolygram`

class RegularPolygram(*num\_vertices*, *\**, *density=2*, *radius=1*, *start\_angle=None*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/polygram.html)
:   Bases: [`Polygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygram.html)

    A [`Polygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygram.html) with regularly spaced vertices.

    Parameters:
    :   - **num\_vertices** (*int*) – The number of vertices.
        - **density** (*int*) –

          The density of the [`RegularPolygram`](#manim.mobject.geometry.polygram.RegularPolygram).

          Can be thought of as how many vertices to hop
          to draw a line between them. Every `density`-th
          vertex is connected.
        - **radius** (*float*) – The radius of the circle that the vertices are placed on.
        - **start\_angle** (*float* *|* *None*) – The angle the vertices start at; the rotation of
          the [`RegularPolygram`](#manim.mobject.geometry.polygram.RegularPolygram).
        - **kwargs** (*Any*) – Forwarded to the parent constructor.

    Examples

    Example: RegularPolygramExample

    ![../_images/RegularPolygramExample-1.png](https://docs.manim.community/en/stable/_images/RegularPolygramExample-1.png)

    ```
    class RegularPolygramExample(Scene):
        def construct(self):
            pentagram = RegularPolygram(5, radius=2)
            self.add(pentagram)
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

    \_original\_\_init\_\_(*num\_vertices*, *\**, *density=2*, *radius=1*, *start\_angle=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **num\_vertices** (*int*)
            - **density** (*int*)
            - **radius** (*float*)
            - **start\_angle** (*float* *|* *None*)
            - **kwargs** (*Any*)

        Return type:
        :   None
