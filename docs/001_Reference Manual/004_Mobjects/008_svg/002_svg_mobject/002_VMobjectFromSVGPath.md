---
{
  "title": "VMobjectFromSVGPath",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "svg",
    "svg_mobject",
    "VMobjectFromSVGPath"
  ],
  "scraped_at": "2026-07-10T15:59:55"
}
---

# VMobjectFromSVGPath

Qualified name: `manim.mobject.svg.svg\_mobject.VMobjectFromSVGPath`

class VMobjectFromSVGPath(*path\_obj*, *long\_lines=False*, *should\_subdivide\_sharp\_curves=False*, *should\_remove\_null\_curves=False*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/svg/svg_mobject.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    A vectorized mobject representing an SVG path.

    Note

    The `long_lines`, `should_subdivide_sharp_curves`,
    and `should_remove_null_curves` keyword arguments are
    only respected with the OpenGL renderer.

    Parameters:
    :   - **path\_obj** (*se.Path*) – A parsed SVG path object.
        - **long\_lines** (*bool*) – Whether or not straight lines in the vectorized mobject
          are drawn in one or two segments.
        - **should\_subdivide\_sharp\_curves** (*bool*) – Whether or not to subdivide subcurves further in case
          two segments meet at an angle that is sharper than a
          given threshold.
        - **should\_remove\_null\_curves** (*bool*) – Whether or not to remove subcurves of length 0.
        - **kwargs** (*Any*) – Further keyword arguments are passed to the parent
          class.

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.generate_points) | Initializes `points` and therefore the shape. |
    | `handle_commands` |  |
    | `init_points` |  |

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

    \_original\_\_init\_\_(*path\_obj*, *long\_lines=False*, *should\_subdivide\_sharp\_curves=False*, *should\_remove\_null\_curves=False*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **path\_obj** (*Path*)
            - **long\_lines** (*bool*)
            - **should\_subdivide\_sharp\_curves** (*bool*)
            - **should\_remove\_null\_curves** (*bool*)
            - **kwargs** (*Any*)

    generate\_points()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/svg/svg_mobject.html)
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   None
