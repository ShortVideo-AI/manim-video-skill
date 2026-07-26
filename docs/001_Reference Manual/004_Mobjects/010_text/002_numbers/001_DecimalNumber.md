---
{
  "title": "DecimalNumber",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "text",
    "numbers",
    "DecimalNumber"
  ],
  "scraped_at": "2026-07-10T16:00:02"
}
---

# DecimalNumber

Qualified name: `manim.mobject.text.numbers.DecimalNumber`

class DecimalNumber(*number=0*, *num\_decimal\_places=2*, *mob\_class=<class 'manim.mobject.text.tex\_mobject.MathTex'>*, *include\_sign=False*, *group\_with\_commas=True*, *digit\_buff\_per\_font\_unit=0.001*, *show\_ellipsis=False*, *unit=None*, *unit\_buff\_per\_font\_unit=0*, *include\_background\_rectangle=False*, *edge\_to\_fix=array([-1.*, *0.*, *0.])*, *font\_size=48*, *stroke\_width=0*, *fill\_opacity=1.0*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/numbers.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    An mobject representing a decimal number.

    Parameters:
    :   - **number** (*float*) – The numeric value to be displayed. It can later be modified using [`set_value()`](#manim.mobject.text.numbers.DecimalNumber.set_value).
        - **num\_decimal\_places** (*int*) – The number of decimal places after the decimal separator. Values are automatically rounded.
        - **mob\_class** (*type**[*[*SingleStringMathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html)*]*) – The class for rendering digits and units, by default [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html).
        - **include\_sign** (*bool*) – Set to `True` to include a sign for positive numbers and zero.
        - **group\_with\_commas** (*bool*) – When `True` thousands groups are separated by commas for readability.
        - **digit\_buff\_per\_font\_unit** (*float*) – Additional spacing between digits. Scales with font size.
        - **show\_ellipsis** (*bool*) – When a number has been truncated by rounding, indicate with an ellipsis (`...`).
        - **unit** (*str* *|* *None*) – A unit string which can be placed to the right of the numerical values.
        - **unit\_buff\_per\_font\_unit** (*float*) – An additional spacing between the numerical values and the unit. A value
          of `unit_buff_per_font_unit=0.003` gives a decent spacing. Scales with font size.
        - **include\_background\_rectangle** (*bool*) – Adds a background rectangle to increase contrast on busy scenes.
        - **edge\_to\_fix** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – Assuring right- or left-alignment of the full object.
        - **font\_size** (*float*) – Size of the font.
        - **stroke\_width** (*float*)
        - **fill\_opacity** (*float*)
        - **kwargs** (*Any*)

    Examples

    Example: MovingSquareWithUpdaters

    [
    ](./MovingSquareWithUpdaters-1.mp4)

    ```
    class MovingSquareWithUpdaters(Scene):
        def construct(self):
            decimal = DecimalNumber(
                0,
                show_ellipsis=True,
                num_decimal_places=3,
                include_sign=True,
                unit=r"\text{M-Units}",
                unit_buff_per_font_unit=0.003
            )
            square = Square().to_edge(UP)

            decimal.add_updater(lambda d: d.next_to(square, RIGHT))
            decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
            self.add(square, decimal)
            self.play(
                square.animate.to_edge(DOWN),
                rate_func=there_and_back,
                run_time=5,
            )
            self.wait()
    ```

    Methods

    |  |  |
    | --- | --- |
    | `get_value` |  |
    | `increment_value` |  |
    | [`set_value`](#manim.mobject.text.numbers.DecimalNumber.set_value) | Set the value of the [`DecimalNumber`](#manim.mobject.text.numbers.DecimalNumber) to a new number. |

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | [`font_size`](#manim.mobject.text.numbers.DecimalNumber.font_size) | The font size of the tex mobject. |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    \_get\_formatter(*\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/numbers.html)
    :   Configuration is based first off instance attributes,
        but overwritten by any kew word argument. Relevant
        key words:
        - include\_sign
        - group\_with\_commas
        - num\_decimal\_places
        - field\_name (e.g. 0 or 0.real)

        Parameters:
        :   **kwargs** (*Any*)

        Return type:
        :   str

    \_original\_\_init\_\_(*number=0*, *num\_decimal\_places=2*, *mob\_class=<class 'manim.mobject.text.tex\_mobject.MathTex'>*, *include\_sign=False*, *group\_with\_commas=True*, *digit\_buff\_per\_font\_unit=0.001*, *show\_ellipsis=False*, *unit=None*, *unit\_buff\_per\_font\_unit=0*, *include\_background\_rectangle=False*, *edge\_to\_fix=array([-1.*, *0.*, *0.])*, *font\_size=48*, *stroke\_width=0*, *fill\_opacity=1.0*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **number** (*float*)
            - **num\_decimal\_places** (*int*)
            - **mob\_class** (*type**[*[*SingleStringMathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html)*]*)
            - **include\_sign** (*bool*)
            - **group\_with\_commas** (*bool*)
            - **digit\_buff\_per\_font\_unit** (*float*)
            - **show\_ellipsis** (*bool*)
            - **unit** (*str* *|* *None*)
            - **unit\_buff\_per\_font\_unit** (*float*)
            - **include\_background\_rectangle** (*bool*)
            - **edge\_to\_fix** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **font\_size** (*float*)
            - **stroke\_width** (*float*)
            - **fill\_opacity** (*float*)
            - **kwargs** (*Any*)

    property font\_size: float
    :   The font size of the tex mobject.

    set\_value(*number*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/numbers.html)
    :   Set the value of the [`DecimalNumber`](#manim.mobject.text.numbers.DecimalNumber) to a new number.

        Parameters:
        :   **number** (*float*) – The value that will overwrite the current number of the [`DecimalNumber`](#manim.mobject.text.numbers.DecimalNumber).

        Return type:
        :   *Self*
