---
{
  "title": "TransformFromCopy",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformFromCopy.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "TransformFromCopy"
  ],
  "scraped_at": "2026-07-10T15:58:23"
}
---

# TransformFromCopy

Qualified name: `manim.animation.transform.TransformFromCopy`

class TransformFromCopy(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html)

    Preserves a copy of the original VMobject and transforms only it’s copy to the target VMobject

    Methods

    |  |  |
    | --- | --- |
    | [`interpolate`](#manim.animation.transform.TransformFromCopy.interpolate) | Set the animation progress. |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
        - **target\_mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))

    \_original\_\_init\_\_(*mobject*, *target\_mobject*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **target\_mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))

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
