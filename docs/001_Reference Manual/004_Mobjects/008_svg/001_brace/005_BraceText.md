---
{
  "title": "BraceText",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceText.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "svg",
    "brace",
    "BraceText"
  ],
  "scraped_at": "2026-07-10T15:59:54"
}
---

# BraceText

Qualified name: `manim.mobject.svg.brace.BraceText`

class BraceText(*obj*, *text*, *label\_constructor=<class 'manim.mobject.text.text\_mobject.Text'>*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/svg/brace.html)
:   Bases: [`BraceLabel`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceLabel.html)

    Create a brace with a text label attached.

    Parameters:
    :   - **obj** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobject adjacent to which the brace is placed.
        - **text** (*str*) – The label text.
        - **brace\_direction** – The direction of the brace. By default `DOWN`.
        - **label\_constructor** (*type**[*[*SingleStringMathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html) *|* [*Text*](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html)*]*) – A class or function used to construct a mobject representing
          the label. By default [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html).
        - **font\_size** – The font size of the label, passed to the `label_constructor`.
        - **buff** – The buffer between the mobject and the brace.
        - **brace\_config** – Arguments to be passed to [`Brace`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.Brace.html).
        - **kwargs** (*Any*) – Additional arguments to be passed to [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html).

    Examples

    Example: BraceTextExample

    ![../_images/BraceTextExample-1.png](https://docs.manim.community/en/stable/_images/BraceTextExample-1.png)

    ```
    class BraceTextExample(Scene):
        def construct(self):
            s1 = Square().move_to(2*LEFT)
            self.add(s1)
            br1 = BraceText(s1, "Label")
            self.add(br1)

            s2 = Square().move_to(2*RIGHT)
            self.add(s2)
            br2 = BraceText(s2, "Label")

            br2.change_label("new")
            self.add(br2)
            self.wait(0.1)
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*obj*, *text*, *label\_constructor=<class 'manim.mobject.text.text\_mobject.Text'>*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **obj** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **text** (*str*)
            - **label\_constructor** (*type**[*[*SingleStringMathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html) *|* [*Text*](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html)*]*)
            - **kwargs** (*Any*)
