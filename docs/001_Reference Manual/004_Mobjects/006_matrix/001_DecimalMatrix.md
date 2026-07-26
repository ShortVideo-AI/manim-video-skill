---
{
  "title": "DecimalMatrix",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.matrix.DecimalMatrix.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "matrix",
    "DecimalMatrix"
  ],
  "scraped_at": "2026-07-10T15:59:43"
}
---

# DecimalMatrix

Qualified name: `manim.mobject.matrix.DecimalMatrix`

class DecimalMatrix(*matrix*, *element\_to\_mobject=<class 'manim.mobject.text.numbers.DecimalNumber'>*, *element\_to\_mobject\_config={'num\_decimal\_places': 1}*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html)
:   Bases: [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html)

    A mobject that displays a matrix with decimal entries on the screen.

    Examples

    Example: DecimalMatrixExample

    ![../_images/DecimalMatrixExample-1.png](https://docs.manim.community/en/stable/_images/DecimalMatrixExample-1.png)

    ```
    class DecimalMatrixExample(Scene):
        def construct(self):
            m0 = DecimalMatrix(
                [[3.456, 2.122], [33.2244, 12]],
                element_to_mobject_config={"num_decimal_places": 2},
                left_bracket="\\{",
                right_bracket="\\}")
            self.add(m0)
    ```

    Will round/truncate the decimal places as per the provided config.

    Parameters:
    :   - **matrix** (*Iterable*) – A numpy 2d array or list of lists
        - **element\_to\_mobject** (*type**[*[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]*) – Mobject to use, by default DecimalNumber
        - **element\_to\_mobject\_config** (*dict**[**str**,* *Any**]*) – Config for the desired mobject, by default {“num\_decimal\_places”: 1}
        - **kwargs** (*Any*)

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

    \_original\_\_init\_\_(*matrix*, *element\_to\_mobject=<class 'manim.mobject.text.numbers.DecimalNumber'>*, *element\_to\_mobject\_config={'num\_decimal\_places': 1}*, *\*\*kwargs*)
    :   Will round/truncate the decimal places as per the provided config.

        Parameters:
        :   - **matrix** (*Iterable*) – A numpy 2d array or list of lists
            - **element\_to\_mobject** (*type**[*[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]*) – Mobject to use, by default DecimalNumber
            - **element\_to\_mobject\_config** (*dict**[**str**,* *Any**]*) – Config for the desired mobject, by default {“num\_decimal\_places”: 1}
            - **kwargs** (*Any*)
