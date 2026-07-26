---
{
  "title": "ChangingDecimal",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "numbers",
    "ChangingDecimal"
  ],
  "scraped_at": "2026-07-10T15:58:05"
}
---

# ChangingDecimal

Qualified name: `manim.animation.numbers.ChangingDecimal`

class ChangingDecimal(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/numbers.html)
:   Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)

    Animate a [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html) to values specified by a user-supplied function.

    Parameters:
    :   - **decimal\_mob** ([*DecimalNumber*](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html)) – The [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html) instance to animate.
        - **number\_update\_func** (*Callable**[**[**float**]**,* *float**]*) – A function that returns the number to display at each point in the animation.
        - **suspend\_mobject\_updating** (*bool*) – If `True`, the mobject is not updated outside this animation.
        - **kwargs** (*Any*)

    Raises:
    :   **TypeError** – If `decimal_mob` is not an instance of [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html).

    Examples

    Example: ChangingDecimalExample

    [
    ](./ChangingDecimalExample-1.mp4)

    ```
    class ChangingDecimalExample(Scene):
        def construct(self):
            number = DecimalNumber(0)
            self.add(number)
            self.play(
                ChangingDecimal(
                    number,
                    lambda a: 5 * a,
                    run_time=3
                )
            )
            self.wait()
    ```

    Methods

    |  |  |
    | --- | --- |
    | `check_validity_of_input` |  |
    | [`interpolate_mobject`](#manim.animation.numbers.ChangingDecimal.interpolate_mobject) | Interpolates the mobject of the `Animation` based on alpha value. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*decimal\_mob*, *number\_update\_func*, *suspend\_mobject\_updating=False*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **decimal\_mob** ([*DecimalNumber*](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html))
            - **number\_update\_func** (*Callable**[**[**float**]**,* *float**]*)
            - **suspend\_mobject\_updating** (*bool*)
            - **kwargs** (*Any*)

        Return type:
        :   None

    interpolate\_mobject(*alpha*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/numbers.html)
    :   Interpolates the mobject of the `Animation` based on alpha value.

        Parameters:
        :   **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
            is completed. For example, alpha-values of 0, 0.5, and 1 correspond
            to the animation being completed 0%, 50%, and 100%, respectively.

        Return type:
        :   None
