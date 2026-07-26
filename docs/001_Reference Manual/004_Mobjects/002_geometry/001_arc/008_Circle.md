---
{
  "title": "Circle",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "arc",
    "Circle"
  ],
  "scraped_at": "2026-07-10T15:58:47"
}
---

# Circle

Qualified name: `manim.mobject.geometry.arc.Circle`

class Circle(*radius=None*, *color=ManimColor('#FC6255')*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
:   Bases: [`Arc`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html)

    A circle.

    Parameters:
    :   - **color** ([*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)) – The color of the shape.
        - **kwargs** (*Any*) – Additional arguments to be passed to [`Arc`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html)
        - **radius** (*float* *|* *None*)

    Examples

    Example: CircleExample

    ![../_images/CircleExample-1.png](https://docs.manim.community/en/stable/_images/CircleExample-1.png)

    ```
    class CircleExample(Scene):
        def construct(self):
            circle_1 = Circle(radius=1.0)
            circle_2 = Circle(radius=1.5, color=GREEN)
            circle_3 = Circle(radius=1.0, color=BLUE_B, fill_opacity=1)

            circle_group = Group(circle_1, circle_2, circle_3).arrange(buff=1)
            self.add(circle_group)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`from_three_points`](#manim.mobject.geometry.arc.Circle.from_three_points) | Returns a circle passing through the specified three points. |
    | [`point_at_angle`](#manim.mobject.geometry.arc.Circle.point_at_angle) | Returns the position of a point on the circle. |
    | [`surround`](#manim.mobject.geometry.arc.Circle.surround) | Modifies a circle so that it surrounds a given mobject. |

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

    \_original\_\_init\_\_(*radius=None*, *color=ManimColor('#FC6255')*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **radius** (*float* *|* *None*)
            - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
            - **kwargs** (*Any*)

        Return type:
        :   None

    static from\_three\_points(*p1*, *p2*, *p3*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
    :   Returns a circle passing through the specified
        three points.

        Example

        Example: CircleFromPointsExample

        ![../_images/CircleFromPointsExample-1.png](https://docs.manim.community/en/stable/_images/CircleFromPointsExample-1.png)

        ```
        class CircleFromPointsExample(Scene):
            def construct(self):
                circle = Circle.from_three_points(LEFT, LEFT + UP, UP * 2, color=RED)
                dots = VGroup(
                    Dot(LEFT),
                    Dot(LEFT + UP),
                    Dot(UP * 2),
                )
                self.add(NumberPlane(), circle, dots)
        ```

        Parameters:
        :   - **p1** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **p2** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **p3** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **kwargs** (*Any*)

        Return type:
        :   [*Circle*](#manim.mobject.geometry.arc.Circle)

    point\_at\_angle(*angle*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
    :   Returns the position of a point on the circle.

        Parameters:
        :   **angle** (*float*) – The angle of the point along the circle in radians.

        Returns:
        :   The location of the point along the circle’s circumference.

        Return type:
        :   `numpy.ndarray`

        Examples

        Example: PointAtAngleExample

        ![../_images/PointAtAngleExample-1.png](https://docs.manim.community/en/stable/_images/PointAtAngleExample-1.png)

        ```
        class PointAtAngleExample(Scene):
            def construct(self):
                circle = Circle(radius=2.0)
                p1 = circle.point_at_angle(PI/2)
                p2 = circle.point_at_angle(270*DEGREES)

                s1 = Square(side_length=0.25).move_to(p1)
                s2 = Square(side_length=0.25).move_to(p2)
                self.add(circle, s1, s2)
        ```

    surround(*mobject*, *dim\_to\_match=0*, *stretch=False*, *buffer\_factor=1.2*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
    :   Modifies a circle so that it surrounds a given mobject.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobject that the circle will be surrounding.
            - **dim\_to\_match** (*int*)
            - **buffer\_factor** (*float*) – Scales the circle with respect to the mobject. A buffer\_factor < 1 makes the circle smaller than the mobject.
            - **stretch** (*bool*) – Stretches the circle to fit more tightly around the mobject. Note: Does not work with `Line`

        Return type:
        :   Self

        Examples

        Example: CircleSurround

        ![../_images/CircleSurround-1.png](https://docs.manim.community/en/stable/_images/CircleSurround-1.png)

        ```
        class CircleSurround(Scene):
            def construct(self):
                triangle1 = Triangle()
                circle1 = Circle().surround(triangle1)
                group1 = Group(triangle1,circle1) # treat the two mobjects as one

                line2 = Line()
                circle2 = Circle().surround(line2, buffer_factor=2.0)
                group2 = Group(line2,circle2)

                # buffer_factor < 1, so the circle is smaller than the square
                square3 = Square()
                circle3 = Circle().surround(square3, buffer_factor=0.5)
                group3 = Group(square3, circle3)

                group = Group(group1, group2, group3).arrange(buff=1)
                self.add(group)
        ```
