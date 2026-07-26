---
{
  "title": "Uncreate",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.creation.Uncreate.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "creation",
    "Uncreate"
  ],
  "scraped_at": "2026-07-10T15:57:46"
}
---

# Uncreate

Qualified name: `manim.animation.creation.Uncreate`

class Uncreate(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
:   Bases: [`Create`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html)

    Like [`Create`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html) but in reverse.

    Examples

    Example: ShowUncreate

    [
    ](./ShowUncreate-1.mp4)

    ```
    class ShowUncreate(Scene):
        def construct(self):
            self.play(Uncreate(Square()))
    ```

    See also

    [`Create`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html)

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   - **mobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* *OpenGLVMobject*)
        - **reverse\_rate\_function** (*bool*)
        - **remover** (*bool*)

    \_original\_\_init\_\_(*mobject*, *reverse\_rate\_function=True*, *remover=True*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* *OpenGLVMobject*)
            - **reverse\_rate\_function** (*bool*)
            - **remover** (*bool*)

        Return type:
        :   None
