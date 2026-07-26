---
{
  "title": "MathTexPart",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTexPart.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "text",
    "tex_mobject",
    "MathTexPart"
  ],
  "scraped_at": "2026-07-10T16:00:05"
}
---

# MathTexPart

Qualified name: `manim.mobject.text.tex\_mobject.MathTexPart`

class MathTexPart(*fill\_color=None*, *fill\_opacity=0.0*, *stroke\_color=None*, *stroke\_opacity=1.0*, *stroke\_width=4*, *background\_stroke\_color=ManimColor('#000000')*, *background\_stroke\_opacity=1.0*, *background\_stroke\_width=0*, *sheen\_factor=0.0*, *joint\_type=None*, *sheen\_direction=array([-1., 1., 0.])*, *close\_new\_points=False*, *pre\_function\_handle\_to\_anchor\_scale\_factor=0.01*, *make\_smooth\_after\_applying\_functions=False*, *background\_image=None*, *shade\_in\_3d=False*, *tolerance\_for\_point\_equality=1e-06*, *n\_points\_per\_cubic\_curve=4*, *cap\_style=CapStyleType.AUTO*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/tex_mobject.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

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
    | `tex_string` |  |

    Parameters:
    :   - **fill\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*)
        - **fill\_opacity** (*float*)
        - **stroke\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*)
        - **stroke\_opacity** (*float*)
        - **stroke\_width** (*float*)
        - **background\_stroke\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) *|* *None*)
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
