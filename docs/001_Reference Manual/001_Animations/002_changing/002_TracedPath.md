---
{
  "title": "TracedPath",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.changing.TracedPath.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "changing",
    "TracedPath"
  ],
  "scraped_at": "2026-07-10T15:57:36"
}
---

# TracedPath

Qualified name: `manim.animation.changing.TracedPath`

class TracedPath(*traced\_point\_func*, *stroke\_width=2*, *stroke\_color=ManimColor('#FFFFFF')*, *dissipating\_time=None*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/changing.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    Traces the path of a point returned by a function call.

    Parameters:
    :   - **traced\_point\_func** (*Callable*) – The function to be traced.
        - **stroke\_width** (*float*) – The width of the trace.
        - **stroke\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*) – The color of the trace.
        - **dissipating\_time** (*float* *|* *None*) – The time taken for the path to dissipate. Default set to `None`
          which disables dissipation.
        - **kwargs** (*Any*)

    Examples

    Example: TracedPathExample

    [
    ](./TracedPathExample-1.mp4)

    ```
    class TracedPathExample(Scene):
        def construct(self):
            circ = Circle(color=RED).shift(4*LEFT)
            dot = Dot(color=RED).move_to(circ.get_start())
            rolling_circle = VGroup(circ, dot)
            trace = TracedPath(circ.get_start)
            rolling_circle.add_updater(lambda m: m.rotate(-0.3))
            self.add(trace, rolling_circle)
            self.play(rolling_circle.animate.shift(8*RIGHT), run_time=4, rate_func=linear)
    ```

    Example: DissipatingPathExample

    [
    ](./DissipatingPathExample-1.mp4)

    ```
    class DissipatingPathExample(Scene):
        def construct(self):
            a = Dot(RIGHT * 2)
            b = TracedPath(a.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])
            self.add(a, b)
            self.play(a.animate(path_arc=PI / 4).shift(LEFT * 2))
            self.play(a.animate(path_arc=-PI / 4).shift(LEFT * 2))
            self.wait()
    ```

    Methods

    |  |  |
    | --- | --- |
    | `update_path` |  |

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

    \_original\_\_init\_\_(*traced\_point\_func*, *stroke\_width=2*, *stroke\_color=ManimColor('#FFFFFF')*, *dissipating\_time=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **traced\_point\_func** (*Callable*)
            - **stroke\_width** (*float*)
            - **stroke\_color** (*TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)* *|* *None*)
            - **dissipating\_time** (*float* *|* *None*)
            - **kwargs** (*Any*)

        Return type:
        :   None
