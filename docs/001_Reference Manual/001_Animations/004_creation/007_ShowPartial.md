---
{
  "title": "ShowPartial",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowPartial.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "creation",
    "ShowPartial"
  ],
  "scraped_at": "2026-07-10T15:57:43"
}
---

# ShowPartial

Qualified name: `manim.animation.creation.ShowPartial`

class ShowPartial(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
:   Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)

    Abstract class for Animations that show the VMobject partially.

    Raises:
    :   **TypeError** – If `mobject` is not an instance of [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html).

    Parameters:
    :   **mobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* *OpenGLVMobject* *|* *OpenGLSurface* *|* *None*)

    See also

    [`Create`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html), [`ShowPassingFlash`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html)

    Methods

    |  |  |
    | --- | --- |
    | `interpolate_submobject` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **mobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* *OpenGLVMobject* *|* *OpenGLSurface* *|* *None*)
