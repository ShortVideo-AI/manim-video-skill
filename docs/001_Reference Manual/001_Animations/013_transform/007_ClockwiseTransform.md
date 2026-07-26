---
{
  "title": "ClockwiseTransform",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.ClockwiseTransform.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "ClockwiseTransform"
  ],
  "scraped_at": "2026-07-10T15:58:15"
}
---

# ClockwiseTransform

Qualified name: `manim.animation.transform.ClockwiseTransform`

class ClockwiseTransform(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html)

    Transforms the points of a mobject along a clockwise oriented arc.

    See also

    [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html), [`CounterclockwiseTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.CounterclockwiseTransform.html)

    Examples

    Example: ClockwiseExample

    [
    ](./ClockwiseExample-1.mp4)

    ```
    class ClockwiseExample(Scene):
        def construct(self):
            dl, dr = Dot(), Dot()
            sl, sr = Square(), Square()

            VGroup(dl, sl).arrange(DOWN).shift(2*LEFT)
            VGroup(dr, sr).arrange(DOWN).shift(2*RIGHT)

            self.add(dl, dr)
            self.wait()
            self.play(
                ClockwiseTransform(dl, sl),
                Transform(dr, sr)
            )
            self.wait()
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

    \_original\_\_init\_\_(*mobject*, *target\_mobject*, *path\_arc=-3.141592653589793*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **target\_mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **path\_arc** (*float*)

        Return type:
        :   None
