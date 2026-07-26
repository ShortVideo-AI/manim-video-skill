---
{
  "title": "UntypeWithCursor",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.creation.UntypeWithCursor.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "creation",
    "UntypeWithCursor"
  ],
  "scraped_at": "2026-07-10T15:57:47"
}
---

# UntypeWithCursor

Qualified name: `manim.animation.creation.UntypeWithCursor`

class UntypeWithCursor(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
:   Bases: [`TypeWithCursor`](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html)

    Similar to [`RemoveTextLetterByLetter`](https://docs.manim.community/en/stable/reference/manim.animation.creation.RemoveTextLetterByLetter.html) , but with an additional cursor mobject at the end.

    Parameters:
    :   - **time\_per\_char** (*float*) – Frequency of appearance of the letters.
        - **cursor** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* *None*) – [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) shown after the last added letter.
        - **buff** – Controls how far away the cursor is to the right of the last added letter.
        - **keep\_cursor\_y** – If `True`, the cursor’s y-coordinate is set to the center of the `Text` and remains the same throughout the animation. Otherwise, it is set to the center of the last added letter.
        - **leave\_cursor\_on** – Whether to show the cursor after the animation.
        - **tip::** (*..*) – This is currently only possible for class:~.Text and not for class:~.MathTex.
        - **text** ([*Text*](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html))

    Examples

    Example: DeletingTextExample

    [
    ](./DeletingTextExample-1.mp4)

    ```
    class DeletingTextExample(Scene):
        def construct(self):
            text = Text("Deleting", color=PURPLE).scale(1.5).to_edge(LEFT)
            cursor = Rectangle(
                color = GREY_A,
                fill_color = GREY_A,
                fill_opacity = 1.0,
                height = 1.1,
                width = 0.5,
            ).move_to(text[0]) # Position the cursor

            self.play(UntypeWithCursor(text, cursor))
            self.play(Blink(cursor, blinks=2))
    ```

    References: [`Blink`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html)

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*text*, *cursor=None*, *time\_per\_char=0.1*, *reverse\_rate\_function=True*, *introducer=False*, *remover=True*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **text** ([*Text*](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html))
            - **cursor** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* *None*)
            - **time\_per\_char** (*float*)

        Return type:
        :   None
