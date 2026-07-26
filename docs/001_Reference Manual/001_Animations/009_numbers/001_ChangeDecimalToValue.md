---
{
  "title": "ChangeDecimalToValue",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangeDecimalToValue.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "numbers",
    "ChangeDecimalToValue"
  ],
  "scraped_at": "2026-07-10T15:58:04"
}
---

# ChangeDecimalToValue

Qualified name: `manim.animation.numbers.ChangeDecimalToValue`

class ChangeDecimalToValue(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/numbers.html)
:   Bases: [`ChangingDecimal`](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html)

    Animate a [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html) to a target value using linear interpolation.

    Parameters:
    :   - **decimal\_mob** ([*DecimalNumber*](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html)) – The [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html) instance to animate.
        - **target\_number** (*int*) – The target value to transition to.
        - **kwargs** (*Any*)

    Examples

    Example: ChangeDecimalToValueExample

    [
    ](./ChangeDecimalToValueExample-1.mp4)

    ```
    class ChangeDecimalToValueExample(Scene):
        def construct(self):
            number = DecimalNumber(0)
            self.add(number)
            self.play(ChangeDecimalToValue(number, 10, run_time=3))
            self.wait()
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*decimal\_mob*, *target\_number*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **decimal\_mob** ([*DecimalNumber*](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html))
            - **target\_number** (*int*)
            - **kwargs** (*Any*)

        Return type:
        :   None
