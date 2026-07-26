---
{
  "title": "GrowFromPoint",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromPoint.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "growing",
    "GrowFromPoint"
  ],
  "scraped_at": "2026-07-10T15:57:52"
}
---

# GrowFromPoint

Qualified name: `manim.animation.growing.GrowFromPoint`

class GrowFromPoint(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/growing.html)
:   Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html)

    Introduce an [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) by growing it from a point.

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobjects to be introduced.
        - **point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The point from which the mobject grows.
        - **point\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.
        - **kwargs** (*Any*)

    Examples

    Example: GrowFromPointExample

    [
    ](./GrowFromPointExample-1.mp4)

    ```
    class GrowFromPointExample(Scene):
        def construct(self):
            dot = Dot(3 * UR, color=GREEN)
            squares = [Square() for _ in range(4)]
            VGroup(*squares).set_x(0).arrange(buff=1)
            self.add(dot)
            self.play(GrowFromPoint(squares[0], ORIGIN))
            self.play(GrowFromPoint(squares[1], [-2, 2, 0]))
            self.play(GrowFromPoint(squares[2], [3, -2, 0], RED))
            self.play(GrowFromPoint(squares[3], dot, dot.get_color()))
    ```

    Methods

    |  |  |
    | --- | --- |
    | `create_starting_mobject` |  |
    | `create_target` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *point*, *point\_color=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **point\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*)
            - **kwargs** (*Any*)
