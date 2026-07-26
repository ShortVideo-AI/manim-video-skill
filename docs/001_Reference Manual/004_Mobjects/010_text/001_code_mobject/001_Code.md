---
{
  "title": "Code",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "text",
    "code_mobject",
    "Code"
  ],
  "scraped_at": "2026-07-10T16:00:01"
}
---

# Code

Qualified name: `manim.mobject.text.code\_mobject.Code`

class Code(*code\_file=None*, *code\_string=None*, *language=None*, *formatter\_style='vim'*, *tab\_width=4*, *add\_line\_numbers=True*, *line\_numbers\_from=1*, *background='rectangle'*, *background\_config=None*, *paragraph\_config=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/code_mobject.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    A highlighted source code listing.

    Examples

    Normal usage:

    We can also render code passed as a string. As the automatic language
    detection can be a bit flaky, it is recommended to specify the language
    explicitly:

    Example: CodeFromString

    ![../_images/CodeFromString-1.png](https://docs.manim.community/en/stable/_images/CodeFromString-1.png)

    ```
    class CodeFromString(Scene):
        def construct(self):
            code = '''from manim import Scene, Square

    class FadeInSquare(Scene):
        def construct(self):
            s = Square()
            self.play(FadeIn(s))
            self.play(s.animate.scale(2))
            self.wait()'''

            rendered_code = Code(
                code_string=code,
                language="python",
                background="window",
                background_config={"stroke_color": "maroon"},
            )
            self.add(rendered_code)
    ```

    Parameters:
    :   - **code\_file** ([*StrPath*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* *None*) – The path to the code file to display.
        - **code\_string** (*str* *|* *None*) – Alternatively, the code string to display.
        - **language** (*str* *|* *None*) – The programming language of the code. If not specified, it will be
          guessed from the file extension or the code itself.
        - **formatter\_style** (*str*) – The style to use for the code highlighting. Defaults to `"vim"`.
          A list of all available styles can be obtained by calling
          [`Code.get_styles_list()`](#manim.mobject.text.code_mobject.Code.get_styles_list).
        - **tab\_width** (*int*) – The width of a tab character in spaces. Defaults to 4.
        - **add\_line\_numbers** (*bool*) – Whether to display line numbers. Defaults to `True`.
        - **line\_numbers\_from** (*int*) – The first line number to display. Defaults to 1.
        - **background** (*Literal**[**'rectangle'**,* *'window'**]*) – The type of background to use. Can be either `"rectangle"` (the
          default) or `"window"`.
        - **background\_config** (*dict**[**str**,* *Any**]* *|* *None*) – Keyword arguments passed to the background constructor. Default
          settings are stored in the class attribute
          `default_background_config` (which can also be modified
          directly).
        - **paragraph\_config** (*dict**[**str**,* *Any**]* *|* *None*) – Keyword arguments passed to the constructor of the
          [`Paragraph`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html) objects holding the code, and the line
          numbers. Default settings are stored in the class attribute
          `default_paragraph_config` (which can also be modified
          directly).

    Methods

    |  |  |
    | --- | --- |
    | [`get_styles_list`](#manim.mobject.text.code_mobject.Code.get_styles_list) | Get the list of all available formatter styles. |

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `default_background_config` |  |
    | `default_paragraph_config` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |
    | `code` |  |

    \_original\_\_init\_\_(*code\_file=None*, *code\_string=None*, *language=None*, *formatter\_style='vim'*, *tab\_width=4*, *add\_line\_numbers=True*, *line\_numbers\_from=1*, *background='rectangle'*, *background\_config=None*, *paragraph\_config=None*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **code\_file** (*TypeAliasForwardRef**(**'~manim.typing.StrPath'**)* *|* *None*)
            - **code\_string** (*str* *|* *None*)
            - **language** (*str* *|* *None*)
            - **formatter\_style** (*str*)
            - **tab\_width** (*int*)
            - **add\_line\_numbers** (*bool*)
            - **line\_numbers\_from** (*int*)
            - **background** (*Literal**[**'rectangle'**,* *'window'**]*)
            - **background\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            - **paragraph\_config** (*dict**[**str**,* *Any**]* *|* *None*)

    classmethod get\_styles\_list()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/code_mobject.html)
    :   Get the list of all available formatter styles.

        Return type:
        :   list[str]
