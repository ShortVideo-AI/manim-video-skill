---
{
  "title": "VMobject",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "types",
    "vectorized_mobject",
    "VMobject"
  ],
  "scraped_at": "2026-07-10T16:00:37"
}
---

# VMobject

Qualified name: `manim.mobject.types.vectorized\_mobject.VMobject`

class VMobject(*fill\_color=None*, *fill\_opacity=0.0*, *stroke\_color=None*, *stroke\_opacity=1.0*, *stroke\_width=4*, *background\_stroke\_color=ManimColor('#000000')*, *background\_stroke\_opacity=1.0*, *background\_stroke\_width=0*, *sheen\_factor=0.0*, *joint\_type=None*, *sheen\_direction=array([-1., 1., 0.])*, *close\_new\_points=False*, *pre\_function\_handle\_to\_anchor\_scale\_factor=0.01*, *make\_smooth\_after\_applying\_functions=False*, *background\_image=None*, *shade\_in\_3d=False*, *tolerance\_for\_point\_equality=1e-06*, *n\_points\_per\_cubic\_curve=4*, *cap\_style=CapStyleType.AUTO*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
:   Bases: [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)

    A vectorized mobject.

    Parameters:
    :   - **background\_stroke\_color** ([*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)) – The purpose of background stroke is to have something
          that won’t overlap fill, e.g. For text against some
          textured background.
        - **sheen\_factor** (*float*) – When a color c is set, there will be a second color
          computed based on interpolating c to WHITE by with
          sheen\_factor, and the display will gradient to this
          secondary color in the direction of sheen\_direction.
        - **close\_new\_points** (*bool*) – Indicates that it will not be displayed, but
          that it should count in parent mobject’s path
        - **tolerance\_for\_point\_equality** (*float*) – This is within a pixel
        - **joint\_type** ([*LineJointType*](https://docs.manim.community/en/stable/reference/manim.constants.LineJointType.html)) – The line joint type used to connect the curve segments
          of this vectorized mobject. See [`LineJointType`](https://docs.manim.community/en/stable/reference/manim.constants.LineJointType.html)
          for options.
        - **fill\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*)
        - **fill\_opacity** (*float*)
        - **stroke\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*)
        - **stroke\_opacity** (*float*)
        - **stroke\_width** (*float*)
        - **background\_stroke\_opacity** (*float*)
        - **background\_stroke\_width** (*float*)
        - **sheen\_direction** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **pre\_function\_handle\_to\_anchor\_scale\_factor** (*float*)
        - **make\_smooth\_after\_applying\_functions** (*bool*)
        - **background\_image** (*Image* *|* *str* *|* *None*)
        - **shade\_in\_3d** (*bool*)
        - **n\_points\_per\_cubic\_curve** (*int*)
        - **cap\_style** ([*CapStyleType*](https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html))
        - **kwargs** (*Any*)

    Methods

    |  |  |
    | --- | --- |
    | `add_cubic_bezier_curve` |  |
    | [`add_cubic_bezier_curve_to`](#manim.mobject.types.vectorized_mobject.VMobject.add_cubic_bezier_curve_to) | Add cubic bezier curve to the path. |
    | `add_cubic_bezier_curves` |  |
    | [`add_line_to`](#manim.mobject.types.vectorized_mobject.VMobject.add_line_to) | Add a straight line from the last point of VMobject to the given point. |
    | [`add_points_as_corners`](#manim.mobject.types.vectorized_mobject.VMobject.add_points_as_corners) | Append multiple straight lines at the end of `VMobject.points`, which connect the given `points` in order starting from the end of the current path. |
    | [`add_quadratic_bezier_curve_to`](#manim.mobject.types.vectorized_mobject.VMobject.add_quadratic_bezier_curve_to) | Add Quadratic bezier curve to the path. |
    | [`add_smooth_curve_to`](#manim.mobject.types.vectorized_mobject.VMobject.add_smooth_curve_to) | Creates a smooth curve from given points and add it to the VMobject. |
    | `add_subpath` |  |
    | [`align_points`](#manim.mobject.types.vectorized_mobject.VMobject.align_points) | Adds points to self and vmobject so that they both have the same number of subpaths, with corresponding subpaths each containing the same number of points. |
    | `align_rgbas` |  |
    | [`append_points`](#manim.mobject.types.vectorized_mobject.VMobject.append_points) | Append the given `new_points` to the end of `VMobject.points`. |
    | `append_vectorized_mobject` |  |
    | `apply_function` |  |
    | [`change_anchor_mode`](#manim.mobject.types.vectorized_mobject.VMobject.change_anchor_mode) | Changes the anchor mode of the bezier curves. |
    | `clear_points` |  |
    | `close_path` |  |
    | `color_using_background_image` |  |
    | `consider_points_equals` |  |
    | [`consider_points_equals_2d`](#manim.mobject.types.vectorized_mobject.VMobject.consider_points_equals_2d) | Determine if two points are close enough to be considered equal. |
    | `fade` |  |
    | [`force_direction`](#manim.mobject.types.vectorized_mobject.VMobject.force_direction) | Makes sure that points are either directed clockwise or counterclockwise. |
    | [`gen_cubic_bezier_tuples_from_points`](#manim.mobject.types.vectorized_mobject.VMobject.gen_cubic_bezier_tuples_from_points) | Returns the bezier tuples from an array of points. |
    | `gen_subpaths_from_points_2d` |  |
    | [`generate_rgbas_array`](#manim.mobject.types.vectorized_mobject.VMobject.generate_rgbas_array) | First arg can be either a color, or a tuple/list of colors. |
    | [`get_anchors`](#manim.mobject.types.vectorized_mobject.VMobject.get_anchors) | Returns the anchors of the curves forming the VMobject. |
    | [`get_anchors_and_handles`](#manim.mobject.types.vectorized_mobject.VMobject.get_anchors_and_handles) | Returns anchors1, handles1, handles2, anchors2, where (anchors1[i], handles1[i], handles2[i], anchors2[i]) will be four points defining a cubic bezier curve for any i in range(0, len(anchors1)) |
    | [`get_arc_length`](#manim.mobject.types.vectorized_mobject.VMobject.get_arc_length) | Return the approximated length of the whole curve. |
    | `get_background_image` |  |
    | [`get_color`](#manim.mobject.types.vectorized_mobject.VMobject.get_color) | Returns the color of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) |
    | `get_cubic_bezier_tuples` |  |
    | `get_cubic_bezier_tuples_from_points` |  |
    | [`get_curve_functions`](#manim.mobject.types.vectorized_mobject.VMobject.get_curve_functions) | Gets the functions for the curves of the mobject. |
    | [`get_curve_functions_with_lengths`](#manim.mobject.types.vectorized_mobject.VMobject.get_curve_functions_with_lengths) | Gets the functions and lengths of the curves for the mobject. |
    | [`get_direction`](#manim.mobject.types.vectorized_mobject.VMobject.get_direction) | Uses [`shoelace_direction()`](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html) to calculate the direction. |
    | [`get_end_anchors`](#manim.mobject.types.vectorized_mobject.VMobject.get_end_anchors) | Return the end anchors of the bezier curves. |
    | [`get_fill_color`](#manim.mobject.types.vectorized_mobject.VMobject.get_fill_color) | If there are multiple colors (for gradient) this returns the first one |
    | `get_fill_colors` |  |
    | `get_fill_opacities` |  |
    | [`get_fill_opacity`](#manim.mobject.types.vectorized_mobject.VMobject.get_fill_opacity) | If there are multiple opacities, this returns the first |
    | `get_fill_rgbas` |  |
    | `get_gradient_start_and_end_points` |  |
    | `get_group_class` |  |
    | `get_last_point` |  |
    | [`get_mobject_type_class`](#manim.mobject.types.vectorized_mobject.VMobject.get_mobject_type_class) | Return the base class of this mobject type. |
    | [`get_nth_curve_function`](#manim.mobject.types.vectorized_mobject.VMobject.get_nth_curve_function) | Returns the expression of the nth curve. |
    | [`get_nth_curve_function_with_length`](#manim.mobject.types.vectorized_mobject.VMobject.get_nth_curve_function_with_length) | Returns the expression of the nth curve along with its (approximate) length. |
    | [`get_nth_curve_length`](#manim.mobject.types.vectorized_mobject.VMobject.get_nth_curve_length) | Returns the (approximate) length of the nth curve. |
    | [`get_nth_curve_length_pieces`](#manim.mobject.types.vectorized_mobject.VMobject.get_nth_curve_length_pieces) | Returns the array of short line lengths used for length approximation. |
    | [`get_nth_curve_points`](#manim.mobject.types.vectorized_mobject.VMobject.get_nth_curve_points) | Returns the points defining the nth curve of the vmobject. |
    | [`get_num_curves`](#manim.mobject.types.vectorized_mobject.VMobject.get_num_curves) | Returns the number of curves of the vmobject. |
    | [`get_point_mobject`](#manim.mobject.types.vectorized_mobject.VMobject.get_point_mobject) | The simplest [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) to be transformed to or from self. |
    | `get_points_defining_boundary` |  |
    | `get_sheen_direction` |  |
    | `get_sheen_factor` |  |
    | [`get_start_anchors`](#manim.mobject.types.vectorized_mobject.VMobject.get_start_anchors) | Returns the start anchors of the bezier curves. |
    | `get_stroke_color` |  |
    | `get_stroke_colors` |  |
    | `get_stroke_opacities` |  |
    | `get_stroke_opacity` |  |
    | `get_stroke_rgbas` |  |
    | `get_stroke_width` |  |
    | `get_style` |  |
    | [`get_subcurve`](#manim.mobject.types.vectorized_mobject.VMobject.get_subcurve) | Returns the subcurve of the VMobject between the interval [a, b]. |
    | [`get_subpaths`](#manim.mobject.types.vectorized_mobject.VMobject.get_subpaths) | Returns subpaths formed by the curves of the VMobject. |
    | `get_subpaths_from_points` |  |
    | `has_new_path_started` |  |
    | [`init_colors`](#manim.mobject.types.vectorized_mobject.VMobject.init_colors) | Initializes the colors. |
    | [`insert_n_curves`](#manim.mobject.types.vectorized_mobject.VMobject.insert_n_curves) | Inserts n curves to the bezier curves of the vmobject. |
    | [`insert_n_curves_to_point_list`](#manim.mobject.types.vectorized_mobject.VMobject.insert_n_curves_to_point_list) | Given an array of k points defining a bezier curves (anchors and handles), returns points defining exactly k + n bezier curves. |
    | `interpolate_color` |  |
    | `is_closed` |  |
    | `make_jagged` |  |
    | `make_smooth` |  |
    | `match_background_image` |  |
    | `match_style` |  |
    | [`point_from_proportion`](#manim.mobject.types.vectorized_mobject.VMobject.point_from_proportion) | Gets the point at a proportion along the path of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject). |
    | [`pointwise_become_partial`](#manim.mobject.types.vectorized_mobject.VMobject.pointwise_become_partial) | Given a 2nd [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject) `vmobject`, a lower bound `a` and an upper bound `b`, modify this [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)'s points to match the portion of the Bézier spline described by `vmobject.points` with the parameter `t` between `a` and `b`. |
    | [`proportion_from_point`](#manim.mobject.types.vectorized_mobject.VMobject.proportion_from_point) | Returns the proportion along the path of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject) a particular given point is at. |
    | [`resize_points`](#manim.mobject.types.vectorized_mobject.VMobject.resize_points) | Resize the array of anchor points and handles to have the specified size. |
    | [`reverse_direction`](#manim.mobject.types.vectorized_mobject.VMobject.reverse_direction) | Reverts the point direction by inverting the point order. |
    | [`rotate`](#manim.mobject.types.vectorized_mobject.VMobject.rotate) | Rotates the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) around a specified axis and point. |
    | [`rotate_sheen_direction`](#manim.mobject.types.vectorized_mobject.VMobject.rotate_sheen_direction) | Rotates the direction of the applied sheen. |
    | [`scale`](#manim.mobject.types.vectorized_mobject.VMobject.scale) | Scale the size by a factor. |
    | [`scale_handle_to_anchor_distances`](#manim.mobject.types.vectorized_mobject.VMobject.scale_handle_to_anchor_distances) | If the distance between a given handle point H and its associated anchor point A is d, then it changes H to be a distances factor\*d away from A, but so that the line from A to H doesn't change. |
    | [`set_anchors_and_handles`](#manim.mobject.types.vectorized_mobject.VMobject.set_anchors_and_handles) | Given two sets of anchors and handles, process them to set them as anchors and handles of the VMobject. |
    | `set_background_stroke` |  |
    | [`set_cap_style`](#manim.mobject.types.vectorized_mobject.VMobject.set_cap_style) | Sets the cap style of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject). |
    | [`set_color`](#manim.mobject.types.vectorized_mobject.VMobject.set_color) | Condition is function which takes in one arguments, (x, y, z). |
    | [`set_fill`](#manim.mobject.types.vectorized_mobject.VMobject.set_fill) | Set the fill color and fill opacity of a [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject). |
    | `set_opacity` |  |
    | `set_points` |  |
    | [`set_points_as_corners`](#manim.mobject.types.vectorized_mobject.VMobject.set_points_as_corners) | Given an array of points, set them as corners of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject). |
    | `set_points_smoothly` |  |
    | `set_shade_in_3d` |  |
    | [`set_sheen`](#manim.mobject.types.vectorized_mobject.VMobject.set_sheen) | Applies a color gradient from a direction. |
    | [`set_sheen_direction`](#manim.mobject.types.vectorized_mobject.VMobject.set_sheen_direction) | Sets the direction of the applied sheen. |
    | `set_stroke` |  |
    | `set_style` |  |
    | [`start_new_path`](#manim.mobject.types.vectorized_mobject.VMobject.start_new_path) | Append a `point` to the `VMobject.points`, which will be the beginning of a new Bézier curve in the path given by the points. |
    | `update_rgbas_array` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | [`fill_color`](#manim.mobject.types.vectorized_mobject.VMobject.fill_color) | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    \_assert\_valid\_submobjects(*submobjects*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Check that all submobjects are actually instances of
        `Mobject`, and that none of them is `self` (a
        `Mobject` cannot contain itself).

        This is an auxiliary function called when adding Mobjects to the
        `submobjects` list.

        This function is intended to be overridden by subclasses such as
        [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject), which should assert that only other VMobjects
        may be added into it.

        Parameters:
        :   **submobjects** (*Iterable**[*[*VMobject*](#manim.mobject.types.vectorized_mobject.VMobject)*]*) – The list containing values to validate.

        Returns:
        :   The Mobject itself.

        Return type:
        :   `Mobject`

        Raises:
        :   - **TypeError** – If any of the values in submobjects is not a `Mobject`.
            - **ValueError** – If there was an attempt to add a `Mobject` as its own
              submobject.

    \_gen\_subpaths\_from\_points(*points*, *filter\_func*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Given an array of points defining the bezier curves of the vmobject, return subpaths formed by these points.
        Here, Two bezier curves form a path if at least two of their anchors are evaluated True by the relation defined by filter\_func.

        The algorithm every bezier tuple (anchors and handles) in `self.points` (by regrouping each n elements, where
        n is the number of points per cubic curve)), and evaluate the relation between two anchors with filter\_func.
        NOTE : The filter\_func takes an int n as parameter, and will evaluate the relation between points[n] and points[n - 1]. This should probably be changed so
        the function takes two points as parameters.

        Parameters:
        :   - **points** ([*CubicBezierPath*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – points defining the bezier curve.
            - **filter\_func** (*Callable**[**[**int**]**,* *bool**]*) – Filter-func defining the relation.

        Returns:
        :   subpaths formed by the points.

        Return type:
        :   Iterable[[CubicSpline](https://docs.manim.community/en/stable/reference/manim.typing.html)]

    \_original\_\_init\_\_(*fill\_color=None*, *fill\_opacity=0.0*, *stroke\_color=None*, *stroke\_opacity=1.0*, *stroke\_width=4*, *background\_stroke\_color=ManimColor('#000000')*, *background\_stroke\_opacity=1.0*, *background\_stroke\_width=0*, *sheen\_factor=0.0*, *joint\_type=None*, *sheen\_direction=array([-1., 1., 0.])*, *close\_new\_points=False*, *pre\_function\_handle\_to\_anchor\_scale\_factor=0.01*, *make\_smooth\_after\_applying\_functions=False*, *background\_image=None*, *shade\_in\_3d=False*, *tolerance\_for\_point\_equality=1e-06*, *n\_points\_per\_cubic\_curve=4*, *cap\_style=CapStyleType.AUTO*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **fill\_color** (*TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)* *|* *None*)
            - **fill\_opacity** (*float*)
            - **stroke\_color** (*TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)* *|* *None*)
            - **stroke\_opacity** (*float*)
            - **stroke\_width** (*float*)
            - **background\_stroke\_color** (*TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)* *|* *None*)
            - **background\_stroke\_opacity** (*float*)
            - **background\_stroke\_width** (*float*)
            - **sheen\_factor** (*float*)
            - **joint\_type** ([*LineJointType*](https://docs.manim.community/en/stable/reference/manim.constants.LineJointType.html) *|* *None*)
            - **sheen\_direction** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **close\_new\_points** (*bool*)
            - **pre\_function\_handle\_to\_anchor\_scale\_factor** (*float*)
            - **make\_smooth\_after\_applying\_functions** (*bool*)
            - **background\_image** (*Image* *|* *str* *|* *None*)
            - **shade\_in\_3d** (*bool*)
            - **tolerance\_for\_point\_equality** (*float*)
            - **n\_points\_per\_cubic\_curve** (*int*)
            - **cap\_style** ([*CapStyleType*](https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html))
            - **kwargs** (*Any*)

    add\_cubic\_bezier\_curve\_to(*handle1*, *handle2*, *anchor*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Add cubic bezier curve to the path.

        NOTE : the first anchor is not a parameter as by default the end of the last sub-path!

        Parameters:
        :   - **handle1** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – first handle
            - **handle2** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – second handle
            - **anchor** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – anchor

        Returns:
        :   `self`

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

    add\_line\_to(*point*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Add a straight line from the last point of VMobject to the given point.

        Parameters:
        :   **point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The end of the straight line.

        Returns:
        :   `self`

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

    add\_points\_as\_corners(*points*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Append multiple straight lines at the end of
        `VMobject.points`, which connect the given `points` in order
        starting from the end of the current path. These `points` would be
        therefore the corners of the new polyline appended to the path.

        Parameters:
        :   **points** ([*Point3DLike\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – An array of 3D points representing the corners of the polyline to
            append to `VMobject.points`.

        Returns:
        :   The VMobject itself, after appending the straight lines to its
            path.

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

    add\_quadratic\_bezier\_curve\_to(*handle*, *anchor*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Add Quadratic bezier curve to the path.

        Returns:
        :   `self`

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

        Parameters:
        :   - **handle** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **anchor** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))

    add\_smooth\_curve\_to(*\*points*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Creates a smooth curve from given points and add it to the VMobject. If two points are passed in, the first is interpreted
        as a handle, the second as an anchor.

        Parameters:
        :   **points** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – Points (anchor and handle, or just anchor) to add a smooth curve from

        Returns:
        :   `self`

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

        Raises:
        :   **ValueError** – If 0 or more than 2 points are given.

    align\_points(*vmobject*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Adds points to self and vmobject so that they both have the same number of subpaths, with
        corresponding subpaths each containing the same number of points.

        Points are added either by subdividing curves evenly along the subpath, or by creating new subpaths consisting
        of a single point repeated.

        Parameters:
        :   **vmobject** ([*VMobject*](#manim.mobject.types.vectorized_mobject.VMobject)) – The object to align points with.

        Returns:
        :   `self`

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

        See also

        [`interpolate()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html), [`align_data()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)

    append\_points(*new\_points*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Append the given `new_points` to the end of
        `VMobject.points`.

        Parameters:
        :   **new\_points** ([*Point3DLike\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – An array of 3D points to append.

        Returns:
        :   The VMobject itself, after appending `new_points`.

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

    change\_anchor\_mode(*mode*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Changes the anchor mode of the bezier curves. This will modify the handles.

        There can be only two modes, “jagged”, and “smooth”.

        Returns:
        :   `self`

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

        Parameters:
        :   **mode** (*Literal**[**'jagged'**,* *'smooth'**]*)

    consider\_points\_equals\_2d(*p0*, *p1*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Determine if two points are close enough to be considered equal.

        This uses the algorithm from np.isclose(), but expanded here for the
        2D point case. NumPy is overkill for such a small question.
        :param p0: first point
        :param p1: second point

        Returns:
        :   whether two points considered close.

        Return type:
        :   bool

        Parameters:
        :   - **p0** ([*Point2DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **p1** ([*Point2DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))

    property fill\_color: [ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)
    :   If there are multiple colors (for gradient)
        this returns the first one

    force\_direction(*target\_direction*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Makes sure that points are either directed clockwise or
        counterclockwise.

        Parameters:
        :   **target\_direction** (*Literal**[**'CW'**,* *'CCW'**]*) – Either `"CW"` or `"CCW"`.

        Return type:
        :   Self

    gen\_cubic\_bezier\_tuples\_from\_points(*points*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Returns the bezier tuples from an array of points.

        self.points is a list of the anchors and handles of the bezier curves of the mobject (ie [anchor1, handle1, handle2, anchor2, anchor3 ..])
        This algorithm basically retrieve them by taking an element every n, where n is the number of control points
        of the bezier curve.

        Parameters:
        :   **points** ([*CubicBezierPathLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – Points from which control points will be extracted.

        Returns:
        :   Bezier control points.

        Return type:
        :   tuple

    generate\_rgbas\_array(*color*, *opacity*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   First arg can be either a color, or a tuple/list of colors.
        Likewise, opacity can either be a float, or a tuple of floats.
        If self.sheen\_factor is not zero, and only
        one color was passed in, a second slightly light color
        will automatically be added for the gradient

        Parameters:
        :   - **color** (*TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)* *|* *Iterable**[*[*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)*]* *|* *None*)
            - **opacity** (*float* *|* *Iterable**[**float**]*)

        Return type:
        :   [*FloatRGBA*](https://docs.manim.community/en/stable/reference/manim.typing.html)

    get\_anchors()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Returns the anchors of the curves forming the VMobject.

        Returns:
        :   The anchors.

        Return type:
        :   [Point3D\_Array](https://docs.manim.community/en/stable/reference/manim.typing.html)

    get\_anchors\_and\_handles()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Returns anchors1, handles1, handles2, anchors2,
        where (anchors1[i], handles1[i], handles2[i], anchors2[i])
        will be four points defining a cubic bezier curve
        for any i in range(0, len(anchors1))

        Returns:
        :   Iterable of the anchors and handles.

        Return type:
        :   list[Point3D\_Array]

    get\_arc\_length(*sample\_points\_per\_curve=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Return the approximated length of the whole curve.

        Parameters:
        :   **sample\_points\_per\_curve** (*int* *|* *None*) – Number of sample points per curve used to approximate the length. More points result in a better approximation.

        Returns:
        :   The length of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).

        Return type:
        :   float

    get\_color()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Returns the color of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)

        Examples

        Return type:
        :   [*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)

    get\_curve\_functions()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Gets the functions for the curves of the mobject.

        Returns:
        :   The functions for the curves.

        Return type:
        :   Iterable[Callable[[float], [Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html)]]

    get\_curve\_functions\_with\_lengths(*\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Gets the functions and lengths of the curves for the mobject.

        Parameters:
        :   **\*\*kwargs** – The keyword arguments passed to [`get_nth_curve_function_with_length()`](#manim.mobject.types.vectorized_mobject.VMobject.get_nth_curve_function_with_length)

        Returns:
        :   The functions and lengths of the curves.

        Return type:
        :   Iterable[tuple[Callable[[float], [Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html)], float]]

    get\_direction()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Uses [`shoelace_direction()`](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html) to calculate the direction.
        The direction of points determines in which direction the
        object is drawn, clockwise or counterclockwise.

        Examples

        The default direction of a [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html) is counterclockwise:

        ```
        >>> from manim import Circle
        >>> Circle().get_direction()
        'CCW'
        ```

        Returns:
        :   Either `"CW"` or `"CCW"`.

        Return type:
        :   `str`

    get\_end\_anchors()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Return the end anchors of the bezier curves.

        Returns:
        :   Starting anchors

        Return type:
        :   [Point3D\_Array](https://docs.manim.community/en/stable/reference/manim.typing.html)

    get\_fill\_color()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   If there are multiple colors (for gradient)
        this returns the first one

        Return type:
        :   [*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)

    get\_fill\_opacity()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   If there are multiple opacities, this returns the
        first

        Return type:
        :   [*ManimFloat*](https://docs.manim.community/en/stable/reference/manim.typing.html)

    static get\_mobject\_type\_class()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Return the base class of this mobject type.

        Return type:
        :   type[[*VMobject*](#manim.mobject.types.vectorized_mobject.VMobject)]

    get\_nth\_curve\_function(*n*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Returns the expression of the nth curve.

        Parameters:
        :   **n** (*int*) – index of the desired curve.

        Returns:
        :   expression of the nth bezier curve.

        Return type:
        :   Callable[float, [Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html)]

    get\_nth\_curve\_function\_with\_length(*n*, *sample\_points=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Returns the expression of the nth curve along with its (approximate) length.

        Parameters:
        :   - **n** (*int*) – The index of the desired curve.
            - **sample\_points** (*int* *|* *None*) – The number of points to sample to find the length.

        Returns:
        :   - **curve** (*Callable[[float], Point3D]*) – The function for the nth curve.
            - **length** (`float`) – The length of the nth curve.

        Return type:
        :   tuple[*Callable*[[float], TypeAliasForwardRef(‘~manim.typing.Point3D’)], float]

    get\_nth\_curve\_length(*n*, *sample\_points=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Returns the (approximate) length of the nth curve.

        Parameters:
        :   - **n** (*int*) – The index of the desired curve.
            - **sample\_points** (*int* *|* *None*) – The number of points to sample to find the length.

        Returns:
        :   **length** – The length of the nth curve.

        Return type:
        :   `float`

    get\_nth\_curve\_length\_pieces(*n*, *sample\_points=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Returns the array of short line lengths used for length approximation.

        Parameters:
        :   - **n** (*int*) – The index of the desired curve.
            - **sample\_points** (*int* *|* *None*) – The number of points to sample to find the length.

        Return type:
        :   The short length-pieces of the nth curve.

    get\_nth\_curve\_points(*n*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Returns the points defining the nth curve of the vmobject.

        Parameters:
        :   **n** (*int*) – index of the desired bezier curve.

        Returns:
        :   points defining the nth bezier curve (anchors, handles)

        Return type:
        :   [CubicBezierPoints](https://docs.manim.community/en/stable/reference/manim.typing.html)

    get\_num\_curves()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Returns the number of curves of the vmobject.

        Returns:
        :   number of curves of the vmobject.

        Return type:
        :   int

    get\_point\_mobject(*center=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   The simplest [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) to be transformed to or from self.
        Should by a point of the appropriate type

        Parameters:
        :   **center** (*TypeAliasForwardRef**(**'~manim.typing.Point3DLike'**)* *|* *None*)

        Return type:
        :   [*VectorizedPoint*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VectorizedPoint.html)

    get\_start\_anchors()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Returns the start anchors of the bezier curves.

        Returns:
        :   Starting anchors

        Return type:
        :   [Point3D\_Array](https://docs.manim.community/en/stable/reference/manim.typing.html)

    get\_subcurve(*a*, *b*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Returns the subcurve of the VMobject between the interval [a, b].
        The curve is a VMobject itself.

        Parameters:
        :   - **a** (*float*) – The lower bound.
            - **b** (*float*) – The upper bound.

        Returns:
        :   The subcurve between of [a, b]

        Return type:
        :   [VMobject](#manim.mobject.types.vectorized_mobject.VMobject)

    get\_subpaths()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Returns subpaths formed by the curves of the VMobject.

        Subpaths are ranges of curves with each pair of consecutive curves having their end/start points coincident.

        Returns:
        :   subpaths.

        Return type:
        :   list[[CubicSpline](https://docs.manim.community/en/stable/reference/manim.typing.html)]

    init\_colors(*propagate\_colors=True*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Initializes the colors.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Parameters:
        :   **propagate\_colors** (*bool*)

        Return type:
        :   Self

    insert\_n\_curves(*n*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Inserts n curves to the bezier curves of the vmobject.

        Parameters:
        :   **n** (*int*) – Number of curves to insert.

        Returns:
        :   `self`

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

    insert\_n\_curves\_to\_point\_list(*n*, *points*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Given an array of k points defining a bezier curves (anchors and handles), returns points defining exactly k + n bezier curves.

        Parameters:
        :   - **n** (*int*) – Number of desired curves.
            - **points** ([*BezierPathLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – Starting points.

        Return type:
        :   Points generated.

    point\_from\_proportion(*alpha*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Gets the point at a proportion along the path of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).

        Parameters:
        :   **alpha** (*float*) – The proportion along the the path of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).

        Returns:
        :   The point on the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).

        Return type:
        :   `numpy.ndarray`

        Raises:
        :   - **ValueError** – If `alpha` is not between 0 and 1.
            - **Exception** – If the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject) has no points.

        Example

        Example: PointFromProportion

        ![../_images/PointFromProportion-1.png](https://docs.manim.community/en/stable/_images/PointFromProportion-1.png)

        ```
        class PointFromProportion(Scene):
            def construct(self):
                line = Line(2*DL, 2*UR)
                self.add(line)
                colors = (RED, BLUE, YELLOW)
                proportions = (1/4, 1/2, 3/4)
                for color, proportion in zip(colors, proportions):
                    self.add(Dot(color=color).move_to(
                            line.point_from_proportion(proportion)
                    ))
        ```

    pointwise\_become\_partial(*vmobject*, *a*, *b*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Given a 2nd [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject) `vmobject`, a lower bound `a` and
        an upper bound `b`, modify this [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)’s points to
        match the portion of the Bézier spline described by `vmobject.points`
        with the parameter `t` between `a` and `b`.

        Parameters:
        :   - **vmobject** ([*VMobject*](#manim.mobject.types.vectorized_mobject.VMobject)) – The [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject) that will serve as a model.
            - **a** (*float*) – The lower bound for `t`.
            - **b** (*float*) – The upper bound for `t`

        Returns:
        :   The [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject) itself, after the transformation.

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

        Raises:
        :   **TypeError** – If `vmobject` is not an instance of [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).

    proportion\_from\_point(*point*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Returns the proportion along the path of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)
        a particular given point is at.

        Parameters:
        :   **point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The Cartesian coordinates of the point which may or may not lie on the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

        Returns:
        :   The proportion along the path of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).

        Return type:
        :   float

        Raises:
        :   - **ValueError** – If `point` does not lie on the curve.
            - **Exception** – If the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject) has no points.

    resize\_points(*new\_length*, *resize\_func=<function resize\_array>*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Resize the array of anchor points and handles to have
        the specified size.

        Parameters:
        :   - **new\_length** (*int*) – The new (total) number of points.
            - **resize\_func** (*Callable**[**[*[*Point3D\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html)*,* *int**]**,* [*Point3D\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html)*]*) – A function mapping a Numpy array (the points) and an integer
              (the target size) to a Numpy array. The default implementation
              is based on Numpy’s `resize` function.

        Return type:
        :   Self

    reverse\_direction()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Reverts the point direction by inverting the point order.

        Returns:
        :   Returns self.

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

        Examples

        Example: ChangeOfDirection

        [
        ](./ChangeOfDirection-1.mp4)

        ```
        class ChangeOfDirection(Scene):
            def construct(self):
                ccw = RegularPolygon(5)
                ccw.shift(LEFT)
                cw = RegularPolygon(5)
                cw.shift(RIGHT).reverse_direction()

                self.play(Create(ccw), Create(cw),
                run_time=4)
        ```

    rotate(*angle*, *axis=array([0., 0., 1.])*, *\**, *about\_point=None*, *about\_edge=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Rotates the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) around a specified axis and point.

        Parameters:
        :   - **angle** (*float*) – The angle of rotation in radians. Predefined constants such as `DEGREES`
              can also be used to specify the angle in degrees.
            - **axis** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The rotation axis (see [`Rotating`](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotating.html) for more).
            - **about\_point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* *None*) – The point about which the mobject rotates. If `None`, rotation occurs around
              the center of the mobject.
            - **about\_edge** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* *None*) – The edge about which to apply the scaling.

        Returns:
        :   `self` (for method chaining)

        Return type:
        :   `Mobject`

        Note

        To animate a rotation, use [`Rotating`](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotating.html) or [`Rotate`](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotate.html)
        instead of `.animate.rotate(...)`.
        The `.animate.rotate(...)` syntax only applies a transformation
        from the initial state to the final rotated state
        (interpolation between the two states), without showing proper rotational motion
        based on the angle (from 0 to the given angle).

        Examples

        Example: RotateMethodExample

        ![../_images/RotateMethodExample-2.png](https://docs.manim.community/en/stable/_images/RotateMethodExample-2.png)

        ```
        class RotateMethodExample(Scene):
            def construct(self):
                circle = Circle(radius=1, color=BLUE)
                line = Line(start=ORIGIN, end=RIGHT)
                arrow1 = Arrow(start=ORIGIN, end=RIGHT, buff=0, color=GOLD)
                group1 = VGroup(circle, line, arrow1)

                group2 = group1.copy()
                arrow2 = group2[2]
                arrow2.rotate(angle=PI / 4, about_point=arrow2.get_start())

                group3 = group1.copy()
                arrow3 = group3[2]
                arrow3.rotate(angle=120 * DEGREES, about_point=arrow3.get_start())

                self.add(VGroup(group1, group2, group3).arrange(RIGHT, buff=1))
        ```

        See also

        [`Rotating`](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotating.html), [`Rotate`](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotate.html), [`animate`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html), `apply_points_function_about_point()`

    rotate\_sheen\_direction(*angle*, *axis=array([0., 0., 1.])*, *family=True*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Rotates the direction of the applied sheen.

        Parameters:
        :   - **angle** (*float*) – Angle by which the direction of sheen is rotated.
            - **axis** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – Axis of rotation.
            - **family** (*bool*)

        Return type:
        :   Self

        Examples

        Normal usage:

        ```
        Circle().set_sheen_direction(UP).rotate_sheen_direction(PI)
        ```

        See also

        [`set_sheen_direction()`](#manim.mobject.types.vectorized_mobject.VMobject.set_sheen_direction)

    scale(*scale\_factor*, *scale\_stroke=False*, *\**, *about\_point=None*, *about\_edge=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Scale the size by a factor.

        Default behavior is to scale about the center of the vmobject.

        Parameters:
        :   - **scale\_factor** (*float*) – The scaling factor \(\alpha\). If \(0 < |\alpha| < 1\), the mobject
              will shrink, and for \(|\alpha| > 1\) it will grow. Furthermore,
              if \(\alpha < 0\), the mobject is also flipped.
            - **scale\_stroke** (*bool*) – Boolean determining if the object’s outline is scaled when the object is scaled.
              If enabled, and object with 2px outline is scaled by a factor of .5, it will have an outline of 1px.
            - **kwargs** – Additional keyword arguments passed to
              [`scale()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).
            - **about\_point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* *None*)
            - **about\_edge** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* *None*)

        Returns:
        :   `self`

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

        Examples

        Example: MobjectScaleExample

        ![../_images/MobjectScaleExample-3.png](https://docs.manim.community/en/stable/_images/MobjectScaleExample-3.png)

        ```
        class MobjectScaleExample(Scene):
            def construct(self):
                c1 = Circle(1, RED).set_x(-1)
                c2 = Circle(1, GREEN).set_x(1)

                vg = VGroup(c1, c2)
                vg.set_stroke(width=50)
                self.add(vg)

                self.play(
                    c1.animate.scale(.25),
                    c2.animate.scale(.25,
                        scale_stroke=True)
                )
        ```

        See also

        `move_to()`

    scale\_handle\_to\_anchor\_distances(*factor*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   If the distance between a given handle point H and its associated
        anchor point A is d, then it changes H to be a distances factor\*d
        away from A, but so that the line from A to H doesn’t change.
        This is mostly useful in the context of applying a (differentiable)
        function, to preserve tangency properties. One would pull all the
        handles closer to their anchors, apply the function then push them out
        again.

        Parameters:
        :   **factor** (*float*) – The factor used for scaling.

        Returns:
        :   `self`

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

    set\_anchors\_and\_handles(*anchors1*, *handles1*, *handles2*, *anchors2*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Given two sets of anchors and handles, process them to set them as anchors
        and handles of the VMobject.

        anchors1[i], handles1[i], handles2[i] and anchors2[i] define the i-th bezier
        curve of the vmobject. There are four hardcoded parameters and this is a
        problem as it makes the number of points per cubic curve unchangeable from 4
        (two anchors and two handles).

        Returns:
        :   `self`

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

        Parameters:
        :   - **anchors1** ([*Point3DLike\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **handles1** ([*Point3DLike\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **handles2** ([*Point3DLike\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **anchors2** ([*Point3DLike\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html))

    set\_cap\_style(*cap\_style*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Sets the cap style of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).

        Parameters:
        :   **cap\_style** ([*CapStyleType*](https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html)) – The cap style to be set. See [`CapStyleType`](https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html) for options.

        Returns:
        :   `self`

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

        Examples

        Example: CapStyleExample

        ![../_images/CapStyleExample-1.png](https://docs.manim.community/en/stable/_images/CapStyleExample-1.png)

        ```
        class CapStyleExample(Scene):
            def construct(self):
                line = Line(LEFT, RIGHT, color=YELLOW, stroke_width=20)
                line.set_cap_style(CapStyleType.ROUND)
                self.add(line)
        ```

    set\_color(*color*, *family=True*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Condition is function which takes in one arguments, (x, y, z).
        Here it just recurses to submobjects, but in subclasses this
        should be further implemented based on the the inner workings
        of color

        Parameters:
        :   - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
            - **family** (*bool*)

        Return type:
        :   Self

    set\_fill(*color=None*, *opacity=None*, *family=True*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Set the fill color and fill opacity of a [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).

        Parameters:
        :   - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*) – Fill color of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).
            - **opacity** (*float* *|* *None*) – Fill opacity of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).
            - **family** (*bool*) – If `True`, the fill color of all submobjects is also set.

        Returns:
        :   `self`

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

        Examples

        Example: SetFill

        ![../_images/SetFill-1.png](https://docs.manim.community/en/stable/_images/SetFill-1.png)

        ```
        class SetFill(Scene):
            def construct(self):
                square = Square().scale(2).set_fill(WHITE,1)
                circle1 = Circle().set_fill(GREEN,0.8)
                circle2 = Circle().set_fill(YELLOW) # No fill_opacity
                circle3 = Circle().set_fill(color = '#FF2135', opacity = 0.2)
                group = Group(circle1,circle2,circle3).arrange()
                self.add(square)
                self.add(group)
        ```

        See also

        `set_style()`

    set\_points\_as\_corners(*points*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Given an array of points, set them as corners of the
        [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).

        To achieve that, this algorithm sets handles aligned with the anchors
        such that the resultant Bézier curve will be the segment between the
        two anchors.

        Parameters:
        :   **points** ([*Point3DLike\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – Array of points that will be set as corners.

        Returns:
        :   The VMobject itself, after setting the new points as corners.

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

        Examples

        Example: PointsAsCornersExample

        ![../_images/PointsAsCornersExample-1.png](https://docs.manim.community/en/stable/_images/PointsAsCornersExample-1.png)

        ```
        class PointsAsCornersExample(Scene):
            def construct(self):
                corners = (
                    # create square
                    UR, UL,
                    DL, DR,
                    UR,
                    # create crosses
                    DL, UL,
                    DR
                )
                vmob = VMobject(stroke_color=RED)
                vmob.set_points_as_corners(corners).scale(2)
                self.add(vmob)
        ```

    set\_sheen(*factor*, *direction=None*, *family=True*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Applies a color gradient from a direction.

        Parameters:
        :   - **factor** (*float*) – The extent of lustre/gradient to apply. If negative, the gradient
              starts from black, if positive the gradient starts from white and
              changes to the current color.
            - **direction** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* *None*) – Direction from where the gradient is applied.
            - **family** (*bool*)

        Return type:
        :   Self

        Examples

        Example: SetSheen

        ![../_images/SetSheen-1.png](https://docs.manim.community/en/stable/_images/SetSheen-1.png)

        ```
        class SetSheen(Scene):
            def construct(self):
                circle = Circle(fill_opacity=1).set_sheen(-0.3, DR)
                self.add(circle)
        ```

    set\_sheen\_direction(*direction*, *family=True*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Sets the direction of the applied sheen.

        Parameters:
        :   - **direction** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – Direction from where the gradient is applied.
            - **family** (*bool*)

        Return type:
        :   Self

        Examples

        Normal usage:

        ```
        Circle().set_sheen_direction(UP)
        ```

        See also

        [`set_sheen()`](#manim.mobject.types.vectorized_mobject.VMobject.set_sheen), [`rotate_sheen_direction()`](#manim.mobject.types.vectorized_mobject.VMobject.rotate_sheen_direction)

    start\_new\_path(*point*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
    :   Append a `point` to the `VMobject.points`, which will be the
        beginning of a new Bézier curve in the path given by the points. If
        there’s an unfinished curve at the end of `VMobject.points`,
        complete it by appending the last Bézier curve’s start anchor as many
        times as needed.

        Parameters:
        :   **point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – A 3D point to append to `VMobject.points`.

        Returns:
        :   The VMobject itself, after appending `point` and starting a new
            curve.

        Return type:
        :   [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)
