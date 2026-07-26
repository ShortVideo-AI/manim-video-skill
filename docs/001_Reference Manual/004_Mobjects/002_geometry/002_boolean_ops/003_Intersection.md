---
{
  "title": "Intersection",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Intersection.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "boolean_ops",
    "Intersection"
  ],
  "scraped_at": "2026-07-10T15:58:53"
}
---

# Intersection

Qualified name: `manim.mobject.geometry.boolean\_ops.Intersection`

class Intersection(*\*vmobjects*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/boolean_ops.html)
:   Bases: `_BooleanOps`

    Find the intersection of two [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) s.
    This keeps the parts covered by both [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) s.

    Parameters:
    :   - **vmobjects** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)) – The [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) to find the intersection.
        - **kwargs** (*Any*)

    Raises:
    :   **ValueError** – If less the 2 [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) are passed.

    Example

    Example: IntersectionExample

    ![../_images/IntersectionExample-2.png](https://docs.manim.community/en/stable/_images/IntersectionExample-2.png)

    ```
    class IntersectionExample(Scene):
        def construct(self):
            sq = Square(color=RED, fill_opacity=1)
            sq.move_to([-2, 0, 0])
            cr = Circle(color=BLUE, fill_opacity=1)
            cr.move_to([-1.3, 0.7, 0])
            un = Intersection(sq, cr, color=GREEN, fill_opacity=1)
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

    \_original\_\_init\_\_(*\*vmobjects*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **vmobjects** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))
            - **kwargs** (*Any*)

        Return type:
        :   None
