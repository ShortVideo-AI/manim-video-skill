---
{
  "title": "Label",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.Label.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "labeled",
    "Label"
  ],
  "scraped_at": "2026-07-10T15:58:55"
}
---

# Label

Qualified name: `manim.mobject.geometry.labeled.Label`

class Label(*label*, *label\_config=None*, *box\_config=None*, *frame\_config=None*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/labeled.html)
:   Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    A Label consisting of text surrounded by a frame.

    Parameters:
    :   - **label** (*str* *|* [*Tex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html) *|* [*MathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html) *|* [*Text*](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html)) – Label that will be displayed.
        - **label\_config** (*dict**[**str**,* *Any**]* *|* *None*) – A dictionary containing the configuration for the label.
          This is only applied if `label` is of type `str`.
        - **box\_config** (*dict**[**str**,* *Any**]* *|* *None*) – A dictionary containing the configuration for the background box.
        - **frame\_config** (*dict**[**str**,* *Any**]* *|* *None*) – A dictionary containing the configuration for the frame.
        - **kwargs** (*Any*)

    Examples

    Example: LabelExample

    ![../_images/LabelExample-1.png](https://docs.manim.community/en/stable/_images/LabelExample-1.png)

    ```
    class LabelExample(Scene):
        def construct(self):
            label = Label(
                label=Text('Label Text', font='sans-serif'),
                box_config = {
                    "color" : BLUE,
                    "fill_opacity" : 0.75
                }
            )
            label.scale(3)
            self.add(label)
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

    \_original\_\_init\_\_(*label*, *label\_config=None*, *box\_config=None*, *frame\_config=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **label** (*str* *|* [*Tex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html) *|* [*MathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html) *|* [*Text*](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html))
            - **label\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            - **box\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            - **frame\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            - **kwargs** (*Any*)

        Return type:
        :   None
