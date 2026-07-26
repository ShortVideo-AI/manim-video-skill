---
{
  "title": "TransformAnimations",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformAnimations.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "TransformAnimations"
  ],
  "scraped_at": "2026-07-10T15:58:22"
}
---

# TransformAnimations

Qualified name: `manim.animation.transform.TransformAnimations`

class TransformAnimations(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html)

    Methods

    |  |  |
    | --- | --- |
    | [`interpolate`](#manim.animation.transform.TransformAnimations.interpolate) | Set the animation progress. |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    Parameters:
    :   - **start\_anim** ([*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html))
        - **end\_anim** ([*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html))
        - **rate\_func** (*Callable*)

    \_original\_\_init\_\_(*start\_anim*, *end\_anim*, *rate\_func=<function squish\_rate\_func.<locals>.result>*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **start\_anim** ([*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html))
            - **end\_anim** ([*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html))
            - **rate\_func** (*Callable*)

        Return type:
        :   None

    interpolate(*alpha*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
    :   Set the animation progress.

        This method gets called for every frame during an animation.

        Parameters:
        :   **alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
            the end.

        Return type:
        :   None
