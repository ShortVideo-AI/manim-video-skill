---
{
  "title": "MobjectMatrix",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "matrix",
    "MobjectMatrix"
  ],
  "scraped_at": "2026-07-10T15:59:45"
}
---

# MobjectMatrix

Qualified name: `manim.mobject.matrix.MobjectMatrix`

class MobjectMatrix(*matrix*, *element\_to\_mobject=<function MobjectMatrix.<lambda>>*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html)
:   Bases: [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html)

    A mobject that displays a matrix of mobject entries on the screen.

    Examples

    Example: MobjectMatrixExample

    ![../_images/MobjectMatrixExample-1.png](https://docs.manim.community/en/stable/_images/MobjectMatrixExample-1.png)

    ```
    class MobjectMatrixExample(Scene):
        def construct(self):
            a = Circle().scale(0.3)
            b = Square().scale(0.3)
            c = MathTex("\\pi").scale(2)
            d = Star().scale(0.3)
            m0 = MobjectMatrix([[a, b], [c, d]])
            self.add(m0)
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

    Parameters:
    :   - **matrix** (*Iterable*)
        - **element\_to\_mobject** (*type**[*[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]* *|* *Callable**[**...**,* [*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*matrix*, *element\_to\_mobject=<function MobjectMatrix.<lambda>>*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **matrix** (*Iterable*)
            - **element\_to\_mobject** (*type**[*[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]* *|* *Callable**[**[**...**]**,* [*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]*)
            - **kwargs** (*Any*)
