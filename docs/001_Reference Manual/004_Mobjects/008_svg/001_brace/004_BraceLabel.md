---
{
  "title": "BraceLabel",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceLabel.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "svg",
    "brace",
    "BraceLabel"
  ],
  "scraped_at": "2026-07-10T15:59:53"
}
---

# BraceLabel

Qualified name: `manim.mobject.svg.brace.BraceLabel`

class BraceLabel(*obj*, *text*, *brace\_direction=array([ 0.*, *-1.*, *0.])*, *label\_constructor=<class 'manim.mobject.text.tex\_mobject.MathTex'>*, *font\_size=48*, *buff=0.2*, *brace\_config=None*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/svg/brace.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    Create a brace with a label attached.

    Parameters:
    :   - **obj** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobject adjacent to which the brace is placed.
        - **text** (*str*) – The label text.
        - **brace\_direction** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The direction of the brace. By default `DOWN`.
        - **label\_constructor** (*type**[*[*SingleStringMathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html) *|* [*Text*](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html)*]*) – A class or function used to construct a mobject representing
          the label. By default [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html).
        - **font\_size** (*float*) – The font size of the label, passed to the `label_constructor`.
        - **buff** (*float*) – The buffer between the mobject and the brace.
        - **brace\_config** (*dict**[**str**,* *Any**]* *|* *None*) – Arguments to be passed to [`Brace`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.Brace.html).
        - **kwargs** (*Any*) – Additional arguments to be passed to [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html).

    Methods

    |  |  |
    | --- | --- |
    | `change_brace_label` |  |
    | `change_label` |  |
    | `creation_anim` |  |
    | `shift_brace` |  |

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

    \_original\_\_init\_\_(*obj*, *text*, *brace\_direction=array([ 0.*, *-1.*, *0.])*, *label\_constructor=<class 'manim.mobject.text.tex\_mobject.MathTex'>*, *font\_size=48*, *buff=0.2*, *brace\_config=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **obj** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **text** (*str*)
            - **brace\_direction** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **label\_constructor** (*type**[*[*SingleStringMathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html) *|* [*Text*](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html)*]*)
            - **font\_size** (*float*)
            - **buff** (*float*)
            - **brace\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            - **kwargs** (*Any*)
