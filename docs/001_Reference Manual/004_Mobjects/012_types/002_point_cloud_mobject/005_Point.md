---
{
  "title": "Point",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.Point.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "types",
    "point_cloud_mobject",
    "Point"
  ],
  "scraped_at": "2026-07-10T16:00:31"
}
---

# Point

Qualified name: `manim.mobject.types.point\_cloud\_mobject.Point`

class Point(*location=array([0., 0., 0.])*, *color=ManimColor('#000000')*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html)
:   Bases: [`PMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html)

    A mobject representing a point.

    Examples

    Example: ExamplePoint

    ![../_images/ExamplePoint-1.png](https://docs.manim.community/en/stable/_images/ExamplePoint-1.png)

    ```
    class ExamplePoint(Scene):
        def construct(self):
            colorList = [RED, GREEN, BLUE, YELLOW]
            for i in range(200):
                point = Point(location=[0.63 * np.random.randint(-4, 4), 0.37 * np.random.randint(-4, 4), 0], color=np.random.choice(colorList))
                self.add(point)
            for i in range(200):
                point = Point(location=[0.37 * np.random.randint(-4, 4), 0.63 * np.random.randint(-4, 4), 0], color=np.random.choice(colorList))
                self.add(point)
            self.add(point)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.types.point_cloud_mobject.Point.generate_points) | Initializes `points` and therefore the shape. |
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
    :   - **location** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **color** ([*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html))
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*location=array([0., 0., 0.])*, *color=ManimColor('#000000')*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **location** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
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
