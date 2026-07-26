---
{
  "title": "CurvesAsSubmobjects",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "types",
    "vectorized_mobject",
    "CurvesAsSubmobjects"
  ],
  "scraped_at": "2026-07-10T16:00:33"
}
---

# CurvesAsSubmobjects

Qualified name: `manim.mobject.types.vectorized\_mobject.CurvesAsSubmobjects`

class CurvesAsSubmobjects(*vmobject*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
:   Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    Convert a curve’s elements to submobjects.

    Examples

    Example: LineGradientExample

    ![../_images/LineGradientExample-1.png](https://docs.manim.community/en/stable/_images/LineGradientExample-1.png)

    ```
    class LineGradientExample(Scene):
        def construct(self):
            curve = ParametricFunction(lambda t: [t, np.sin(t), 0], t_range=[-PI, PI, 0.01], stroke_width=10)
            new_curve = CurvesAsSubmobjects(curve)
            new_curve.set_color_by_gradient(BLUE, RED)
            self.add(new_curve.shift(UP), curve)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`point_from_proportion`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.point_from_proportion) | Gets the point at a proportion along the path of the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects). |

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
    :   **vmobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))

    \_original\_\_init\_\_(*vmobject*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **vmobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))

        Return type:
        :   None

    point\_from\_proportion(*alpha*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Gets the point at a proportion along the path of the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects).

        Parameters:
        :   **alpha** (*float*) – The proportion along the the path of the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects).

        Returns:
        :   The point on the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects).

        Return type:
        :   `numpy.ndarray`

        Raises:
        :   - **ValueError** – If `alpha` is not between 0 and 1.
            - **Exception** – If the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects) has no submobjects, or no submobject has points.
