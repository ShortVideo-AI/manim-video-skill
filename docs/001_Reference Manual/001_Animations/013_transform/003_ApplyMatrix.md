---
{
  "title": "ApplyMatrix",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "ApplyMatrix"
  ],
  "scraped_at": "2026-07-10T15:58:12"
}
---

# ApplyMatrix

Qualified name: `manim.animation.transform.ApplyMatrix`

class ApplyMatrix(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`ApplyPointwiseFunction`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html)

    Applies a matrix transform to an mobject.

    Parameters:
    :   - **matrix** (*np.ndarray*) – The transformation matrix.
        - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).
        - **about\_point** (*np.ndarray*) – The origin point for the transform. Defaults to `ORIGIN`.
        - **kwargs** – Further keyword arguments that are passed to [`ApplyPointwiseFunction`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html).

    Examples

    Example: ApplyMatrixExample

    [
    ](./ApplyMatrixExample-1.mp4)

    ```
    class ApplyMatrixExample(Scene):
        def construct(self):
            matrix = [[1, 1], [0, 2/3]]
            self.play(ApplyMatrix(matrix, Text("Hello World!")), ApplyMatrix(matrix, NumberPlane()))
    ```

    Methods

    |  |  |
    | --- | --- |
    | `initialize_matrix` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*matrix*, *mobject*, *about\_point=array([0., 0., 0.])*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **matrix** (*ndarray*)
            - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **about\_point** (*ndarray*)

        Return type:
        :   None
