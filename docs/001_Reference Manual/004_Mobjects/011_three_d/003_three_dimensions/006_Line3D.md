---
{
  "title": "Line3D",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "three_d",
    "three_dimensions",
    "Line3D"
  ],
  "scraped_at": "2026-07-10T16:00:21"
}
---

# Line3D

Qualified name: `manim.mobject.three\_d.three\_dimensions.Line3D`

class Line3D(*start=array([-1., 0., 0.])*, *end=array([1., 0., 0.])*, *thickness=0.02*, *color=None*, *resolution=24*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
:   Bases: [`Cylinder`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cylinder.html)

    A cylindrical line, for use in ThreeDScene.

    Parameters:
    :   - **start** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The start point of the line.
        - **end** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The end point of the line.
        - **thickness** (*float*) – The thickness of the line.
        - **color** ([*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)) – The color of the line.
        - **resolution** (*tuple**[**int**,* *int**]*) – The resolution of the line.
          By default this value is the number of points the line will sampled at.
          If you want the line to also come out checkered, use a tuple.
          For example, for a line made of 24 points with 4 checker points on each
          cylinder, pass the tuple (4, 24).
        - **kwargs** (*Any*)

    Examples

    Example: ExampleLine3D

    ![../_images/ExampleLine3D-1.png](https://docs.manim.community/en/stable/_images/ExampleLine3D-1.png)

    ```
    class ExampleLine3D(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            line = Line3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 2]))
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            self.add(axes, line)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`get_end`](#manim.mobject.three_d.three_dimensions.Line3D.get_end) | Returns the ending point of the [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D). |
    | [`get_start`](#manim.mobject.three_d.three_dimensions.Line3D.get_start) | Returns the starting point of the [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D). |
    | [`parallel_to`](#manim.mobject.three_d.three_dimensions.Line3D.parallel_to) | Returns a line parallel to another line going through a given point. |
    | [`perpendicular_to`](#manim.mobject.three_d.three_dimensions.Line3D.perpendicular_to) | Returns a line perpendicular to another line going through a given point. |
    | [`pointify`](#manim.mobject.three_d.three_dimensions.Line3D.pointify) | Gets a point representing the center of the [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html). |
    | [`set_start_and_end_attrs`](#manim.mobject.three_d.three_dimensions.Line3D.set_start_and_end_attrs) | Sets the start and end points of the line. |

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

    \_original\_\_init\_\_(*start=array([-1., 0., 0.])*, *end=array([1., 0., 0.])*, *thickness=0.02*, *color=None*, *resolution=24*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **start** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **end** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **thickness** (*float*)
            - **color** (*TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)* *|* *None*)
            - **resolution** (*int* *|* *tuple**[**int**,* *int**]*)
            - **kwargs** (*Any*)

    get\_end()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
    :   Returns the ending point of the [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D).

        Returns:
        :   **end** – Ending point of the [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D).

        Return type:
        :   `numpy.array`

    get\_start()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
    :   Returns the starting point of the [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D).

        Returns:
        :   **start** – Starting point of the [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D).

        Return type:
        :   `numpy.array`

    classmethod parallel\_to(*line*, *point=array([0., 0., 0.])*, *length=5*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
    :   Returns a line parallel to another line going through
        a given point.

        Parameters:
        :   - **line** ([*Line3D*](#manim.mobject.three_d.three_dimensions.Line3D)) – The line to be parallel to.
            - **point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The point to pass through.
            - **length** (*float*) – Length of the parallel line.
            - **kwargs** (*Any*) – Additional parameters to be passed to the class.

        Returns:
        :   Line parallel to `line`.

        Return type:
        :   [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D)

        Examples

        Example: ParallelLineExample

        ![../_images/ParallelLineExample-1.png](https://docs.manim.community/en/stable/_images/ParallelLineExample-1.png)

        ```
        class ParallelLineExample(ThreeDScene):
            def construct(self):
                self.set_camera_orientation(PI / 3, -PI / 4)
                ax = ThreeDAxes((-5, 5), (-5, 5), (-5, 5), 10, 10, 10)
                line1 = Line3D(RIGHT * 2, UP + OUT, color=RED)
                line2 = Line3D.parallel_to(line1, color=YELLOW)
                self.add(ax, line1, line2)
        ```

    classmethod perpendicular\_to(*line*, *point=array([0., 0., 0.])*, *length=5*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
    :   Returns a line perpendicular to another line going through
        a given point.

        Parameters:
        :   - **line** ([*Line3D*](#manim.mobject.three_d.three_dimensions.Line3D)) – The line to be perpendicular to.
            - **point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The point to pass through.
            - **length** (*float*) – Length of the perpendicular line.
            - **kwargs** (*Any*) – Additional parameters to be passed to the class.

        Returns:
        :   Line perpendicular to `line`.

        Return type:
        :   [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D)

        Examples

        Example: PerpLineExample

        ![../_images/PerpLineExample-1.png](https://docs.manim.community/en/stable/_images/PerpLineExample-1.png)

        ```
        class PerpLineExample(ThreeDScene):
            def construct(self):
                self.set_camera_orientation(PI / 3, -PI / 4)
                ax = ThreeDAxes((-5, 5), (-5, 5), (-5, 5), 10, 10, 10)
                line1 = Line3D(RIGHT * 2, UP + OUT, color=RED)
                line2 = Line3D.perpendicular_to(line1, color=BLUE)
                self.add(ax, line1, line2)
        ```

    pointify(*mob\_or\_point*, *direction=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
    :   Gets a point representing the center of the [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).

        Parameters:
        :   - **mob\_or\_point** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) *|* *TypeAliasForwardRef**(**'~manim.typing.Point3DLike'**)*) – [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) or point whose center should be returned.
            - **direction** (*TypeAliasForwardRef**(**'~manim.typing.Vector3DLike'**)* *|* *None*) – If an edge of a [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) should be returned, the direction of the edge.

        Returns:
        :   Center of the [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) or point, or edge if direction is given.

        Return type:
        :   `numpy.array`

    set\_start\_and\_end\_attrs(*start*, *end*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
    :   Sets the start and end points of the line.

        If either `start` or `end` are [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html),
        this gives their centers.

        Parameters:
        :   - **start** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – Starting point or `Mobject`.
            - **end** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – Ending point or `Mobject`.
            - **kwargs** (*Any*)

        Return type:
        :   None
