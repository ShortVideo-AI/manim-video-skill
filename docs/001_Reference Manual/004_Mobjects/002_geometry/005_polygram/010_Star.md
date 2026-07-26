---
{
  "title": "Star",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Star.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "polygram",
    "Star"
  ],
  "scraped_at": "2026-07-10T15:59:11"
}
---

# Star

Qualified name: `manim.mobject.geometry.polygram.Star`

class Star(*n=5*, *\**, *outer\_radius=1*, *inner\_radius=None*, *density=2*, *start\_angle=1.5707963267948966*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/polygram.html)
:   Bases: [`Polygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html)

    A regular polygram without the intersecting lines.

    Parameters:
    :   - **n** (*int*) – How many points on the [`Star`](#manim.mobject.geometry.polygram.Star).
        - **outer\_radius** (*float*) – The radius of the circle that the outer vertices are placed on.
        - **inner\_radius** (*float* *|* *None*) –

          The radius of the circle that the inner vertices are placed on.

          If unspecified, the inner radius will be
          calculated such that the edges of the [`Star`](#manim.mobject.geometry.polygram.Star)
          perfectly follow the edges of its [`RegularPolygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygram.html)
          counterpart.
        - **density** (*int*) –

          The density of the [`Star`](#manim.mobject.geometry.polygram.Star). Only used if
          `inner_radius` is unspecified.

          See [`RegularPolygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygram.html) for more information.
        - **start\_angle** (*float* *|* *None*) – The angle the vertices start at; the rotation of
          the [`Star`](#manim.mobject.geometry.polygram.Star).
        - **kwargs** (*Any*) – Forwardeds to the parent constructor.

    Raises:
    :   **ValueError** – If `inner_radius` is unspecified and `density`
        is not in the range `[1, n/2)`.

    Examples

    Example: StarExample

    [
    ](./StarExample-1.mp4)

    ```
    class StarExample(Scene):
        def construct(self):
            pentagram = RegularPolygram(5, radius=2)
            star = Star(outer_radius=2, color=RED)

            self.add(pentagram)
            self.play(Create(star), run_time=3)
            self.play(FadeOut(star), run_time=2)
    ```

    Example: DifferentDensitiesExample

    ![../_images/DifferentDensitiesExample-1.png](https://docs.manim.community/en/stable/_images/DifferentDensitiesExample-1.png)

    ```
    class DifferentDensitiesExample(Scene):
        def construct(self):
            density_2 = Star(7, outer_radius=2, density=2, color=RED)
            density_3 = Star(7, outer_radius=2, density=3, color=PURPLE)

            self.add(VGroup(density_2, density_3).arrange(RIGHT))
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

    \_original\_\_init\_\_(*n=5*, *\**, *outer\_radius=1*, *inner\_radius=None*, *density=2*, *start\_angle=1.5707963267948966*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **n** (*int*)
            - **outer\_radius** (*float*)
            - **inner\_radius** (*float* *|* *None*)
            - **density** (*int*)
            - **start\_angle** (*float* *|* *None*)
            - **kwargs** (*Any*)

        Return type:
        :   None
