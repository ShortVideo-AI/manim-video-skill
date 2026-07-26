---
{
  "title": "SingleStringMathTex",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "text",
    "tex_mobject",
    "SingleStringMathTex"
  ],
  "scraped_at": "2026-07-10T16:00:06"
}
---

# SingleStringMathTex

Qualified name: `manim.mobject.text.tex\_mobject.SingleStringMathTex`

class SingleStringMathTex(*tex\_string*, *stroke\_width=0*, *should\_center=True*, *height=None*, *organize\_left\_to\_right=False*, *tex\_environment='align\*'*, *tex\_template=None*, *font\_size=48*, *color=None*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/tex_mobject.html)
:   Bases: [`SVGMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.svg_mobject.SVGMobject.html)

    Elementary building block for rendering text with LaTeX.

    Tests

    Check that creating a [`SingleStringMathTex`](#manim.mobject.text.tex_mobject.SingleStringMathTex) object works:

    ```
    >>> SingleStringMathTex('Test')
    SingleStringMathTex('Test')
    ```

    Methods

    |  |  |
    | --- | --- |
    | `get_tex_string` |  |
    | [`init_colors`](#manim.mobject.text.tex_mobject.SingleStringMathTex.init_colors) | Initializes the colors. |

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | [`font_size`](#manim.mobject.text.tex_mobject.SingleStringMathTex.font_size) | The font size of the tex mobject. |
    | `hash_seed` | A unique hash representing the result of the generated mobject points. |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    Parameters:
    :   - **tex\_string** (*str*)
        - **stroke\_width** (*float*)
        - **should\_center** (*bool*)
        - **height** (*float* *|* *None*)
        - **organize\_left\_to\_right** (*bool*)
        - **tex\_environment** (*str* *|* *None*)
        - **tex\_template** ([*TexTemplate*](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html) *|* *None*)
        - **font\_size** (*float*)
        - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*tex\_string*, *stroke\_width=0*, *should\_center=True*, *height=None*, *organize\_left\_to\_right=False*, *tex\_environment='align\*'*, *tex\_template=None*, *font\_size=48*, *color=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **tex\_string** (*str*)
            - **stroke\_width** (*float*)
            - **should\_center** (*bool*)
            - **height** (*float* *|* *None*)
            - **organize\_left\_to\_right** (*bool*)
            - **tex\_environment** (*str* *|* *None*)
            - **tex\_template** ([*TexTemplate*](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html) *|* *None*)
            - **font\_size** (*float*)
            - **color** (*TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)* *|* *None*)
            - **kwargs** (*Any*)

    \_remove\_stray\_braces(*tex*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/tex_mobject.html)
    :   Makes [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html) resilient to unmatched braces.

        This is important when the braces in the TeX code are spread over
        multiple arguments as in, e.g., `MathTex(r"e^{i", r"\tau} = 1")`.

        Parameters:
        :   **tex** (*str*)

        Return type:
        :   str

    property font\_size: float
    :   The font size of the tex mobject.

    init\_colors(*propagate\_colors=True*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/tex_mobject.html)
    :   Initializes the colors.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Parameters:
        :   **propagate\_colors** (*bool*)

        Return type:
        :   *Self*
