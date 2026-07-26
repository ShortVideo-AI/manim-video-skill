---
{
  "title": "LabeledLine",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledLine.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "labeled",
    "LabeledLine"
  ],
  "scraped_at": "2026-07-10T15:58:56"
}
---

# LabeledLine

Qualified name: `manim.mobject.geometry.labeled.LabeledLine`

class LabeledLine(*label*, *label\_position=0.5*, *label\_config=None*, *box\_config=None*, *frame\_config=None*, *\*args*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/labeled.html)
:   Bases: [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html)

    Constructs a line containing a label box somewhere along its length.

    Parameters:
    :   - **label** (*str* *|* [*Tex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html) *|* [*MathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html) *|* [*Text*](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html)) – Label that will be displayed on the line.
        - **label\_position** (*float*) – A ratio in the range [0-1] to indicate the position of the label with respect to the length of the line. Default value is 0.5.
        - **label\_config** (*dict**[**str**,* *Any**]* *|* *None*) – A dictionary containing the configuration for the label.
          This is only applied if `label` is of type `str`.
        - **box\_config** (*dict**[**str**,* *Any**]* *|* *None*) – A dictionary containing the configuration for the background box.
        - **frame\_config** (*dict**[**str**,* *Any**]* *|* *None*) –

          A dictionary containing the configuration for the frame.

          See also

          [`LabeledArrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledArrow.html)
        - **args** (*Any*)
        - **kwargs** (*Any*)

    Examples

    Example: LabeledLineExample

    ![../_images/LabeledLineExample-1.png](https://docs.manim.community/en/stable/_images/LabeledLineExample-1.png)

    ```
    class LabeledLineExample(Scene):
        def construct(self):
            line = LabeledLine(
                label          = '0.5',
                label_position = 0.8,
                label_config = {
                    "font_size" : 20
                },
                start=LEFT+DOWN,
                end=RIGHT+UP)

            line.set_length(line.get_length() * 2)
            self.add(line)
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

    \_original\_\_init\_\_(*label*, *label\_position=0.5*, *label\_config=None*, *box\_config=None*, *frame\_config=None*, *\*args*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **label** (*str* *|* [*Tex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html) *|* [*MathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html) *|* [*Text*](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html))
            - **label\_position** (*float*)
            - **label\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            - **box\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            - **frame\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            - **args** (*Any*)
            - **kwargs** (*Any*)

        Return type:
        :   None
