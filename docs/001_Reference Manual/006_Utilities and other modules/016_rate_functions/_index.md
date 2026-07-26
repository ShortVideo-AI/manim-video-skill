---
{
  "title": "rate_functions",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "rate_functions"
  ],
  "scraped_at": "2026-07-10T16:01:38"
}
---

# rate\_functions

A selection of rate functions, i.e., *speed curves* for animations.
Please find a standard list at <https://easings.net/>. Here is a picture
for the non-standard ones

Example: RateFuncExample

![../_images/RateFuncExample-1.png](https://docs.manim.community/en/stable/_images/RateFuncExample-1.png)

```
class RateFuncExample(Scene):
    def construct(self):
        x = VGroup()
        for k, v in rate_functions.__dict__.items():
            if "function" in str(v):
                if (
                    not k.startswith("__")
                    and not k.startswith("sqrt")
                    and not k.startswith("bezier")
                ):
                    try:
                        rate_func = v
                        plot = (
                            ParametricFunction(
                                lambda x: [x, rate_func(x), 0],
                                t_range=[0, 1, .01],
                                use_smoothing=False,
                                color=YELLOW,
                            )
                            .stretch_to_fit_width(1.5)
                            .stretch_to_fit_height(1)
                        )
                        plot_bg = SurroundingRectangle(plot).set_color(WHITE)
                        plot_title = (
                            Text(rate_func.__name__, weight=BOLD)
                            .scale(0.5)
                            .next_to(plot_bg, UP, buff=0.1)
                        )
                        x.add(VGroup(plot_bg, plot, plot_title))
                    except: # because functions `not_quite_there`, `function squish_rate_func` are not working.
                        pass
        x.arrange_in_grid(cols=8)
        x.height = config.frame_height
        x.width = config.frame_width
        x.move_to(ORIGIN).scale(0.95)
        self.add(x)
```

There are primarily 3 kinds of standard easing functions:

1. Ease In - The animation has a smooth start.
2. Ease Out - The animation has a smooth end.
3. Ease In Out - The animation has a smooth start as well as smooth end.

Note

The standard functions are not exported, so to use them you do something like this:
rate\_func=rate\_functions.ease\_in\_sine
On the other hand, the non-standard functions, which are used more commonly, are exported and can be used directly.

Example: RateFunctions1Example

[
](./RateFunctions1Example-1.mp4)

```
class RateFunctions1Example(Scene):
    def construct(self):
        line1 = Line(3*LEFT, 3*RIGHT).shift(UP).set_color(RED)
        line2 = Line(3*LEFT, 3*RIGHT).set_color(GREEN)
        line3 = Line(3*LEFT, 3*RIGHT).shift(DOWN).set_color(BLUE)

        dot1 = Dot().move_to(line1.get_left())
        dot2 = Dot().move_to(line2.get_left())
        dot3 = Dot().move_to(line3.get_left())

        label1 = Tex("Ease In").next_to(line1, RIGHT)
        label2 = Tex("Ease out").next_to(line2, RIGHT)
        label3 = Tex("Ease In Out").next_to(line3, RIGHT)

        self.play(
            FadeIn(VGroup(line1, line2, line3)),
            FadeIn(VGroup(dot1, dot2, dot3)),
            Write(VGroup(label1, label2, label3)),
        )
        self.play(
            MoveAlongPath(dot1, line1, rate_func=rate_functions.ease_in_sine),
            MoveAlongPath(dot2, line2, rate_func=rate_functions.ease_out_sine),
            MoveAlongPath(dot3, line3, rate_func=rate_functions.ease_in_out_sine),
            run_time=7
        )
        self.wait()
```

Classes

| Name | Description |
| --- | --- |
| [`RateFunction`](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html) |  |

Functions

double\_smooth(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_back(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_bounce(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_circ(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_cubic(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_elastic(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_expo(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_back(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_bounce(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_circ(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_cubic(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_elastic(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_expo(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_quad(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_quart(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_quint(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_sine(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_quad(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_quart(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_quint(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_sine(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_back(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_bounce(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_circ(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_cubic(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_elastic(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_expo(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_quad(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_quart(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_quint(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_sine(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

exponential\_decay(*t*, *half\_life=0.1*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   - **t** (*float*)
        - **half\_life** (*float*)

    Return type:
    :   float

linear(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

lingering(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

not\_quite\_there(*func=<function smooth>*, *proportion=0.7*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   - **func** ([*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html))
        - **proportion** (*float*)

    Return type:
    :   [*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html)

running\_start(*t*, *pull\_factor=-0.5*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   - **t** (*float*)
        - **pull\_factor** (*float*)

    Return type:
    :   float

rush\_from(*t*, *inflection=10.0*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   - **t** (*float*)
        - **inflection** (*float*)

    Return type:
    :   float

rush\_into(*t*, *inflection=10.0*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   - **t** (*float*)
        - **inflection** (*float*)

    Return type:
    :   float

slow\_into(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

smooth(*t*, *inflection=10.0*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   - **t** (*float*)
        - **inflection** (*float*)

    Return type:
    :   float

smoothererstep(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Implementation of the 3rd order SmoothStep sigmoid function.
    The 1st, 2nd and 3rd derivatives (speed, acceleration and jerk) are zero at the endpoints.
    <https://en.wikipedia.org/wiki/Smoothstep>

    Parameters:
    :   **t** (*float*)

    Return type:
    :   float

smootherstep(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Implementation of the 2nd order SmoothStep sigmoid function.
    The 1st and 2nd derivatives (speed and acceleration) are zero at the endpoints.
    <https://en.wikipedia.org/wiki/Smoothstep>

    Parameters:
    :   **t** (*float*)

    Return type:
    :   float

smoothstep(*t*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Implementation of the 1st order SmoothStep sigmoid function.
    The 1st derivative (speed) is zero at the endpoints.
    <https://en.wikipedia.org/wiki/Smoothstep>

    Parameters:
    :   **t** (*float*)

    Return type:
    :   float

squish\_rate\_func(*func*, *a=0.4*, *b=0.6*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   - **func** ([*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html))
        - **a** (*float*)
        - **b** (*float*)

    Return type:
    :   [*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html)

there\_and\_back(*t*, *inflection=10.0*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   - **t** (*float*)
        - **inflection** (*float*)

    Return type:
    :   float

there\_and\_back\_with\_pause(*t*, *pause\_ratio=0.3333333333333333*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   - **t** (*float*)
        - **pause\_ratio** (*float*)

    Return type:
    :   float

unit\_interval(*function*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **function** ([*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html))

    Return type:
    :   [*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html)

wiggle(*t*, *wiggles=2*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   - **t** (*float*)
        - **wiggles** (*float*)

    Return type:
    :   float

zero(*function*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/rate_functions.html)
:   Parameters:
    :   **function** ([*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html))

    Return type:
    :   [*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html)
