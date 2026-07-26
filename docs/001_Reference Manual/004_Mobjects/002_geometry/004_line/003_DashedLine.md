---
{
  "title": "DashedLine",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.DashedLine.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "line",
    "DashedLine"
  ],
  "scraped_at": "2026-07-10T15:59:00"
}
---

# DashedLine

Qualified name: `manim.mobject.geometry.line.DashedLine`

class DashedLine(*\*args*, *dash\_length=0.05*, *dashed\_ratio=0.5*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
:   Bases: [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html)

    A dashed [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html).

    Parameters:
    :   - **args** (*Any*) – Arguments to be passed to [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html)
        - **dash\_length** (*float*) – The length of each individual dash of the line.
        - **dashed\_ratio** (*float*) – The ratio of dash space to empty space. Range of 0-1.
        - **kwargs** (*Any*) – Additional arguments to be passed to [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html)

    See also

    [`DashedVMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.DashedVMobject.html)

    Examples

    Example: DashedLineExample

    ![../_images/DashedLineExample-1.png](https://docs.manim.community/en/stable/_images/DashedLineExample-1.png)

    ```
    class DashedLineExample(Scene):
        def construct(self):
            # dash_length increased
            dashed_1 = DashedLine(config.left_side, config.right_side, dash_length=2.0).shift(UP*2)
            # normal
            dashed_2 = DashedLine(config.left_side, config.right_side)
            # dashed_ratio decreased
            dashed_3 = DashedLine(config.left_side, config.right_side, dashed_ratio=0.1).shift(DOWN*2)
            self.add(dashed_1, dashed_2, dashed_3)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`get_end`](#manim.mobject.geometry.line.DashedLine.get_end) | Returns the end point of the line. |
    | [`get_first_handle`](#manim.mobject.geometry.line.DashedLine.get_first_handle) | Returns the point of the first handle. |
    | [`get_last_handle`](#manim.mobject.geometry.line.DashedLine.get_last_handle) | Returns the point of the last handle. |
    | [`get_start`](#manim.mobject.geometry.line.DashedLine.get_start) | Returns the start point of the line. |

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

    \_calculate\_num\_dashes()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
    :   Returns the number of dashes in the dashed line.

        Examples

        ```
        >>> DashedLine()._calculate_num_dashes()
        20
        ```

        Return type:
        :   int

    \_original\_\_init\_\_(*\*args*, *dash\_length=0.05*, *dashed\_ratio=0.5*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **args** (*Any*)
            - **dash\_length** (*float*)
            - **dashed\_ratio** (*float*)
            - **kwargs** (*Any*)

        Return type:
        :   None

    get\_end()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
    :   Returns the end point of the line.

        Examples

        ```
        >>> DashedLine().get_end()
        array([1., 0., 0.])
        ```

        Return type:
        :   [*Point3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)

    get\_first\_handle()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
    :   Returns the point of the first handle.

        Examples

        Return type:
        :   [*Point3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)

    get\_last\_handle()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
    :   Returns the point of the last handle.

        Examples

        Return type:
        :   [*Point3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)

    get\_start()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html)
    :   Returns the start point of the line.

        Examples

        ```
        >>> DashedLine().get_start()
        array([-1.,  0.,  0.])
        ```

        Return type:
        :   [*Point3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)
