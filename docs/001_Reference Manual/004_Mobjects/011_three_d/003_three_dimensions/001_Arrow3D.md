---
{
  "title": "Arrow3D",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Arrow3D.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "three_d",
    "three_dimensions",
    "Arrow3D"
  ],
  "scraped_at": "2026-07-10T16:00:17"
}
---

# Arrow3D

Qualified name: `manim.mobject.three\_d.three\_dimensions.Arrow3D`

class Arrow3D(*start=array([-1., 0., 0.])*, *end=array([1., 0., 0.])*, *thickness=0.02*, *height=0.3*, *base\_radius=0.08*, *color=ManimColor('#FFFFFF')*, *resolution=24*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
:   Bases: [`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html)

    An arrow made out of a cylindrical line and a conical tip.

    Parameters:
    :   - **start** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The start position of the arrow.
        - **end** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The end position of the arrow.
        - **thickness** (*float*) – The thickness of the arrow.
        - **height** (*float*) – The height of the conical tip.
        - **base\_radius** (*float*) – The base radius of the conical tip.
        - **color** ([*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)) – The color of the arrow.
        - **resolution** (*int* *|* *tuple**[**int**,* *int**]*) – The resolution of the arrow line.
        - **kwargs** (*Any*)

    Examples

    Example: ExampleArrow3D

    ![../_images/ExampleArrow3D-1.png](https://docs.manim.community/en/stable/_images/ExampleArrow3D-1.png)

    ```
    class ExampleArrow3D(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            arrow = Arrow3D(
                start=np.array([0, 0, 0]),
                end=np.array([2, 2, 2]),
                resolution=8
            )
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            self.add(axes, arrow)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`get_end`](#manim.mobject.three_d.three_dimensions.Arrow3D.get_end) | Returns the ending point of the [`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html). |

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

    \_original\_\_init\_\_(*start=array([-1., 0., 0.])*, *end=array([1., 0., 0.])*, *thickness=0.02*, *height=0.3*, *base\_radius=0.08*, *color=ManimColor('#FFFFFF')*, *resolution=24*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **start** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **end** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **thickness** (*float*)
            - **height** (*float*)
            - **base\_radius** (*float*)
            - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
            - **resolution** (*int* *|* *tuple**[**int**,* *int**]*)
            - **kwargs** (*Any*)

        Return type:
        :   None

    get\_end()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
    :   Returns the ending point of the [`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html).

        Returns:
        :   **end** – Ending point of the [`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html).

        Return type:
        :   `numpy.array`
