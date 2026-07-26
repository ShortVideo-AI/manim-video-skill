---
{
  "title": "ApplyPointwiseFunctionToCenter",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunctionToCenter.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "ApplyPointwiseFunctionToCenter"
  ],
  "scraped_at": "2026-07-10T15:58:14"
}
---

# ApplyPointwiseFunctionToCenter

Qualified name: `manim.animation.transform.ApplyPointwiseFunctionToCenter`

class ApplyPointwiseFunctionToCenter(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`ApplyPointwiseFunction`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html)

    Methods

    |  |  |
    | --- | --- |
    | [`begin`](#manim.animation.transform.ApplyPointwiseFunctionToCenter.begin) | Begin the animation. |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    Parameters:
    :   - **function** (*types.MethodType*)
        - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))

    \_original\_\_init\_\_(*function*, *mobject*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **function** (*MethodType*)
            - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))

        Return type:
        :   None

    begin()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
    :   Begin the animation.

        This method is called right as an animation is being played. As much
        initialization as possible, especially any mobject copying, should live in this
        method.

        Return type:
        :   None
