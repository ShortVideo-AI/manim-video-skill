---
{
  "title": "RightAngle",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.RightAngle.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "line",
    "RightAngle"
  ],
  "scraped_at": "2026-07-10T15:59:02"
}
---

# RightAngle

Qualified name: `manim.mobject.geometry.line.RightAngle`

class RightAngle(*line1*, *line2*, *length=None*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
:   Bases: [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html)

    An elbow-type mobject representing a right angle between two lines.

    Parameters:
    :   - **line1** ([*Line*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html)) – The first line.
        - **line2** ([*Line*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html)) – The second line.
        - **length** (*float* *|* *None*) – The length of the arms.
        - **\*\*kwargs** (*Any*) – Further keyword arguments that are passed to the constructor of [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html).

    Examples

    Example: RightAngleExample

    ![../_images/RightAngleExample-1.png](https://docs.manim.community/en/stable/_images/RightAngleExample-1.png)

    ```
    class RightAngleExample(Scene):
        def construct(self):
            line1 = Line( LEFT, RIGHT )
            line2 = Line( DOWN, UP )
            rightangles = [
                RightAngle(line1, line2),
                RightAngle(line1, line2, length=0.4, quadrant=(1,-1)),
                RightAngle(line1, line2, length=0.5, quadrant=(-1,1), stroke_width=8),
                RightAngle(line1, line2, length=0.7, quadrant=(-1,-1), color=RED),
            ]
            plots = VGroup()
            for rightangle in rightangles:
                plot=VGroup(line1.copy(),line2.copy(), rightangle)
                plots.add(plot)
            plots.arrange(buff=1.5)
            self.add(plots)
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

    \_original\_\_init\_\_(*line1*, *line2*, *length=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **line1** ([*Line*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html))
            - **line2** ([*Line*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html))
            - **length** (*float* *|* *None*)
            - **kwargs** (*Any*)

        Return type:
        :   None
