---
{
  "title": "FocusOn",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.indication.FocusOn.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "indication",
    "FocusOn"
  ],
  "scraped_at": "2026-07-10T15:57:57"
}
---

# FocusOn

Qualified name: `manim.animation.indication.FocusOn`

class FocusOn(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html)
:   Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html)

    Shrink a spotlight to a position.

    Parameters:
    :   - **focus\_point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* [*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The point at which to shrink the spotlight. If it is a `Mobject` its center will be used.
        - **opacity** (*float*) – The opacity of the spotlight.
        - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html)) – The color of the spotlight.
        - **run\_time** (*float*) – The duration of the animation.
        - **kwargs** (*Any*)

    Examples

    Example: UsingFocusOn

    [
    ](./UsingFocusOn-1.mp4)

    ```
    class UsingFocusOn(Scene):
        def construct(self):
            dot = Dot(color=PURE_YELLOW).shift(DOWN)
            self.add(Tex("Focusing on the dot below:"), dot)
            self.play(FocusOn(dot))
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

    \_original\_\_init\_\_(*focus\_point*, *opacity=0.2*, *color=ManimColor('#888888')*, *run\_time=2*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **focus\_point** (*TypeAliasForwardRef**(**'~manim.typing.Point3DLike'**)* *|* [*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **opacity** (*float*)
            - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
            - **run\_time** (*float*)
            - **kwargs** (*Any*)
