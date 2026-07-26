---
{
  "title": "debug",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.debug.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "debug"
  ],
  "scraped_at": "2026-07-10T16:01:24"
}
---

# debug

Debugging utilities.

Functions

index\_labels(*mobject*, *label\_height=0.15*, *background\_stroke\_width=5*, *background\_stroke\_color=ManimColor('#000000')*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/debug.html)
:   Returns a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) of [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html) mobjects
    that shows the index of each submobject.

    Useful for working with parts of complicated mobjects.

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobject that will have its submobjects labelled.
        - **label\_height** (*float*) – The height of the labels, by default 0.15.
        - **background\_stroke\_width** (*float*) – The stroke width of the outline of the labels, by default 5.
        - **background\_stroke\_color** ([*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)) – The stroke color of the outline of labels.
        - **kwargs** (*Any*) – Additional parameters to be passed into the :class`~.Integer`
          mobjects used to construct the labels.

    Return type:
    :   [*VGroup*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    Examples

    Example: IndexLabelsExample

    ![../_images/IndexLabelsExample-1.png](https://docs.manim.community/en/stable/_images/IndexLabelsExample-1.png)

    ```
    class IndexLabelsExample(Scene):
        def construct(self):
            text = MathTex(
                "\\frac{d}{dx}f(x)g(x)=",
                "f(x)\\frac{d}{dx}g(x)",
                "+",
                "g(x)\\frac{d}{dx}f(x)",
            )

            #index the fist term in the MathTex mob
            indices = index_labels(text[0])

            text[0][1].set_color(PURPLE_B)
            text[0][8:12].set_color(DARK_BLUE)

            self.add(text, indices)
    ```

print\_family(*mobject*, *n\_tabs=0*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/debug.html)
:   For debugging purposes

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
        - **n\_tabs** (*int*)

    Return type:
    :   None
