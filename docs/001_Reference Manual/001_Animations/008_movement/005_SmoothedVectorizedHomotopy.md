---
{
  "title": "SmoothedVectorizedHomotopy",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.movement.SmoothedVectorizedHomotopy.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "movement",
    "SmoothedVectorizedHomotopy"
  ],
  "scraped_at": "2026-07-10T15:58:03"
}
---

# SmoothedVectorizedHomotopy

Qualified name: `manim.animation.movement.SmoothedVectorizedHomotopy`

class SmoothedVectorizedHomotopy(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/movement.html)
:   Bases: [`Homotopy`](https://docs.manim.community/en/stable/reference/manim.animation.movement.Homotopy.html)

    Methods

    |  |  |
    | --- | --- |
    | `interpolate_submobject` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   - **homotopy** (*Callable**[**[**float**,* *float**,* *float**,* *float**]**,* *tuple**[**float**,* *float**,* *float**]**]*)
        - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
        - **run\_time** (*float*)
        - **apply\_function\_kwargs** (*dict**[**str**,* *Any**]* *|* *None*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*homotopy*, *mobject*, *run\_time=3*, *apply\_function\_kwargs=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **homotopy** (*Callable**[**[**float**,* *float**,* *float**,* *float**]**,* *tuple**[**float**,* *float**,* *float**]**]*)
            - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **run\_time** (*float*)
            - **apply\_function\_kwargs** (*dict**[**str**,* *Any**]* *|* *None*)
            - **kwargs** (*Any*)
