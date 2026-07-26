---
{
  "title": "ApplyPointwiseFunction",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "ApplyPointwiseFunction"
  ],
  "scraped_at": "2026-07-10T15:58:13"
}
---

# ApplyPointwiseFunction

Qualified name: `manim.animation.transform.ApplyPointwiseFunction`

class ApplyPointwiseFunction(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`ApplyMethod`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html)

    Animation that applies a pointwise function to a mobject.

    Examples

    Example: WarpSquare

    [
    ](./WarpSquare-1.mp4)

    ```
    class WarpSquare(Scene):
        def construct(self):
            square = Square()
            self.play(
                ApplyPointwiseFunction(
                    lambda point: complex_to_R3(np.exp(R3_to_complex(point))), square
                )
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
    :   - **function** (*types.MethodType*)
        - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
        - **run\_time** (*float*)

    \_original\_\_init\_\_(*function*, *mobject*, *run\_time=3.0*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **function** (*MethodType*)
            - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **run\_time** (*float*)

        Return type:
        :   None
