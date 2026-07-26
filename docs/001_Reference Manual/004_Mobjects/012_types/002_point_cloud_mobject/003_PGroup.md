---
{
  "title": "PGroup",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PGroup.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "types",
    "point_cloud_mobject",
    "PGroup"
  ],
  "scraped_at": "2026-07-10T16:00:29"
}
---

# PGroup

Qualified name: `manim.mobject.types.point\_cloud\_mobject.PGroup`

class PGroup(*\*pmobs*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html)
:   Bases: [`PMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html)

    A group for several point mobjects.

    Examples

    Example: PgroupExample

    ![../_images/PgroupExample-1.png](https://docs.manim.community/en/stable/_images/PgroupExample-1.png)

    ```
    class PgroupExample(Scene):
        def construct(self):

            p1 = PointCloudDot(radius=1, density=20, color=BLUE)
            p1.move_to(4.5 * LEFT)
            p2 = PointCloudDot()
            p3 = PointCloudDot(radius=1.5, stroke_width=2.5, color=PINK)
            p3.move_to(4.5 * RIGHT)
            pList = PGroup(p1, p2, p3)

            self.add(pList)
    ```

    Methods

    |  |  |
    | --- | --- |
    | `fade_to` |  |

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
    :   - **pmobs** (*Any*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*\*pmobs*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **pmobs** (*Any*)
            - **kwargs** (*Any*)

        Return type:
        :   None
