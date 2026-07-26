---
{
  "title": "Elbow",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Elbow.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "line",
    "Elbow"
  ],
  "scraped_at": "2026-07-10T15:59:01"
}
---

# Elbow

Qualified name: `manim.mobject.geometry.line.Elbow`

class Elbow(*width=0.2*, *angle=0*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    Two lines that create a right angle about each other: L-shape.

    Parameters:
    :   - **width** (*float*) – The length of the elbow’s sides.
        - **angle** (*float*) – The rotation of the elbow.
        - **kwargs** (*Any*) – Additional arguments to be passed to [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)
        - **seealso::** (*..*) – [`RightAngle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.RightAngle.html)

    Examples

    Example: ElbowExample

    ![../_images/ElbowExample-1.png](https://docs.manim.community/en/stable/_images/ElbowExample-1.png)

    ```
    class ElbowExample(Scene):
        def construct(self):
            elbow_1 = Elbow()
            elbow_2 = Elbow(width=2.0)
            elbow_3 = Elbow(width=2.0, angle=5*PI/4)

            elbow_group = Group(elbow_1, elbow_2, elbow_3).arrange(buff=1)
            self.add(elbow_group)
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

    \_original\_\_init\_\_(*width=0.2*, *angle=0*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **width** (*float*)
            - **angle** (*float*)
            - **kwargs** (*Any*)

        Return type:
        :   None
