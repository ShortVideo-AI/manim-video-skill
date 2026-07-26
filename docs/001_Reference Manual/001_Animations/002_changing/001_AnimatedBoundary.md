---
{
  "title": "AnimatedBoundary",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.changing.AnimatedBoundary.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "changing",
    "AnimatedBoundary"
  ],
  "scraped_at": "2026-07-10T15:57:35"
}
---

# AnimatedBoundary

Qualified name: `manim.animation.changing.AnimatedBoundary`

class AnimatedBoundary(*vmobject, colors=[ManimColor('#29ABCA'), ManimColor('#9CDCEB'), ManimColor('#236B8E'), ManimColor('#736357')], max\_stroke\_width=3, cycle\_rate=0.5, back\_and\_forth=True, draw\_rate\_func=<function smooth>, fade\_rate\_func=<function smooth>, \*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/changing.html)
:   Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    Boundary of a [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) with animated color change.

    Examples

    Example: AnimatedBoundaryExample

    [
    ](./AnimatedBoundaryExample-1.mp4)

    ```
    class AnimatedBoundaryExample(Scene):
        def construct(self):
            text = Text("So shiny!")
            boundary = AnimatedBoundary(text, colors=[RED, GREEN, BLUE],
                                        cycle_rate=3)
            self.add(text, boundary)
            self.wait(2)
    ```

    Methods

    |  |  |
    | --- | --- |
    | `full_family_become_partial` |  |
    | `update_boundary_copies` |  |

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
    :   - **vmobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))
        - **colors** (*Sequence**[*[*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html)*]*)
        - **max\_stroke\_width** (*float*)
        - **cycle\_rate** (*float*)
        - **back\_and\_forth** (*bool*)
        - **draw\_rate\_func** ([*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html))
        - **fade\_rate\_func** ([*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html))
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*vmobject, colors=[ManimColor('#29ABCA'), ManimColor('#9CDCEB'), ManimColor('#236B8E'), ManimColor('#736357')], max\_stroke\_width=3, cycle\_rate=0.5, back\_and\_forth=True, draw\_rate\_func=<function smooth>, fade\_rate\_func=<function smooth>, \*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **vmobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))
            - **colors** (*Sequence**[**TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)**]*)
            - **max\_stroke\_width** (*float*)
            - **cycle\_rate** (*float*)
            - **back\_and\_forth** (*bool*)
            - **draw\_rate\_func** ([*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html))
            - **fade\_rate\_func** ([*RateFunction*](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html))
            - **kwargs** (*Any*)
