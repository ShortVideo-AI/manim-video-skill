---
{
  "title": "SpinInFromNothing",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.growing.SpinInFromNothing.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "growing",
    "SpinInFromNothing"
  ],
  "scraped_at": "2026-07-10T15:57:53"
}
---

# SpinInFromNothing

Qualified name: `manim.animation.growing.SpinInFromNothing`

class SpinInFromNothing(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/growing.html)
:   Bases: [`GrowFromCenter`](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromCenter.html)

    Introduce an [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) spinning and growing it from its center.

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobjects to be introduced.
        - **angle** (*float*) – The amount of spinning before mobject reaches its full size. E.g. 2\*PI means
          that the object will do one full spin before being fully introduced.
        - **point\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.
        - **kwargs** (*Any*)

    Examples

    Example: SpinInFromNothingExample

    [
    ](./SpinInFromNothingExample-1.mp4)

    ```
    class SpinInFromNothingExample(Scene):
        def construct(self):
            squares = [Square() for _ in range(3)]
            VGroup(*squares).set_x(0).arrange(buff=2)
            self.play(SpinInFromNothing(squares[0]))
            self.play(SpinInFromNothing(squares[1], angle=2 * PI))
            self.play(SpinInFromNothing(squares[2], point_color=RED))
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *angle=1.5707963267948966*, *point\_color=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **angle** (*float*)
            - **point\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*)
            - **kwargs** (*Any*)
