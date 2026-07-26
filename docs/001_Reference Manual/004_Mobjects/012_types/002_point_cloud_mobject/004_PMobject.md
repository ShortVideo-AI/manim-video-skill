---
{
  "title": "PMobject",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "types",
    "point_cloud_mobject",
    "PMobject"
  ],
  "scraped_at": "2026-07-10T16:00:30"
}
---

# PMobject

Qualified name: `manim.mobject.types.point\_cloud\_mobject.PMobject`

class PMobject(*stroke\_width=4*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html)
:   Bases: [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)

    A disc made of a cloud of Dots

    Examples

    Example: PMobjectExample

    ![../_images/PMobjectExample-1.png](https://docs.manim.community/en/stable/_images/PMobjectExample-1.png)

    ```
    class PMobjectExample(Scene):
        def construct(self):

            pG = PGroup()  # This is just a collection of PMobject's

            # As the scale factor increases, the number of points
            # removed increases.
            for sf in range(1, 9 + 1):
                p = PointCloudDot(density=20, radius=1).thin_out(sf)
                # PointCloudDot is a type of PMobject
                # and can therefore be added to a PGroup
                pG.add(p)

            # This organizes all the shapes in a grid.
            pG.arrange_in_grid()

            self.add(pG)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`add_points`](#manim.mobject.types.point_cloud_mobject.PMobject.add_points) | Add points. |
    | `align_points_with_larger` |  |
    | `fade_to` |  |
    | `filter_out` |  |
    | `get_all_rgbas` |  |
    | `get_array_attrs` |  |
    | [`get_color`](#manim.mobject.types.point_cloud_mobject.PMobject.get_color) | Returns the color of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) |
    | [`get_mobject_type_class`](#manim.mobject.types.point_cloud_mobject.PMobject.get_mobject_type_class) | Return the base class of this mobject type. |
    | [`get_point_mobject`](#manim.mobject.types.point_cloud_mobject.PMobject.get_point_mobject) | The simplest [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) to be transformed to or from self. |
    | `get_stroke_width` |  |
    | `ingest_submobjects` |  |
    | `interpolate_color` |  |
    | `match_colors` |  |
    | `point_from_proportion` |  |
    | `pointwise_become_partial` |  |
    | [`reset_points`](#manim.mobject.types.point_cloud_mobject.PMobject.reset_points) | Sets `points` to be an empty array. |
    | [`set_color`](#manim.mobject.types.point_cloud_mobject.PMobject.set_color) | Condition is function which takes in one arguments, (x, y, z). |
    | [`set_color_by_gradient`](#manim.mobject.types.point_cloud_mobject.PMobject.set_color_by_gradient) |  |
    | `set_colors_by_radial_gradient` |  |
    | `set_stroke_width` |  |
    | [`sort_points`](#manim.mobject.types.point_cloud_mobject.PMobject.sort_points) | Function is any map from R^3 to R |
    | [`thin_out`](#manim.mobject.types.point_cloud_mobject.PMobject.thin_out) | Removes all but every nth point for n = factor |

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `depth` | The depth of the mobject. |
    | `height` | The height of the mobject. |
    | `width` | The width of the mobject. |

    Parameters:
    :   - **stroke\_width** (*int*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*stroke\_width=4*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **stroke\_width** (*int*)
            - **kwargs** (*Any*)

        Return type:
        :   None

    add\_points(*points*, *rgbas=None*, *color=None*, *alpha=1.0*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html)
    :   Add points.

        Points must be a Nx3 numpy array.
        Rgbas must be a Nx4 numpy array if it is not None.

        Parameters:
        :   - **points** ([*Point3DLike\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **rgbas** ([*FloatRGBALike\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* *None*)
            - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*)
            - **alpha** (*float*)

        Return type:
        :   Self

    get\_color()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html)
    :   Returns the color of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)

        Examples

        Return type:
        :   [*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)

    static get\_mobject\_type\_class()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html)
    :   Return the base class of this mobject type.

        Return type:
        :   type[[*PMobject*](#manim.mobject.types.point_cloud_mobject.PMobject)]

    get\_point\_mobject(*center=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html)
    :   The simplest [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) to be transformed to or from self.
        Should by a point of the appropriate type

        Parameters:
        :   **center** (*TypeAliasForwardRef**(**'~manim.typing.Point3DLike'**)* *|* *None*)

        Return type:
        :   [*Point*](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.Point.html)

    reset\_points()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html)
    :   Sets `points` to be an empty array.

        Return type:
        :   Self

    set\_color(*color=ManimColor('#FFFF00')*, *family=True*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html)
    :   Condition is function which takes in one arguments, (x, y, z).
        Here it just recurses to submobjects, but in subclasses this
        should be further implemented based on the the inner workings
        of color

        Parameters:
        :   - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
            - **family** (*bool*)

        Return type:
        :   Self

    set\_color\_by\_gradient(*\*colors*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html)
    :   Parameters:
        :   - **colors** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html)) – The colors to use for the gradient. Use like set\_color\_by\_gradient(RED, BLUE, GREEN).
            - **ManimColor.parse****(****color****)** (*self.color =*)
            - **self** (*return*)

        Return type:
        :   Self

    sort\_points(*function=<function PMobject.<lambda>>*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html)
    :   Function is any map from R^3 to R

        Parameters:
        :   **function** (*Callable**[**[**npt.NDArray**[*[*ManimFloat*](https://docs.manim.community/en/stable/reference/manim.typing.html)*]**]**,* *float**]*)

        Return type:
        :   Self

    thin\_out(*factor=5*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html)
    :   Removes all but every nth point for n = factor

        Parameters:
        :   **factor** (*int*)

        Return type:
        :   Self
