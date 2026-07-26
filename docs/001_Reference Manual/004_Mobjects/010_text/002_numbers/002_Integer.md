---
{
  "title": "Integer",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "text",
    "numbers",
    "Integer"
  ],
  "scraped_at": "2026-07-10T16:00:02"
}
---

# Integer

Qualified name: `manim.mobject.text.numbers.Integer`

class Integer(*number=0*, *num\_decimal\_places=0*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/numbers.html)
:   Bases: [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html)

    A class for displaying Integers.

    Examples

    Example: IntegerExample

    ![../_images/IntegerExample-1.png](https://docs.manim.community/en/stable/_images/IntegerExample-1.png)

    ```
    class IntegerExample(Scene):
        def construct(self):
            self.add(Integer(number=2.5).set_color(ORANGE).scale(2.5).set_x(-0.5).set_y(0.8))
            self.add(Integer(number=3.14159, show_ellipsis=True).set_x(3).set_y(3.3).scale(3.14159))
            self.add(Integer(number=42).set_x(2.5).set_y(-2.3).set_color_by_gradient(BLUE, TEAL).scale(1.7))
            self.add(Integer(number=6.28).set_x(-1.5).set_y(-2).set_color(YELLOW).scale(1.4))
    ```

    Methods

    |  |  |
    | --- | --- |
    | `get_value` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `font_size` | The font size of the tex mobject. |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    Parameters:
    :   - **number** (*float*)
        - **num\_decimal\_places** (*int*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*number=0*, *num\_decimal\_places=0*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **number** (*float*)
            - **num\_decimal\_places** (*int*)
            - **kwargs** (*Any*)

        Return type:
        :   None
