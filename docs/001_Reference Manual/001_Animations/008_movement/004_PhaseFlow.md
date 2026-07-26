---
{
  "title": "PhaseFlow",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.movement.PhaseFlow.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "movement",
    "PhaseFlow"
  ],
  "scraped_at": "2026-07-10T15:58:03"
}
---

# PhaseFlow

Qualified name: `manim.animation.movement.PhaseFlow`

class PhaseFlow(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/movement.html)
:   Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)

    Methods

    |  |  |
    | --- | --- |
    | [`interpolate_mobject`](#manim.animation.movement.PhaseFlow.interpolate_mobject) | Interpolates the mobject of the `Animation` based on alpha value. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   - **function** (*Callable**[**[**np.ndarray**]**,* *np.ndarray**]*)
        - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
        - **virtual\_time** (*float*)
        - **suspend\_mobject\_updating** (*bool*)
        - **rate\_func** ([*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html))
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*function*, *mobject*, *virtual\_time=1*, *suspend\_mobject\_updating=False*, *rate\_func=<function linear>*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **function** (*Callable**[**[**np.ndarray**]**,* *np.ndarray**]*)
            - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **virtual\_time** (*float*)
            - **suspend\_mobject\_updating** (*bool*)
            - **rate\_func** ([*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html))
            - **kwargs** (*Any*)

    interpolate\_mobject(*alpha*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/movement.html)
    :   Interpolates the mobject of the `Animation` based on alpha value.

        Parameters:
        :   **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
            is completed. For example, alpha-values of 0, 0.5, and 1 correspond
            to the animation being completed 0%, 50%, and 100%, respectively.

        Return type:
        :   None
