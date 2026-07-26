---
{
  "title": "GrowArrow",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowArrow.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "growing",
    "GrowArrow"
  ],
  "scraped_at": "2026-07-10T15:57:51"
}
---

# GrowArrow

Qualified name: `manim.animation.growing.GrowArrow`

class GrowArrow(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/growing.html)
:   Bases: [`GrowFromPoint`](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromPoint.html)

    Introduce an [`Arrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html) by growing it from its start toward its tip.

    Parameters:
    :   - **arrow** ([*Arrow*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html)) – The arrow to be introduced.
        - **point\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*) – Initial color of the arrow before growing to its full size. Leave empty to match arrow’s color.
        - **kwargs** (*Any*)

    Examples

    Example: GrowArrowExample

    [
    ](./GrowArrowExample-1.mp4)

    ```
    class GrowArrowExample(Scene):
        def construct(self):
            arrows = [Arrow(2 * LEFT, 2 * RIGHT), Arrow(2 * DR, 2 * UL)]
            VGroup(*arrows).set_x(0).arrange(buff=2)
            self.play(GrowArrow(arrows[0]))
            self.play(GrowArrow(arrows[1], point_color=RED))
    ```

    Methods

    |  |  |
    | --- | --- |
    | `create_starting_mobject` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*arrow*, *point\_color=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **arrow** ([*Arrow*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html))
            - **point\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*)
            - **kwargs** (*Any*)
