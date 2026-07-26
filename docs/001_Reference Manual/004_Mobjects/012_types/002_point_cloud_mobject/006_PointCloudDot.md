---
{
  "title": "PointCloudDot",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PointCloudDot.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "types",
    "point_cloud_mobject",
    "PointCloudDot"
  ],
  "scraped_at": "2026-07-10T16:00:31"
}
---

# PointCloudDot

Qualified name: `manim.mobject.types.point\_cloud\_mobject.PointCloudDot`

class PointCloudDot(*center=array([0., 0., 0.])*, *radius=2.0*, *stroke\_width=2*, *density=10*, *color=ManimColor('#FFFF00')*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html)
:   Bases: [`Mobject1D`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.Mobject1D.html)

    A disc made of a cloud of dots.

    Examples

    Example: PointCloudDotExample

    ![../_images/PointCloudDotExample-1.png](https://docs.manim.community/en/stable/_images/PointCloudDotExample-1.png)

    ```
    class PointCloudDotExample(Scene):
        def construct(self):
            cloud_1 = PointCloudDot(color=RED)
            cloud_2 = PointCloudDot(stroke_width=4, radius=1)
            cloud_3 = PointCloudDot(density=15)

            group = Group(cloud_1, cloud_2, cloud_3).arrange()
            self.add(group)
    ```

    Example: PointCloudDotExample2

    [
    ](./PointCloudDotExample2-1.mp4)

    ```
    class PointCloudDotExample2(Scene):
        def construct(self):
            plane = ComplexPlane()
            cloud = PointCloudDot(color=RED)
            self.add(
                plane, cloud
            )
            self.wait()
            self.play(
                cloud.animate.apply_complex_function(lambda z: np.exp(z))
            )
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.types.point_cloud_mobject.PointCloudDot.generate_points) | Initializes `points` and therefore the shape. |
    | `init_points` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `depth` | The depth of the mobject. |
    | `height` | The height of the mobject. |
    | `width` | The width of the mobject. |

    Parameters:
    :   - **center** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **radius** (*float*)
        - **stroke\_width** (*int*)
        - **density** (*int*)
        - **color** ([*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html))
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*center=array([0., 0., 0.])*, *radius=2.0*, *stroke\_width=2*, *density=10*, *color=ManimColor('#FFFF00')*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **center** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **radius** (*float*)
            - **stroke\_width** (*int*)
            - **density** (*int*)
            - **color** ([*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html))
            - **kwargs** (*Any*)

        Return type:
        :   None

    generate\_points()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html)
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   None
