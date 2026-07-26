---
{
  "title": "Cone",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "three_d",
    "three_dimensions",
    "Cone"
  ],
  "scraped_at": "2026-07-10T16:00:18"
}
---

# Cone

Qualified name: `manim.mobject.three\_d.three\_dimensions.Cone`

class Cone(*base\_radius=1*, *height=1*, *direction=array([0., 0., 1.])*, *show\_base=False*, *v\_range=(0, 6.283185307179586)*, *u\_min=0*, *checkerboard\_colors=False*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
:   Bases: [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html)

    A circular cone.
    Can be defined using 2 parameters: its height, and its base radius.
    The polar angle, theta, can be calculated using arctan(base\_radius /
    height) The spherical radius, r, is calculated using the pythagorean
    theorem.

    Parameters:
    :   - **base\_radius** (*float*) – The base radius from which the cone tapers.
        - **height** (*float*) – The height measured from the plane formed by the base\_radius to
          the apex of the cone.
        - **direction** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The direction of the apex.
        - **show\_base** (*bool*) – Whether to show the base plane or not.
        - **v\_range** (*tuple**[**float**,* *float**]*) – The azimuthal angle to start and end at.
        - **u\_min** (*float*) – The radius at the apex.
        - **checkerboard\_colors** (*list**[*[*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)*]* *|* *Literal**[**False**]*) – Show checkerboard grid texture on the cone.
        - **kwargs** (*Any*)

    Examples

    Example: ExampleCone

    ![../_images/ExampleCone-1.png](https://docs.manim.community/en/stable/_images/ExampleCone-1.png)

    ```
    class ExampleCone(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            cone = Cone(direction=X_AXIS+Y_AXIS+2*Z_AXIS, resolution=8)
            self.set_camera_orientation(phi=5*PI/11, theta=PI/9)
            self.add(axes, cone)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`func`](#manim.mobject.three_d.three_dimensions.Cone.func) | Converts from spherical coordinates to cartesian. |
    | [`get_direction`](#manim.mobject.three_d.three_dimensions.Cone.get_direction) | Returns the current direction of the apex of the [`Cone`](#manim.mobject.three_d.three_dimensions.Cone). |
    | [`get_end`](#manim.mobject.three_d.three_dimensions.Cone.get_end) | Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) ends. |
    | [`get_start`](#manim.mobject.three_d.three_dimensions.Cone.get_start) | Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) starts. |
    | [`set_direction`](#manim.mobject.three_d.three_dimensions.Cone.set_direction) | Changes the direction of the apex of the [`Cone`](#manim.mobject.three_d.three_dimensions.Cone). |

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

    \_original\_\_init\_\_(*base\_radius=1*, *height=1*, *direction=array([0., 0., 1.])*, *show\_base=False*, *v\_range=(0, 6.283185307179586)*, *u\_min=0*, *checkerboard\_colors=False*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **base\_radius** (*float*)
            - **height** (*float*)
            - **direction** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **show\_base** (*bool*)
            - **v\_range** (*tuple**[**float**,* *float**]*)
            - **u\_min** (*float*)
            - **checkerboard\_colors** (*Iterable**[**TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)**]* *|* *Literal**[**False**]*)
            - **kwargs** (*Any*)

        Return type:
        :   None

    func(*u*, *v*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
    :   Converts from spherical coordinates to cartesian.

        Parameters:
        :   - **u** (*float*) – The radius.
            - **v** (*float*) – The azimuthal angle.

        Returns:
        :   Points defining the [`Cone`](#manim.mobject.three_d.three_dimensions.Cone).

        Return type:
        :   `numpy.array`

    get\_direction()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
    :   Returns the current direction of the apex of the [`Cone`](#manim.mobject.three_d.three_dimensions.Cone).

        Returns:
        :   **direction** – The direction of the apex.

        Return type:
        :   `numpy.array`

    get\_end()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
    :   Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) ends.

        Return type:
        :   [*Point3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)

    get\_start()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
    :   Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) starts.

        Return type:
        :   [*Point3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)

    set\_direction(*direction*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html)
    :   Changes the direction of the apex of the [`Cone`](#manim.mobject.three_d.three_dimensions.Cone).

        Parameters:
        :   **direction** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The direction of the apex.

        Return type:
        :   None
