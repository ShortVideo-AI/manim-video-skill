---
{
  "title": "Difference",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "boolean_ops",
    "Difference"
  ],
  "scraped_at": "2026-07-10T15:58:52"
}
---

# Difference

Qualified name: `manim.mobject.geometry.boolean\_ops.Difference`

class Difference(*subject*, *clip*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/boolean_ops.html)
:   Bases: `_BooleanOps`

    Subtracts one [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) from another one.

    Parameters:
    :   - **subject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)) – The 1st [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html).
        - **clip** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)) – The 2nd [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)
        - **kwargs** (*Any*)

    Example

    Example: DifferenceExample

    ![../_images/DifferenceExample-1.png](https://docs.manim.community/en/stable/_images/DifferenceExample-1.png)

    ```
    class DifferenceExample(Scene):
        def construct(self):
            sq = Square(color=RED, fill_opacity=1)
            sq.move_to([-2, 0, 0])
            cr = Circle(color=BLUE, fill_opacity=1)
            cr.move_to([-1.3, 0.7, 0])
            un = Difference(sq, cr, color=GREEN, fill_opacity=1)
            un.move_to([1.5, 0, 0])
            self.add(sq, cr, un)
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

    \_original\_\_init\_\_(*subject*, *clip*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **subject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))
            - **clip** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))
            - **kwargs** (*Any*)

        Return type:
        :   None
