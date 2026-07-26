---
{
  "title": "ApplyWave",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.indication.ApplyWave.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "indication",
    "ApplyWave"
  ],
  "scraped_at": "2026-07-10T15:57:54"
}
---

# ApplyWave

Qualified name: `manim.animation.indication.ApplyWave`

class ApplyWave(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html)
:   Bases: [`Homotopy`](https://docs.manim.community/en/stable/reference/manim.animation.movement.Homotopy.html)

    Send a wave through the Mobject distorting it temporarily.

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobject to be distorted.
        - **direction** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The direction in which the wave nudges points of the shape
        - **amplitude** (*float*) – The distance points of the shape get shifted
        - **wave\_func** ([*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html)) – The function defining the shape of one wave flank.
        - **time\_width** (*float*) – The length of the wave relative to the width of the mobject.
        - **ripples** (*int*) – The number of ripples of the wave
        - **run\_time** (*float*) – The duration of the animation.
        - **kwargs** (*Any*)

    Examples

    Example: ApplyingWaves

    [
    ](./ApplyingWaves-1.mp4)

    ```
    class ApplyingWaves(Scene):
        def construct(self):
            tex = Tex("WaveWaveWaveWaveWave").scale(2)
            self.play(ApplyWave(tex))
            self.play(ApplyWave(
                tex,
                direction=RIGHT,
                time_width=0.5,
                amplitude=0.3
            ))
            self.play(ApplyWave(
                tex,
                rate_func=linear,
                ripples=4
            ))
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *direction=array([0.*, *1.*, *0.])*, *amplitude=0.2*, *wave\_func=<function smooth>*, *time\_width=1*, *ripples=1*, *run\_time=2*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **direction** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **amplitude** (*float*)
            - **wave\_func** ([*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html))
            - **time\_width** (*float*)
            - **ripples** (*int*)
            - **run\_time** (*float*)
            - **kwargs** (*Any*)
