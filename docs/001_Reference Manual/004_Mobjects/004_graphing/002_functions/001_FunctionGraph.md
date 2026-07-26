---
{
  "title": "FunctionGraph",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.FunctionGraph.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "graphing",
    "functions",
    "FunctionGraph"
  ],
  "scraped_at": "2026-07-10T15:59:33"
}
---

# FunctionGraph

Qualified name: `manim.mobject.graphing.functions.FunctionGraph`

class FunctionGraph(*function*, *x\_range=None*, *color=ManimColor('#FFFF00')*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/functions.html)
:   Bases: [`ParametricFunction`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ParametricFunction.html)

    A [`ParametricFunction`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ParametricFunction.html) that spans the length of the scene by default.

    Examples

    Example: ExampleFunctionGraph

    ![../_images/ExampleFunctionGraph-1.png](https://docs.manim.community/en/stable/_images/ExampleFunctionGraph-1.png)

    ```
    class ExampleFunctionGraph(Scene):
        def construct(self):
            cos_func = FunctionGraph(
                lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
                color=RED,
            )

            sin_func_1 = FunctionGraph(
                lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
                color=BLUE,
            )

            sin_func_2 = FunctionGraph(
                lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
                x_range=[-4, 4],
                color=GREEN,
            ).move_to([0, 1, 0])

            self.add(cos_func, sin_func_1, sin_func_2)
    ```

    Methods

    |  |  |
    | --- | --- |
    | `get_function` |  |
    | `get_point_from_function` |  |

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

    Parameters:
    :   - **function** (*Callable**[**[**float**]**,* *Any**]*)
        - **x\_range** (*tuple**[**float**,* *float**]* *|* *tuple**[**float**,* *float**,* *float**]* *|* *None*)
        - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*function*, *x\_range=None*, *color=ManimColor('#FFFF00')*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **function** (*Callable**[**[**float**]**,* *Any**]*)
            - **x\_range** (*tuple**[**float**,* *float**]* *|* *tuple**[**float**,* *float**,* *float**]* *|* *None*)
            - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
            - **kwargs** (*Any*)

        Return type:
        :   None
