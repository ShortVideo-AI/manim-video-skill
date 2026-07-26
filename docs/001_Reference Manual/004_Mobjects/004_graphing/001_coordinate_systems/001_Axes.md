---
{
  "title": "Axes",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "graphing",
    "coordinate_systems",
    "Axes"
  ],
  "scraped_at": "2026-07-10T15:59:26"
}
---

# Axes

Qualified name: `manim.mobject.graphing.coordinate\_systems.Axes`

class Axes(*x\_range=None*, *y\_range=None*, *x\_length=12*, *y\_length=6*, *axis\_config=None*, *x\_axis\_config=None*, *y\_axis\_config=None*, *tips=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
:   Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html), [`CoordinateSystem`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html)

    Creates a set of axes.

    Parameters:
    :   - **x\_range** (*Sequence**[**float**]* *|* *None*) – The `(x_min, x_max, x_step)` values of the x-axis.
        - **y\_range** (*Sequence**[**float**]* *|* *None*) – The `(y_min, y_max, y_step)` values of the y-axis.
        - **x\_length** (*float* *|* *None*) – The length of the x-axis.
        - **y\_length** (*float* *|* *None*) – The length of the y-axis.
        - **axis\_config** (*dict* *|* *None*) – Arguments to be passed to [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html) that influences both axes.
        - **x\_axis\_config** (*dict* *|* *None*) – Arguments to be passed to [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html) that influence the x-axis.
        - **y\_axis\_config** (*dict* *|* *None*) – Arguments to be passed to [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html) that influence the y-axis.
        - **tips** (*bool*) – Whether or not to include the tips on both axes.
        - **kwargs** (*Any*) – Additional arguments to be passed to [`CoordinateSystem`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html) and [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html).

    Examples

    Example: LogScalingExample

    ![../_images/LogScalingExample-1.png](https://docs.manim.community/en/stable/_images/LogScalingExample-1.png)

    ```
    class LogScalingExample(Scene):
        def construct(self):
            ax = Axes(
                x_range=[0, 10, 1],
                y_range=[-2, 6, 1],
                tips=False,
                axis_config={"include_numbers": True},
                y_axis_config={"scaling": LogBase(custom_labels=True)},
            )

            # x_min must be > 0 because log is undefined at 0.
            graph = ax.plot(lambda x: x ** 2, x_range=[0.001, 10], use_smoothing=False)
            self.add(ax, graph)
    ```

    Styling arguments can be passed to the underlying [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html)
    mobjects that represent the axes:

    Example: AxesWithDifferentTips

    ![../_images/AxesWithDifferentTips-1.png](https://docs.manim.community/en/stable/_images/AxesWithDifferentTips-1.png)

    ```
    class AxesWithDifferentTips(Scene):
        def construct(self):
            ax = Axes(axis_config={'tip_shape': StealthTip})
            self.add(ax)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`coords_to_point`](#manim.mobject.graphing.coordinate_systems.Axes.coords_to_point) | Accepts coordinates from the axes and returns a point with respect to the scene. |
    | [`get_axes`](#manim.mobject.graphing.coordinate_systems.Axes.get_axes) | Gets the axes. |
    | [`get_axis_labels`](#manim.mobject.graphing.coordinate_systems.Axes.get_axis_labels) | Defines labels for the x-axis and y-axis of the graph. |
    | [`plot_line_graph`](#manim.mobject.graphing.coordinate_systems.Axes.plot_line_graph) | Draws a line graph. |
    | [`point_to_coords`](#manim.mobject.graphing.coordinate_systems.Axes.point_to_coords) | Accepts a point from the scene and returns its coordinates with respect to the axes. |

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

    \_create\_axis(*range\_terms*, *axis\_config*, *length*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
    :   Creates an axis and dynamically adjusts its position depending on where 0 is located on the line.

        Parameters:
        :   - **range\_terms** (*Sequence**[**float**]*) – The range of the the axis : `(x_min, x_max, x_step)`.
            - **axis\_config** (*dict**[**str**,* *Any**]*) – Additional parameters that are passed to [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html).
            - **length** (*float*) – The length of the axis.

        Returns:
        :   Returns a number line based on `range_terms`.

        Return type:
        :   `NumberLine`

    static \_origin\_shift(*axis\_range*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
    :   Determines how to shift graph mobjects to compensate when 0 is not on the axis.

        Parameters:
        :   **axis\_range** (*Sequence**[**float**]*) – The range of the axis : `(x_min, x_max, x_step)`.

        Return type:
        :   float

    \_original\_\_init\_\_(*x\_range=None*, *y\_range=None*, *x\_length=12*, *y\_length=6*, *axis\_config=None*, *x\_axis\_config=None*, *y\_axis\_config=None*, *tips=True*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **x\_range** (*Sequence**[**float**]* *|* *None*)
            - **y\_range** (*Sequence**[**float**]* *|* *None*)
            - **x\_length** (*float* *|* *None*)
            - **y\_length** (*float* *|* *None*)
            - **axis\_config** (*dict* *|* *None*)
            - **x\_axis\_config** (*dict* *|* *None*)
            - **y\_axis\_config** (*dict* *|* *None*)
            - **tips** (*bool*)
            - **kwargs** (*Any*)

    static \_update\_default\_configs(*default\_configs*, *passed\_configs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
    :   Takes in two tuples of dicts and return modifies the first such that values from
        `passed_configs` overwrite values in `default_configs`. If a key does not exist
        in default\_configs, it is added to the dict.

        This method is useful for having defaults in a class and being able to overwrite
        them with user-defined input.

        Parameters:
        :   - **default\_configs** (*tuple**[**dict**[**Any**,* *Any**]**]*) – The dict that will be updated.
            - **passed\_configs** (*tuple**[**dict**[**Any**,* *Any**]**]*) – The dict that will be used to update.

        Return type:
        :   None

        Examples

        To create a tuple with one dictionary, add a comma after the element:

        ```
        self._update_default_configs(
            (dict_1,)(
                dict_2,
            )
        )
        ```

    coords\_to\_point(*\*coords*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
    :   Accepts coordinates from the axes and returns a point with respect to the scene.
        Equivalent to ax @ (coord1)

        Parameters:
        :   **coords** (*float* *|* *Sequence**[**float**]* *|* *Sequence**[**Sequence**[**float**]**]* *|* *ndarray*) –

            The coordinates. Each coord is passed as a separate argument: `ax.coords_to_point(1, 2, 3)`.

            Also accepts a list of coordinates

            `ax.coords_to_point( [x_0, x_1, ...], [y_0, y_1, ...], ... )`

            `ax.coords_to_point( [[x_0, y_0, z_0], [x_1, y_1, z_1]] )`

            A single coordinate can also be passed as a flat list or 1D array:

            `ax.coords_to_point( [x, y, z] )`

        Returns:
        :   A point with respect to the scene’s coordinate system.
            The shape of the array will be similar to the shape of the input.

        Return type:
        :   np.ndarray

        Examples

        Example: CoordsToPointExample

        ![../_images/CoordsToPointExample-1.png](https://docs.manim.community/en/stable/_images/CoordsToPointExample-1.png)

        ```
        class CoordsToPointExample(Scene):
            def construct(self):
                ax = Axes().add_coordinates()

                # a dot with respect to the axes
                dot_axes = Dot(ax.coords_to_point(2, 2), color=GREEN)
                lines = ax.get_lines_to_point(ax.c2p(2,2))

                # a dot with respect to the scene
                # the default plane corresponds to the coordinates of the scene.
                plane = NumberPlane()
                dot_scene = Dot((2,2,0), color=RED)

                self.add(plane, dot_scene, ax, dot_axes, lines)
        ```

    get\_axes()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
    :   Gets the axes.

        Returns:
        :   A pair of axes.

        Return type:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    get\_axis\_labels(*x\_label='x'*, *y\_label='y'*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
    :   Defines labels for the x-axis and y-axis of the graph.

        For increased control over the position of the labels,
        use [`get_x_axis_label()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html) and
        [`get_y_axis_label()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html).

        Parameters:
        :   - **x\_label** (*float* *|* *str* *|* [*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The label for the x\_axis. Defaults to [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html) for `str` and `float` inputs.
            - **y\_label** (*float* *|* *str* *|* [*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The label for the y\_axis. Defaults to [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html) for `str` and `float` inputs.

        Returns:
        :   A [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) of the labels for the x\_axis and y\_axis.

        Return type:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

        See also

        [`get_x_axis_label()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html)
        [`get_y_axis_label()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html)

        Examples

        Example: GetAxisLabelsExample

        ![../_images/GetAxisLabelsExample-1.png](https://docs.manim.community/en/stable/_images/GetAxisLabelsExample-1.png)

        ```
        class GetAxisLabelsExample(Scene):
            def construct(self):
                ax = Axes()
                labels = ax.get_axis_labels(
                    Tex("x-axis").scale(0.7), Text("y-axis").scale(0.45)
                )
                self.add(ax, labels)
        ```

    plot\_line\_graph(*x\_values*, *y\_values*, *z\_values=None*, *line\_color=ManimColor('#FFFF00')*, *add\_vertex\_dots=True*, *vertex\_dot\_radius=0.08*, *vertex\_dot\_style=None*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
    :   Draws a line graph.

        The graph connects the vertices formed from zipping
        `x_values`, `y_values` and `z_values`. Also adds [`Dots`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html) at the
        vertices if `add_vertex_dots` is set to `True`.

        Parameters:
        :   - **x\_values** (*Iterable**[**float**]*) – Iterable of values along the x-axis.
            - **y\_values** (*Iterable**[**float**]*) – Iterable of values along the y-axis.
            - **z\_values** (*Iterable**[**float**]* *|* *None*) – Iterable of values (zeros if z\_values is None) along the z-axis.
            - **line\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html)) – Color for the line graph.
            - **add\_vertex\_dots** (*bool*) – Whether or not to add [`Dot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html) at each vertex.
            - **vertex\_dot\_radius** (*float*) – Radius for the [`Dot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html) at each vertex.
            - **vertex\_dot\_style** (*dict**[**str**,* *Any**]* *|* *None*) – Style arguments to be passed into [`Dot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html) at each vertex.
            - **kwargs** (*Any*) – Additional arguments to be passed into [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html).

        Returns:
        :   A VDict containing both the line and dots (if specified). The line can be accessed with: `line_graph["line_graph"]`.
            The dots can be accessed with: `line_graph["vertex_dots"]`.

        Return type:
        :   [`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html)

        Examples

        Example: LineGraphExample

        ![../_images/LineGraphExample-1.png](https://docs.manim.community/en/stable/_images/LineGraphExample-1.png)

        ```
        class LineGraphExample(Scene):
            def construct(self):
                plane = NumberPlane(
                    x_range = (0, 7),
                    y_range = (0, 5),
                    x_length = 7,
                    axis_config={"include_numbers": True},
                )
                plane.center()
                line_graph = plane.plot_line_graph(
                    x_values = [0, 1.5, 2, 2.8, 4, 6.25],
                    y_values = [1, 3, 2.25, 4, 2.5, 1.75],
                    line_color=GOLD_E,
                    vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
                    stroke_width = 4,
                )
                self.add(plane, line_graph)
        ```

    point\_to\_coords(*point*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html)
    :   Accepts a point from the scene and returns its coordinates with respect to the axes.

        Parameters:
        :   **point** (*Sequence**[**float**]*) – The point, i.e. `RIGHT` or `[0, 1, 0]`.
            Also accepts a list of points as `[RIGHT, [0, 1, 0]]`.

        Returns:
        :   The coordinates on the axes, i.e. `[4.0, 7.0]`.
            Or a list of coordinates if point is a list of points.

        Return type:
        :   np.ndarray[float]

        Examples

        Example: PointToCoordsExample

        ![../_images/PointToCoordsExample-1.png](https://docs.manim.community/en/stable/_images/PointToCoordsExample-1.png)

        ```
        class PointToCoordsExample(Scene):
            def construct(self):
                ax = Axes(x_range=[0, 10, 2]).add_coordinates()
                circ = Circle(radius=0.5).shift(UR * 2)

                # get the coordinates of the circle with respect to the axes
                coords = np.around(ax.point_to_coords(circ.get_right()), decimals=2)

                label = (
                    Matrix([[coords[0]], [coords[1]]]).scale(0.75).next_to(circ, RIGHT)
                )

                self.add(ax, circ, label, Dot(circ.get_right()))
        ```
