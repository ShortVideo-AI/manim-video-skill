---
{
  "title": "LabeledArrow",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledArrow.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "labeled",
    "LabeledArrow"
  ],
  "scraped_at": "2026-07-10T15:58:55"
}
---

# LabeledArrow

Qualified name: `manim.mobject.geometry.labeled.LabeledArrow`

class LabeledArrow(*\*args*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/labeled.html)
:   Bases: [`LabeledLine`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledLine.html), [`Arrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html)

    Constructs an arrow containing a label box somewhere along its length.
    This class inherits its label properties from LabeledLine, so the main parameters controlling it are the same.

    Parameters:
    :   - **label** – Label that will be displayed on the Arrow.
        - **label\_position** – A ratio in the range [0-1] to indicate the position of the label with respect to the length of the line. Default value is 0.5.
        - **label\_config** – A dictionary containing the configuration for the label.
          This is only applied if `label` is of type `str`.
        - **box\_config** – A dictionary containing the configuration for the background box.
        - **frame\_config** –

          A dictionary containing the configuration for the frame.

          See also

          [`LabeledLine`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledLine.html)
        - **args** (*Any*)
        - **kwargs** (*Any*)

    Examples

    Example: LabeledArrowExample

    ![../_images/LabeledArrowExample-1.png](https://docs.manim.community/en/stable/_images/LabeledArrowExample-1.png)

    ```
    class LabeledArrowExample(Scene):
        def construct(self):
            l_arrow = LabeledArrow("0.5", start=LEFT*3, end=RIGHT*3 + UP*2, label_position=0.5)

            self.add(l_arrow)
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

    \_original\_\_init\_\_(*\*args*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **args** (*Any*)
            - **kwargs** (*Any*)

        Return type:
        :   None
