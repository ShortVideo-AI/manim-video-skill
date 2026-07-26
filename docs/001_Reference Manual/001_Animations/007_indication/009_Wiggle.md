---
{
  "title": "Wiggle",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.indication.Wiggle.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "indication",
    "Wiggle"
  ],
  "scraped_at": "2026-07-10T15:58:00"
}
---

# Wiggle

Qualified name: `manim.animation.indication.Wiggle`

class Wiggle(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html)
:   Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)

    Wiggle a Mobject.

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobject to wiggle.
        - **scale\_value** (*float*) – The factor by which the mobject will be temporarily scaled.
        - **rotation\_angle** (*float*) – The wiggle angle.
        - **n\_wiggles** (*int*) – The number of wiggles.
        - **scale\_about\_point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* *None*) – The point about which the mobject gets scaled.
        - **rotate\_about\_point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* *None*) – The point around which the mobject gets rotated.
        - **run\_time** (*float*) – The duration of the animation
        - **kwargs** (*Any*)

    Examples

    Example: ApplyingWaves

    [
    ](./ApplyingWaves-2.mp4)

    ```
    class ApplyingWaves(Scene):
        def construct(self):
            tex = Tex("Wiggle").scale(3)
            self.play(Wiggle(tex))
            self.wait()
    ```

    Methods

    |  |  |
    | --- | --- |
    | `get_rotate_about_point` |  |
    | `get_scale_about_point` |  |
    | `interpolate_submobject` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *scale\_value=1.1*, *rotation\_angle=0.06283185307179587*, *n\_wiggles=6*, *scale\_about\_point=None*, *rotate\_about\_point=None*, *run\_time=2*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **scale\_value** (*float*)
            - **rotation\_angle** (*float*)
            - **n\_wiggles** (*int*)
            - **scale\_about\_point** (*TypeAliasForwardRef**(**'~manim.typing.Point3DLike'**)* *|* *None*)
            - **rotate\_about\_point** (*TypeAliasForwardRef**(**'~manim.typing.Point3DLike'**)* *|* *None*)
            - **run\_time** (*float*)
            - **kwargs** (*Any*)
