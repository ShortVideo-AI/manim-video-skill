---
{
  "title": "GrowFromCenter",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromCenter.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "growing",
    "GrowFromCenter"
  ],
  "scraped_at": "2026-07-10T15:57:51"
}
---

# GrowFromCenter

Qualified name: `manim.animation.growing.GrowFromCenter`

class GrowFromCenter(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/growing.html)
:   Bases: [`GrowFromPoint`](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromPoint.html)

    Introduce an [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) by growing it from its center.

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobjects to be introduced.
        - **point\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.
        - **kwargs** (*Any*)

    Examples

    Example: GrowFromCenterExample

    [
    ](./GrowFromCenterExample-1.mp4)

    ```
    class GrowFromCenterExample(Scene):
        def construct(self):
            squares = [Square() for _ in range(2)]
            VGroup(*squares).set_x(0).arrange(buff=2)
            self.play(GrowFromCenter(squares[0]))
            self.play(GrowFromCenter(squares[1], point_color=RED))
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *point\_color=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **point\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*)
            - **kwargs** (*Any*)
