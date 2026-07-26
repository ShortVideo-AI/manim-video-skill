---
{
  "title": "CounterclockwiseTransform",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.CounterclockwiseTransform.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "CounterclockwiseTransform"
  ],
  "scraped_at": "2026-07-10T15:58:15"
}
---

# CounterclockwiseTransform

Qualified name: `manim.animation.transform.CounterclockwiseTransform`

class CounterclockwiseTransform(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html)

    Transforms the points of a mobject along a counterclockwise oriented arc.

    See also

    [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html), [`ClockwiseTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ClockwiseTransform.html)

    Examples

    Example: CounterclockwiseTransform\_vs\_Transform

    [
    ](./CounterclockwiseTransform_vs_Transform-1.mp4)

    ```
    class CounterclockwiseTransform_vs_Transform(Scene):
        def construct(self):
            # set up the numbers
            c_transform = VGroup(DecimalNumber(number=3.141, num_decimal_places=3), DecimalNumber(number=1.618, num_decimal_places=3))
            text_1 = Text("CounterclockwiseTransform", color=RED)
            c_transform.add(text_1)

            transform = VGroup(DecimalNumber(number=1.618, num_decimal_places=3), DecimalNumber(number=3.141, num_decimal_places=3))
            text_2 = Text("Transform", color=BLUE)
            transform.add(text_2)

            ints = VGroup(c_transform, transform)
            texts = VGroup(text_1, text_2).scale(0.75)
            c_transform.arrange(direction=UP, buff=1)
            transform.arrange(direction=UP, buff=1)

            ints.arrange(buff=2)
            self.add(ints, texts)

            # The mobs move in clockwise direction for ClockwiseTransform()
            self.play(CounterclockwiseTransform(c_transform[0], c_transform[1]))

            # The mobs move straight up for Transform()
            self.play(Transform(transform[0], transform[1]))
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
        - **target\_mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
        - **path\_arc** (*float*)

    \_original\_\_init\_\_(*mobject*, *target\_mobject*, *path\_arc=3.141592653589793*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **target\_mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **path\_arc** (*float*)

        Return type:
        :   None
