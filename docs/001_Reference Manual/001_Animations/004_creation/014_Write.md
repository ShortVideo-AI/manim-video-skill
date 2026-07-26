---
{
  "title": "Write",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.creation.Write.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "creation",
    "Write"
  ],
  "scraped_at": "2026-07-10T15:57:48"
}
---

# Write

Qualified name: `manim.animation.creation.Write`

class Write(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
:   Bases: [`DrawBorderThenFill`](https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html)

    Simulate hand-writing a [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html) or hand-drawing a [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html).

    Examples

    Example: ShowWrite

    [
    ](./ShowWrite-1.mp4)

    ```
    class ShowWrite(Scene):
        def construct(self):
            self.play(Write(Text("Hello", font_size=144)))
    ```

    Example: ShowWriteReversed

    [
    ](./ShowWriteReversed-1.mp4)

    ```
    class ShowWriteReversed(Scene):
        def construct(self):
            self.play(Write(Text("Hello", font_size=144), reverse=True, remover=False))
    ```

    Tests

    Check that creating empty [`Write`](#manim.animation.creation.Write) animations works:

    ```
    >>> from manim import Write, Text
    >>> Write(Text(''))
    Write(Text(''))
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`begin`](#manim.animation.creation.Write.begin) | Begin the animation. |
    | [`finish`](#manim.animation.creation.Write.finish) | Finish the animation. |
    | `reverse_submobjects` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   - **vmobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* *OpenGLVMobject*)
        - **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
        - **reverse** (*bool*)

    \_original\_\_init\_\_(*vmobject*, *rate\_func=<function linear>*, *reverse=False*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **vmobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* *OpenGLVMobject*)
            - **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
            - **reverse** (*bool*)

        Return type:
        :   None

    begin()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
    :   Begin the animation.

        This method is called right as an animation is being played. As much
        initialization as possible, especially any mobject copying, should live in this
        method.

        Return type:
        :   None

    finish()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
    :   Finish the animation.

        This method gets called when the animation is over.

        Return type:
        :   None
