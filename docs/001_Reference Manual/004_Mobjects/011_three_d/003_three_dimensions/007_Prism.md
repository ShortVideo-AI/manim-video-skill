---
{
  "title": "Prism",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "three_d",
    "three_dimensions",
    "Prism"
  ],
  "scraped_at": "2026-07-10T16:00:21"
}
---

# Prism

Qualified name: `manim.mobject.three\_d.three\_dimensions.Prism`

class Prism(*dimensions=[3, 2, 1]*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
:   Bases: [`Cube`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cube.html)

    A right rectangular prism (or rectangular cuboid).
    Defined by the length of each side in `[x, y, z]` format.

    Parameters:
    :   - **dimensions** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – Dimensions of the [`Prism`](#manim.mobject.three_d.three_dimensions.Prism) in `[x, y, z]` format.
        - **kwargs** (*Any*)

    Examples

    Example: ExamplePrism

    ![../_images/ExamplePrism-1.png](https://docs.manim.community/en/stable/_images/ExamplePrism-1.png)

    ```
    class ExamplePrism(ThreeDScene):
        def construct(self):
            self.set_camera_orientation(phi=60 * DEGREES, theta=150 * DEGREES)
            prismSmall = Prism(dimensions=[1, 2, 3]).rotate(PI / 2)
            prismLarge = Prism(dimensions=[1.5, 3, 4.5]).move_to([2, 0, 0])
            self.add(prismSmall, prismLarge)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.three_d.three_dimensions.Prism.generate_points) | Creates the sides of the [`Prism`](#manim.mobject.three_d.three_dimensions.Prism). |

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

    \_original\_\_init\_\_(*dimensions=[3, 2, 1]*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **dimensions** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **kwargs** (*Any*)

        Return type:
        :   None

    generate\_points()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
    :   Creates the sides of the [`Prism`](#manim.mobject.three_d.three_dimensions.Prism).

        Return type:
        :   None
