---
{
  "title": "UpdateFromAlphaFunc",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromAlphaFunc.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "updaters",
    "update",
    "UpdateFromAlphaFunc"
  ],
  "scraped_at": "2026-07-10T15:58:27"
}
---

# UpdateFromAlphaFunc

Qualified name: `manim.animation.updaters.update.UpdateFromAlphaFunc`

class UpdateFromAlphaFunc(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/updaters/update.html)
:   Bases: [`UpdateFromFunc`](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromFunc.html)

    Methods

    |  |  |
    | --- | --- |
    | [`interpolate_mobject`](#manim.animation.updaters.update.UpdateFromAlphaFunc.interpolate_mobject) | Interpolates the mobject of the `Animation` based on alpha value. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
        - **update\_function** (*Callable**[**[*[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]**,* *Any**]*)
        - **suspend\_mobject\_updating** (*bool*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*mobject*, *update\_function*, *suspend\_mobject\_updating=False*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **update\_function** (*Callable**[**[*[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]**,* *Any**]*)
            - **suspend\_mobject\_updating** (*bool*)
            - **kwargs** (*Any*)

        Return type:
        :   None

    interpolate\_mobject(*alpha*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/updaters/update.html)
    :   Interpolates the mobject of the `Animation` based on alpha value.

        Parameters:
        :   **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
            is completed. For example, alpha-values of 0, 0.5, and 1 correspond
            to the animation being completed 0%, 50%, and 100%, respectively.

        Return type:
        :   None
