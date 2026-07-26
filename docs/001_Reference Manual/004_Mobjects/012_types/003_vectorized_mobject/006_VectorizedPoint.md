---
{
  "title": "VectorizedPoint",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VectorizedPoint.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "types",
    "vectorized_mobject",
    "VectorizedPoint"
  ],
  "scraped_at": "2026-07-10T16:00:38"
}
---

# VectorizedPoint

Qualified name: `manim.mobject.types.vectorized\_mobject.VectorizedPoint`

class VectorizedPoint(*location=array([0., 0., 0.])*, *color=ManimColor('#000000')*, *fill\_opacity=0*, *stroke\_width=0*, *artificial\_width=0.01*, *artificial\_height=0.01*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    Methods

    |  |  |
    | --- | --- |
    | `get_location` |  |
    | `set_location` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | [`height`](#manim.mobject.types.vectorized_mobject.VectorizedPoint.height) | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | [`width`](#manim.mobject.types.vectorized_mobject.VectorizedPoint.width) | The width of the mobject. |

    Parameters:
    :   - **location** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **color** ([*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html))
        - **fill\_opacity** (*float*)
        - **stroke\_width** (*float*)
        - **artificial\_width** (*float*)
        - **artificial\_height** (*float*)

    \_original\_\_init\_\_(*location=array([0., 0., 0.])*, *color=ManimColor('#000000')*, *fill\_opacity=0*, *stroke\_width=0*, *artificial\_width=0.01*, *artificial\_height=0.01*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **location** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **color** ([*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html))
            - **fill\_opacity** (*float*)
            - **stroke\_width** (*float*)
            - **artificial\_width** (*float*)
            - **artificial\_height** (*float*)

        Return type:
        :   None

    basecls
    :   alias of [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    property height: float
    :   The height of the mobject.

        Return type:
        :   `float`

        Examples

        Example: HeightExample

        [
        ](./HeightExample-2.mp4)

        ```
        class HeightExample(Scene):
            def construct(self):
                decimal = DecimalNumber().to_edge(UP)
                rect = Rectangle(color=BLUE)
                rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

                decimal.add_updater(lambda d: d.set_value(rect.height))

                self.add(rect_copy, rect, decimal)
                self.play(rect.animate.set(height=5))
                self.wait()
        ```

        See also

        `length_over_dim()`

    property width: float
    :   The width of the mobject.

        Return type:
        :   `float`

        Examples

        Example: WidthExample

        [
        ](./WidthExample-2.mp4)

        ```
        class WidthExample(Scene):
            def construct(self):
                decimal = DecimalNumber().to_edge(UP)
                rect = Rectangle(color=BLUE)
                rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

                decimal.add_updater(lambda d: d.set_value(rect.width))

                self.add(rect_copy, rect, decimal)
                self.play(rect.animate.set(width=7))
                self.wait()
        ```

        See also

        `length_over_dim()`
