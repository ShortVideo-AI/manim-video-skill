---
{
  "title": "Brace",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.Brace.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "svg",
    "brace",
    "Brace"
  ],
  "scraped_at": "2026-07-10T15:59:52"
}
---

# Brace

Qualified name: `manim.mobject.svg.brace.Brace`

class Brace(*mobject*, *direction=array([0., -1., 0.])*, *buff=0.2*, *sharpness=2*, *stroke\_width=0*, *fill\_opacity=1.0*, *background\_stroke\_width=0*, *background\_stroke\_color=ManimColor('#000000')*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/svg/brace.html)
:   Bases: [`VMobjectFromSVGPath`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.html)

    Takes a mobject and draws a brace adjacent to it.

    Passing a direction vector determines the direction from which the
    brace is drawn. By default it is drawn from below.

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobject adjacent to which the brace is placed.
        - **direction** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The direction from which the brace faces the mobject.
        - **buff** (*float*)
        - **sharpness** (*float*)
        - **stroke\_width** (*float*)
        - **fill\_opacity** (*float*)
        - **background\_stroke\_width** (*float*)
        - **background\_stroke\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
        - **kwargs** (*Any*)

    See also

    [`BraceBetweenPoints`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html)

    Examples

    Example: BraceExample

    ![../_images/BraceExample-1.png](https://docs.manim.community/en/stable/_images/BraceExample-1.png)

    ```
    class BraceExample(Scene):
        def construct(self):
            s = Square()
            self.add(s)
            for i in np.linspace(0.1,1.0,4):
                br = Brace(s, sharpness=i)
                t = Text(f"sharpness= {i}").next_to(br, RIGHT)
                self.add(t)
                self.add(br)
            VGroup(*self.mobjects).arrange(DOWN, buff=0.2)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`get_direction`](#manim.mobject.svg.brace.Brace.get_direction) | Returns the direction from the center to the brace tip. |
    | [`get_tex`](#manim.mobject.svg.brace.Brace.get_tex) | Places the tex at the brace tip. |
    | [`get_text`](#manim.mobject.svg.brace.Brace.get_text) | Places the text at the brace tip. |
    | [`get_tip`](#manim.mobject.svg.brace.Brace.get_tip) | Returns the point at the brace tip. |
    | [`put_at_tip`](#manim.mobject.svg.brace.Brace.put_at_tip) | Puts the given mobject at the brace tip. |

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

    \_original\_\_init\_\_(*mobject*, *direction=array([0., -1., 0.])*, *buff=0.2*, *sharpness=2*, *stroke\_width=0*, *fill\_opacity=1.0*, *background\_stroke\_width=0*, *background\_stroke\_color=ManimColor('#000000')*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **direction** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **buff** (*float*)
            - **sharpness** (*float*)
            - **stroke\_width** (*float*)
            - **fill\_opacity** (*float*)
            - **background\_stroke\_width** (*float*)
            - **background\_stroke\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
            - **kwargs** (*Any*)

    get\_direction()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/svg/brace.html)
    :   Returns the direction from the center to the brace tip.

        Return type:
        :   [*Vector3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)

    get\_tex(*\*tex*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/svg/brace.html)
    :   Places the tex at the brace tip.

        Parameters:
        :   - **tex** (*str*) – The tex to be placed at the brace tip.
            - **kwargs** (*Any*) – Any further keyword arguments are passed to [`put_at_tip()`](#manim.mobject.svg.brace.Brace.put_at_tip) which
              is used to position the tex at the brace tip.

        Return type:
        :   [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html)

    get\_text(*\*text*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/svg/brace.html)
    :   Places the text at the brace tip.

        Parameters:
        :   - **text** (*str*) – The text to be placed at the brace tip.
            - **kwargs** (*Any*) – Any additional keyword arguments are passed to [`put_at_tip()`](#manim.mobject.svg.brace.Brace.put_at_tip) which
              is used to position the text at the brace tip.

        Return type:
        :   [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html)

    get\_tip()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/svg/brace.html)
    :   Returns the point at the brace tip.

        Return type:
        :   [*Point3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)

    put\_at\_tip(*mob*, *use\_next\_to=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/svg/brace.html)
    :   Puts the given mobject at the brace tip.

        Parameters:
        :   - **mob** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobject to be placed at the tip.
            - **use\_next\_to** (*bool*) – If true, then `next_to()` is used to place the mobject at the
              tip.
            - **kwargs** (*Any*) – Any additional keyword arguments are passed to `next_to()` which
              is used to put the mobject next to the brace tip.

        Return type:
        :   *Self*
