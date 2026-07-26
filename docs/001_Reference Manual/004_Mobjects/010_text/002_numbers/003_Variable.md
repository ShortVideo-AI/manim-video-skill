---
{
  "title": "Variable",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Variable.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "text",
    "numbers",
    "Variable"
  ],
  "scraped_at": "2026-07-10T16:00:03"
}
---

# Variable

Qualified name: `manim.mobject.text.numbers.Variable`

class Variable(*var*, *label*, *var\_type=<class 'manim.mobject.text.numbers.DecimalNumber'>*, *num\_decimal\_places=2*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/numbers.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    A class for displaying text that shows “label = value” with
    the value continuously updated from a [`ValueTracker`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html).

    Parameters:
    :   - **var** (*float*) – The initial value you need to keep track of and display.
        - **label** (*str* *|* [*Tex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html) *|* [*MathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html) *|* [*Text*](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html) *|* [*SingleStringMathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html)) – The label for your variable. Raw strings are convertex to [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html) objects.
        - **var\_type** (*type**[*[*DecimalNumber*](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html) *|* [*Integer*](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html)*]*) – The class used for displaying the number. Defaults to [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html).
        - **num\_decimal\_places** (*int*) – The number of decimal places to display in your variable. Defaults to 2.
          If var\_type is an [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html), this parameter is ignored.
        - **kwargs** (*Any*) – Other arguments to be passed to ~.Mobject.

    label
    :   The label for your variable, for example `x = ...`.

        Type:
        :   Union[`str`, [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html), [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html), [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html), [`SingleStringMathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html)]

    tracker
    :   Useful in updating the value of your variable on-screen.

        Type:
        :   [`ValueTracker`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html)

    value
    :   The tex for the value of your variable.

        Type:
        :   Union[[`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html), [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html)]

    Examples

    Normal usage:

    Example: VariablesWithValueTracker

    [
    ](./VariablesWithValueTracker-1.mp4)

    ```
    class VariablesWithValueTracker(Scene):
        def construct(self):
            var = 0.5
            on_screen_var = Variable(var, Text("var"), num_decimal_places=3)

            # You can also change the colours for the label and value
            on_screen_var.label.set_color(RED)
            on_screen_var.value.set_color(GREEN)

            self.play(Write(on_screen_var))
            # The above line will just display the variable with
            # its initial value on the screen. If you also wish to
            # update it, you can do so by accessing the `tracker` attribute
            self.wait()
            var_tracker = on_screen_var.tracker
            var = 10.5
            self.play(var_tracker.animate.set_value(var))
            self.wait()

            int_var = 0
            on_screen_int_var = Variable(
                int_var, Text("int_var"), var_type=Integer
            ).next_to(on_screen_var, DOWN)
            on_screen_int_var.label.set_color(RED)
            on_screen_int_var.value.set_color(GREEN)

            self.play(Write(on_screen_int_var))
            self.wait()
            var_tracker = on_screen_int_var.tracker
            var = 10.5
            self.play(var_tracker.animate.set_value(var))
            self.wait()

            # If you wish to have a somewhat more complicated label for your
            # variable with subscripts, superscripts, etc. the default class
            # for the label is MathTex
            subscript_label_var = 10
            on_screen_subscript_var = Variable(subscript_label_var, "{a}_{i}").next_to(
                on_screen_int_var, DOWN
            )
            self.play(Write(on_screen_subscript_var))
            self.wait()
    ```

    Example: VariableExample

    [
    ](./VariableExample-1.mp4)

    ```
    class VariableExample(Scene):
        def construct(self):
            start = 2.0

            x_var = Variable(start, 'x', num_decimal_places=3)
            sqr_var = Variable(start**2, 'x^2', num_decimal_places=3)
            Group(x_var, sqr_var).arrange(DOWN)

            sqr_var.add_updater(lambda v: v.tracker.set_value(x_var.tracker.get_value()**2))

            self.add(x_var, sqr_var)
            self.play(x_var.tracker.animate.set_value(5), run_time=2, rate_func=linear)
            self.wait(0.1)
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

    \_original\_\_init\_\_(*var*, *label*, *var\_type=<class 'manim.mobject.text.numbers.DecimalNumber'>*, *num\_decimal\_places=2*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **var** (*float*)
            - **label** (*str* *|* [*Tex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html) *|* [*MathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html) *|* [*Text*](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html) *|* [*SingleStringMathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html))
            - **var\_type** (*type**[*[*DecimalNumber*](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html) *|* [*Integer*](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html)*]*)
            - **num\_decimal\_places** (*int*)
            - **kwargs** (*Any*)
