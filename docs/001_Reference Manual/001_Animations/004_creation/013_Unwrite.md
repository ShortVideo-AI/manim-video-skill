---
{
  "title": "Unwrite",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.creation.Unwrite.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "creation",
    "Unwrite"
  ],
  "scraped_at": "2026-07-10T15:57:47"
}
---

# Unwrite

Qualified name: `manim.animation.creation.Unwrite`

class Unwrite(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
:   Bases: [`Write`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Write.html)

    Simulate erasing by hand a [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html) or a [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html).

    Parameters:
    :   - **reverse** (*bool*) – Set True to have the animation start erasing from the last submobject first.
        - **vmobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))
        - **rate\_func** (*Callable**[**[**float**]**,* *float**]*)

    Examples

    Example: UnwriteReverseTrue

    [
    ](./UnwriteReverseTrue-1.mp4)

    ```
    class UnwriteReverseTrue(Scene):
        def construct(self):
            text = Tex("Alice and Bob").scale(3)
            self.add(text)
            self.play(Unwrite(text))
    ```

    Example: UnwriteReverseFalse

    [
    ](./UnwriteReverseFalse-1.mp4)

    ```
    class UnwriteReverseFalse(Scene):
        def construct(self):
            text = Tex("Alice and Bob").scale(3)
            self.add(text)
            self.play(Unwrite(text, reverse=False))
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*vmobject*, *rate\_func=<function linear>*, *reverse=True*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **vmobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))
            - **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
            - **reverse** (*bool*)

        Return type:
        :   None
