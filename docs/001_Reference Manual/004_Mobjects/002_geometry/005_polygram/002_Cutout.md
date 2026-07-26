---
{
  "title": "Cutout",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Cutout.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "polygram",
    "Cutout"
  ],
  "scraped_at": "2026-07-10T15:59:05"
}
---

# Cutout

Qualified name: `manim.mobject.geometry.polygram.Cutout`

class Cutout(*main\_shape*, *\*mobjects*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/polygram.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    A shape with smaller cutouts.

    Parameters:
    :   - **main\_shape** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)) – The primary shape from which cutouts are made.
        - **mobjects** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)) – The smaller shapes which are to be cut out of the `main_shape`.
        - **kwargs** (*Any*) – Further keyword arguments that are passed to the constructor of
          [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html).

    Warning

    Technically, this class behaves similar to a symmetric difference: if
    parts of the `mobjects` are not located within the `main_shape`,
    these parts will be added to the resulting [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html).

    Examples

    Example: CutoutExample

    [
    ](./CutoutExample-1.mp4)

    ```
    class CutoutExample(Scene):
        def construct(self):
            s1 = Square().scale(2.5)
            s2 = Triangle().shift(DOWN + RIGHT).scale(0.5)
            s3 = Square().shift(UP + RIGHT).scale(0.5)
            s4 = RegularPolygon(5).shift(DOWN + LEFT).scale(0.5)
            s5 = RegularPolygon(6).shift(UP + LEFT).scale(0.5)
            c = Cutout(s1, s2, s3, s4, s5, fill_opacity=1, color=BLUE, stroke_color=RED)
            self.play(Write(c), run_time=4)
            self.wait()
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

    \_original\_\_init\_\_(*main\_shape*, *\*mobjects*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **main\_shape** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))
            - **mobjects** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))
            - **kwargs** (*Any*)

        Return type:
        :   None
