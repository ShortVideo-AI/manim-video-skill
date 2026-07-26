---
{
  "title": "ComplexPlane",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "graphing",
    "coordinate_systems",
    "ComplexPlane"
  ],
  "scraped_at": "2026-07-10T15:59:27"
}
---

# ComplexPlane

Qualified name: `manim.mobject.graphing.coordinate\_systems.ComplexPlane`

class ComplexPlane(*\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
:   Bases: [`NumberPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html)

    A [`NumberPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html) specialized for use with complex numbers.

    Examples

    Example: ComplexPlaneExample

    ![../_images/ComplexPlaneExample-1.png](https://docs.manim.community/en/stable/_images/ComplexPlaneExample-1.png)

    ```
    class ComplexPlaneExample(Scene):
        def construct(self):
            plane = ComplexPlane().add_coordinates()
            self.add(plane)
            d1 = Dot(plane.n2p(2 + 1j), color=YELLOW)
            d2 = Dot(plane.n2p(-3 - 2j), color=YELLOW)
            label1 = MathTex("2+i").next_to(d1, UR, 0.1)
            label2 = MathTex("-3-2i").next_to(d2, UR, 0.1)
            self.add(
                d1,
                label1,
                d2,
                label2,
            )
    ```

    References: [`Dot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html) [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html)

    Methods

    |  |  |
    | --- | --- |
    | [`add_coordinates`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.add_coordinates) | Adds the labels produced from `get_coordinate_labels()` to the plane. |
    | [`get_coordinate_labels`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.get_coordinate_labels) | Generates the [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html) mobjects for the coordinates of the plane. |
    | [`n2p`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.n2p) | Abbreviation for [`number_to_point()`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point). |
    | [`number_to_point`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point) | Accepts a float/complex number and returns the equivalent point on the plane. |
    | [`p2n`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.p2n) | Abbreviation for [`point_to_number()`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number). |
    | [`point_to_number`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number) | Accepts a point and returns a complex number equivalent to that point on the plane. |

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
    :   **kwargs** (*Any*)

    \_get\_default\_coordinate\_values()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
    :   Generate a list containing the numerical values of the plane’s labels.

        Returns:
        :   A list of floats representing the x-axis and complex numbers representing the y-axis.

        Return type:
        :   List[float | complex]

    \_original\_\_init\_\_(*\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **kwargs** (*Any*)

    add\_coordinates(*\*numbers*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
    :   Adds the labels produced from `get_coordinate_labels()` to the plane.

        Parameters:
        :   - **numbers** (*Iterable**[**float* *|* *complex**]*) – An iterable of floats/complex numbers. Floats are positioned along the x-axis, complex numbers along the y-axis.
            - **kwargs** (*Any*) – Additional arguments to be passed to [`get_number_mobject()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html), i.e. [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html).

        Return type:
        :   *Self*

    get\_coordinate\_labels(*\*numbers*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
    :   Generates the [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html) mobjects for the coordinates of the plane.

        Parameters:
        :   - **numbers** (*Iterable**[**float* *|* *complex**]*) – An iterable of floats/complex numbers. Floats are positioned along the x-axis, complex numbers along the y-axis.
            - **kwargs** (*Any*) – Additional arguments to be passed to [`get_number_mobject()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html), i.e. [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html).

        Returns:
        :   A [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) containing the positioned label mobjects.

        Return type:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    n2p(*number*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
    :   Abbreviation for [`number_to_point()`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point).

        Parameters:
        :   **number** (*float* *|* *complex*)

        Return type:
        :   *ndarray*

    number\_to\_point(*number*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
    :   Accepts a float/complex number and returns the equivalent point on the plane.

        Parameters:
        :   **number** (*float* *|* *complex*) – The number. Can be a float or a complex number.

        Returns:
        :   The point on the plane.

        Return type:
        :   np.ndarray

    p2n(*point*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
    :   Abbreviation for [`point_to_number()`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number).

        Parameters:
        :   **point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))

        Return type:
        :   complex

    point\_to\_number(*point*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
    :   Accepts a point and returns a complex number equivalent to that point on the plane.

        Parameters:
        :   **point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The point in manim’s coordinate-system

        Returns:
        :   A complex number consisting of real and imaginary components.

        Return type:
        :   complex
