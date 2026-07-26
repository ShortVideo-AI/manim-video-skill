---
{
  "title": "Create",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "creation",
    "Create"
  ],
  "scraped_at": "2026-07-10T15:57:41"
}
---

# Create

Qualified name: `manim.animation.creation.Create`

class Create(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
:   Bases: [`ShowPartial`](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowPartial.html)

    Incrementally show a VMobject.

    Parameters:
    :   - **mobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* *OpenGLVMobject* *|* *OpenGLSurface*) – The VMobject to animate.
        - **lag\_ratio** (*float*)
        - **introducer** (*bool*)

    Raises:
    :   **TypeError** – If `mobject` is not an instance of [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html).

    Examples

    Example: CreateScene

    [
    ](./CreateScene-1.mp4)

    ```
    class CreateScene(Scene):
        def construct(self):
            self.play(Create(Square()))
    ```

    See also

    [`ShowPassingFlash`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html)

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *lag\_ratio=1.0*, *introducer=True*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* *OpenGLVMobject* *|* *OpenGLSurface*)
            - **lag\_ratio** (*float*)
            - **introducer** (*bool*)

        Return type:
        :   None
