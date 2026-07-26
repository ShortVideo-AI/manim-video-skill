---
{
  "title": "Exclusion",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Exclusion.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "boolean_ops",
    "Exclusion"
  ],
  "scraped_at": "2026-07-10T15:58:53"
}
---

# Exclusion

Qualified name: `manim.mobject.geometry.boolean\_ops.Exclusion`

class Exclusion(*subject*, *clip*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/boolean_ops.html)
:   Bases: `_BooleanOps`

    Find the XOR between two [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html).
    This creates a new [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) consisting of the region
    covered by exactly one of them.

    Parameters:
    :   - **subject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)) – The 1st [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html).
        - **clip** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)) – The 2nd [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)
        - **kwargs** (*Any*)

    Example

    Example: IntersectionExample

    ![../_images/IntersectionExample-1.png](https://docs.manim.community/en/stable/_images/IntersectionExample-1.png)

    ```
    class IntersectionExample(Scene):
        def construct(self):
            sq = Square(color=RED, fill_opacity=1)
            sq.move_to([-2, 0, 0])
            cr = Circle(color=BLUE, fill_opacity=1)
            cr.move_to([-1.3, 0.7, 0])
            un = Exclusion(sq, cr, color=GREEN, fill_opacity=1)
            un.move_to([1.5, 0.4, 0])
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
