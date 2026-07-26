---
{
  "title": "Indicate",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.indication.Indicate.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "indication",
    "Indicate"
  ],
  "scraped_at": "2026-07-10T15:57:57"
}
---

# Indicate

Qualified name: `manim.animation.indication.Indicate`

class Indicate(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html)
:   Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html)

    Indicate a Mobject by temporarily resizing and recoloring it.

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobject to indicate.
        - **scale\_factor** (*float*) – The factor by which the mobject will be temporally scaled
        - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html)) – The color the mobject temporally takes.
        - **rate\_func** ([*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html)) – The function defining the animation progress at every point in time.
        - **kwargs** (*Any*) – Additional arguments to be passed to the [`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html) constructor

    Examples

    Example: UsingIndicate

    [
    ](./UsingIndicate-1.mp4)

    ```
    class UsingIndicate(Scene):
        def construct(self):
            tex = Tex("Indicate").scale(3)
            self.play(Indicate(tex))
            self.wait()
    ```

    Methods

    |  |  |
    | --- | --- |
    | `create_target` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *scale\_factor=1.2*, *color=ManimColor('#FFFF00')*, *rate\_func=<function there\_and\_back>*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **scale\_factor** (*float*)
            - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
            - **rate\_func** ([*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html))
            - **kwargs** (*Any*)
