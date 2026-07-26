---
{
  "title": "ArcPolygon",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcPolygon.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "arc",
    "ArcPolygon"
  ],
  "scraped_at": "2026-07-10T15:58:46"
}
---

# ArcPolygon

Qualified name: `manim.mobject.geometry.arc.ArcPolygon`

class ArcPolygon(*\*vertices*, *angle=0.7853981633974483*, *radius=None*, *arc\_config=None*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    A generalized polygon allowing for points to be connected with arcs.

    This version tries to stick close to the way `Polygon` is used. Points
    can be passed to it directly which are used to generate the according arcs
    (using [`ArcBetweenPoints`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcBetweenPoints.html)). An angle or radius can be passed to it to
    use across all arcs, but to configure arcs individually an `arc_config` list
    has to be passed with the syntax explained below.

    Parameters:
    :   - **vertices** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – A list of vertices, start and end points for the arc segments.
        - **angle** (*float*) – The angle used for constructing the arcs. If no other parameters
          are set, this angle is used to construct all arcs.
        - **radius** (*float* *|* *None*) – The circle radius used to construct the arcs. If specified,
          overrides the specified `angle`.
        - **arc\_config** (*list**[**dict**]* *|* *None*) – When passing a `dict`, its content will be passed as keyword
          arguments to [`ArcBetweenPoints`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcBetweenPoints.html). Otherwise, a list
          of dictionaries containing values that are passed as keyword
          arguments for every individual arc can be passed.
        - **kwargs** (*Any*) – Further keyword arguments that are passed to the constructor of
          [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html).

    arcs
    :   The arcs created from the input parameters:

        Type:
        :   `list`

    Tip

    Two instances of [`ArcPolygon`](#manim.mobject.geometry.arc.ArcPolygon) can be transformed properly into one
    another as well. Be advised that any arc initialized with `angle=0`
    will actually be a straight line, so if a straight section should seamlessly
    transform into an arced section or vice versa, initialize the straight section
    with a negligible angle instead (such as `angle=0.0001`).

    Note

    There is an alternative version ([`ArcPolygonFromArcs`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcPolygonFromArcs.html)) that is instantiated
    with pre-defined arcs.

    See also

    [`ArcPolygonFromArcs`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcPolygonFromArcs.html)

    Examples

    Example: SeveralArcPolygons

    [
    ](./SeveralArcPolygons-1.mp4)

    ```
    class SeveralArcPolygons(Scene):
        def construct(self):
            a = [0, 0, 0]
            b = [2, 0, 0]
            c = [0, 2, 0]
            ap1 = ArcPolygon(a, b, c, radius=2)
            ap2 = ArcPolygon(a, b, c, angle=45*DEGREES)
            ap3 = ArcPolygon(a, b, c, arc_config={'radius': 1.7, 'color': RED})
            ap4 = ArcPolygon(a, b, c, color=RED, fill_opacity=1,
                                        arc_config=[{'radius': 1.7, 'color': RED},
                                        {'angle': 20*DEGREES, 'color': BLUE},
                                        {'radius': 1}])
            ap_group = VGroup(ap1, ap2, ap3, ap4).arrange()
            self.play(*[Create(ap) for ap in [ap1, ap2, ap3, ap4]])
            self.wait()
    ```

    For further examples see [`ArcPolygonFromArcs`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcPolygonFromArcs.html).

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

    \_original\_\_init\_\_(*\*vertices*, *angle=0.7853981633974483*, *radius=None*, *arc\_config=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **vertices** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **angle** (*float*)
            - **radius** (*float* *|* *None*)
            - **arc\_config** (*list**[**dict**]* *|* *None*)
            - **kwargs** (*Any*)

        Return type:
        :   None
