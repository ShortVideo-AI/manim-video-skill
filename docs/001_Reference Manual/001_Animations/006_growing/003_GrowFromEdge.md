---
{
  "title": "GrowFromEdge",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromEdge.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "growing",
    "GrowFromEdge"
  ],
  "scraped_at": "2026-07-10T15:57:52"
}
---

# GrowFromEdge

Qualified name: `manim.animation.growing.GrowFromEdge`

class GrowFromEdge(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/growing.html)
:   Bases: [`GrowFromPoint`](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromPoint.html)

    Introduce an [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) by growing it from one of its bounding box edges.

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobjects to be introduced.
        - **edge** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The direction to seek bounding box edge of mobject.
        - **point\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.
        - **kwargs** (*Any*)

    Examples

    Example: GrowFromEdgeExample

    [
    ](./GrowFromEdgeExample-1.mp4)

    ```
    class GrowFromEdgeExample(Scene):
        def construct(self):
            squares = [Square() for _ in range(4)]
            VGroup(*squares).set_x(0).arrange(buff=1)
            self.play(GrowFromEdge(squares[0], DOWN))
            self.play(GrowFromEdge(squares[1], RIGHT))
            self.play(GrowFromEdge(squares[2], UR))
            self.play(GrowFromEdge(squares[3], UP, point_color=RED))
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *edge*, *point\_color=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **edge** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **point\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*)
            - **kwargs** (*Any*)
