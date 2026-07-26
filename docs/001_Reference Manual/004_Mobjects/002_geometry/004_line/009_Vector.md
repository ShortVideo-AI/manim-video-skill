---
{
  "title": "Vector",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "line",
    "Vector"
  ],
  "scraped_at": "2026-07-10T15:59:04"
}
---

# Vector

Qualified name: `manim.mobject.geometry.line.Vector`

class Vector(*direction=array([1., 0., 0.])*, *buff=0*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
:   Bases: [`Arrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html)

    A vector specialized for use in graphs.

    Caution

    Do not confuse with the [`Vector2D`](https://docs.manim.community/en/stable/reference/manim.typing.html),
    [`Vector3D`](https://docs.manim.community/en/stable/reference/manim.typing.html) or [`VectorND`](https://docs.manim.community/en/stable/reference/manim.typing.html) type aliases,
    which are not Mobjects!

    Parameters:
    :   - **direction** ([*Vector2DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* [*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The direction of the arrow.
        - **buff** (*float*) – The distance of the vector from its endpoints.
        - **kwargs** (*Any*) – Additional arguments to be passed to [`Arrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html)

    Examples

    Example: VectorExample

    ![../_images/VectorExample-1.png](https://docs.manim.community/en/stable/_images/VectorExample-1.png)

    ```
    class VectorExample(Scene):
        def construct(self):
            plane = NumberPlane()
            vector_1 = Vector([1,2])
            vector_2 = Vector([-5,-2])
            self.add(plane, vector_1, vector_2)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`coordinate_label`](#manim.mobject.geometry.line.Vector.coordinate_label) | Creates a label based on the coordinates of the vector. |

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

    \_original\_\_init\_\_(*direction=array([1., 0., 0.])*, *buff=0*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **direction** (*TypeAliasForwardRef**(**'~manim.typing.Vector2DLike'**)* *|* *TypeAliasForwardRef**(**'~manim.typing.Vector3DLike'**)*)
            - **buff** (*float*)
            - **kwargs** (*Any*)

        Return type:
        :   None

    coordinate\_label(*integer\_labels=True*, *n\_dim=2*, *color=None*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
    :   Creates a label based on the coordinates of the vector.

        Parameters:
        :   - **integer\_labels** (*bool*) – Whether or not to round the coordinates to integers.
            - **n\_dim** (*int*) – The number of dimensions of the vector.
            - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*) – Sets the color of label, optional.
            - **kwargs** (*Any*) – Additional arguments to be passed to [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html).

        Returns:
        :   The label.

        Return type:
        :   [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html)

        Examples

        Example: VectorCoordinateLabel

        ![../_images/VectorCoordinateLabel-1.png](https://docs.manim.community/en/stable/_images/VectorCoordinateLabel-1.png)

        ```
        class VectorCoordinateLabel(Scene):
            def construct(self):
                plane = NumberPlane()

                vec_1 = Vector([1, 2])
                vec_2 = Vector([-3, -2])
                label_1 = vec_1.coordinate_label()
                label_2 = vec_2.coordinate_label(color=YELLOW)

                self.add(plane, vec_1, vec_2, label_1, label_2)
        ```
