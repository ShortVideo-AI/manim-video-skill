---
{
  "title": "Line",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "line",
    "Line"
  ],
  "scraped_at": "2026-07-10T15:59:02"
}
---

# Line

Qualified name: `manim.mobject.geometry.line.Line`

class Line(*start=array([-1., 0., 0.])*, *end=array([1., 0., 0.])*, *buff=0*, *path\_arc=0*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
:   Bases: [`TipableVMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.TipableVMobject.html)

    A straight or curved line segment between two points or mobjects.

    Parameters:
    :   - **start** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* [*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The starting point or Mobject of the line.
        - **end** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* [*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The ending point or Mobject of the line.
        - **buff** (*float*) – The distance to shorten the line from both ends.
        - **path\_arc** (*float*) – If nonzero, the line will be curved into an arc with this angle (in radians).
        - **kwargs** (*Any*) – Additional arguments to be passed to `TipableVMobject`

    Examples

    Example: LineExample

    ![../_images/LineExample-1.png](https://docs.manim.community/en/stable/_images/LineExample-1.png)

    ```
    class LineExample(Scene):
        def construct(self):
            line1 = Line(LEFT*2, RIGHT*2)
            line2 = Line(LEFT*2, RIGHT*2, buff=0.5)
            line3 = Line(LEFT*2, RIGHT*2, path_arc=PI/2)
            grp = VGroup(line1,line2,line3).arrange(DOWN, buff=2)
            self.add(grp)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.geometry.line.Line.generate_points) | Initializes `points` and therefore the shape. |
    | `get_angle` |  |
    | [`get_projection`](#manim.mobject.geometry.line.Line.get_projection) | Returns the projection of a point onto a line. |
    | `get_slope` |  |
    | `get_unit_vector` |  |
    | `get_vector` |  |
    | `init_points` |  |
    | [`put_start_and_end_on`](#manim.mobject.geometry.line.Line.put_start_and_end_on) | Sets starts and end coordinates of a line. |
    | `set_angle` |  |
    | `set_length` |  |
    | `set_path_arc` |  |
    | [`set_points_by_ends`](#manim.mobject.geometry.line.Line.set_points_by_ends) | Sets the points of the line based on its start and end points. |

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

    \_original\_\_init\_\_(*start=array([-1., 0., 0.])*, *end=array([1., 0., 0.])*, *buff=0*, *path\_arc=0*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **start** (*TypeAliasForwardRef**(**'~manim.typing.Point3DLike'**)* *|* [*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **end** (*TypeAliasForwardRef**(**'~manim.typing.Point3DLike'**)* *|* [*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **buff** (*float*)
            - **path\_arc** (*float*)
            - **kwargs** (*Any*)

        Return type:
        :   None

    \_pointify(*mob\_or\_point*, *direction=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
    :   Transforms a mobject into its corresponding point. Does nothing if a point is passed.

        `direction` determines the location of the point along its bounding box in that direction.

        Parameters:
        :   - **mob\_or\_point** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) *|* *TypeAliasForwardRef**(**'~manim.typing.Point3DLike'**)*) – The mobject or point.
            - **direction** (*TypeAliasForwardRef**(**'~manim.typing.Vector3DLike'**)* *|* *None*) – The direction.

        Return type:
        :   [*Point3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)

    generate\_points()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   None

    get\_projection(*point*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
    :   Returns the projection of a point onto a line.

        Parameters:
        :   **point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The point to which the line is projected.

        Return type:
        :   [*Point3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)

    put\_start\_and\_end\_on(*start*, *end*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
    :   Sets starts and end coordinates of a line.

        Examples

        Example: LineExample

        [
        ](./LineExample-2.mp4)

        ```
        class LineExample(Scene):
            def construct(self):
                d = VGroup()
                for i in range(0,10):
                    d.add(Dot())
                d.arrange_in_grid(buff=1)
                self.add(d)
                l= Line(d[0], d[1])
                self.add(l)
                self.wait()
                l.put_start_and_end_on(d[1].get_center(), d[2].get_center())
                self.wait()
                l.put_start_and_end_on(d[4].get_center(), d[7].get_center())
                self.wait()
        ```

        Parameters:
        :   - **start** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **end** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))

        Return type:
        :   Self

    set\_points\_by\_ends(*start*, *end*, *buff=0*, *path\_arc=0*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
    :   Sets the points of the line based on its start and end points.
        Unlike [`put_start_and_end_on()`](#manim.mobject.geometry.line.Line.put_start_and_end_on), this method respects self.buff and
        Mobject bounding boxes.

        Parameters:
        :   - **start** (*TypeAliasForwardRef**(**'~manim.typing.Point3DLike'**)* *|* [*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The start point or Mobject of the line.
            - **end** (*TypeAliasForwardRef**(**'~manim.typing.Point3DLike'**)* *|* [*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The end point or Mobject of the line.
            - **buff** (*float*) – The empty space between the start and end of the line, by default 0.
            - **path\_arc** (*float*) – The angle of a circle spanned by this arc, by default 0 which is a straight line.

        Return type:
        :   None
