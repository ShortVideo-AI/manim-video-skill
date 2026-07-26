---
{
  "title": "Sphere",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Sphere.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "three_d",
    "three_dimensions",
    "Sphere"
  ],
  "scraped_at": "2026-07-10T16:00:22"
}
---

# Sphere

Qualified name: `manim.mobject.three\_d.three\_dimensions.Sphere`

class Sphere(*center=array([0., 0., 0.])*, *radius=1*, *resolution=None*, *u\_range=(0, 6.283185307179586)*, *v\_range=(0, 3.141592653589793)*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
:   Bases: [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html)

    A three-dimensional sphere.

    Parameters:
    :   - **center** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – Center of the [`Sphere`](#manim.mobject.three_d.three_dimensions.Sphere).
        - **radius** (*float*) – The radius of the [`Sphere`](#manim.mobject.three_d.three_dimensions.Sphere).
        - **resolution** (*int* *|* *Sequence**[**int**]* *|* *None*) – The number of samples taken of the [`Sphere`](#manim.mobject.three_d.three_dimensions.Sphere). A tuple can be used
          to define different resolutions for `u` and `v` respectively.
        - **u\_range** (*tuple**[**float**,* *float**]*) – The range of the `u` variable: `(u_min, u_max)`.
        - **v\_range** (*tuple**[**float**,* *float**]*) – The range of the `v` variable: `(v_min, v_max)`.
        - **kwargs** (*Any*)

    Examples

    Example: ExampleSphere

    ![../_images/ExampleSphere-1.png](https://docs.manim.community/en/stable/_images/ExampleSphere-1.png)

    ```
    class ExampleSphere(ThreeDScene):
        def construct(self):
            self.set_camera_orientation(phi=PI / 6, theta=PI / 6)
            sphere1 = Sphere(
                center=(3, 0, 0),
                radius=1,
                resolution=(20, 20),
                u_range=[0.001, PI - 0.001],
                v_range=[0, TAU]
            )
            sphere1.set_color(RED)
            self.add(sphere1)
            sphere2 = Sphere(center=(-1, -3, 0), radius=2, resolution=(18, 18))
            sphere2.set_color(GREEN)
            self.add(sphere2)
            sphere3 = Sphere(center=(-1, 2, 0), radius=2, resolution=(16, 16))
            sphere3.set_color(BLUE)
            self.add(sphere3)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`func`](#manim.mobject.three_d.three_dimensions.Sphere.func) | The z values defining the [`Sphere`](#manim.mobject.three_d.three_dimensions.Sphere) being plotted. |

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

    \_original\_\_init\_\_(*center=array([0., 0., 0.])*, *radius=1*, *resolution=None*, *u\_range=(0, 6.283185307179586)*, *v\_range=(0, 3.141592653589793)*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **center** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **radius** (*float*)
            - **resolution** (*int* *|* *Sequence**[**int**]* *|* *None*)
            - **u\_range** (*tuple**[**float**,* *float**]*)
            - **v\_range** (*tuple**[**float**,* *float**]*)
            - **kwargs** (*Any*)

        Return type:
        :   None

    func(*u*, *v*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
    :   The z values defining the [`Sphere`](#manim.mobject.three_d.three_dimensions.Sphere) being plotted.

        Returns:
        :   The z values defining the [`Sphere`](#manim.mobject.three_d.three_dimensions.Sphere).

        Return type:
        :   `Point3D`

        Parameters:
        :   - **u** (*float*)
            - **v** (*float*)
