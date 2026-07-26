---
{
  "title": "DashedVMobject",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.DashedVMobject.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "types",
    "vectorized_mobject",
    "DashedVMobject"
  ],
  "scraped_at": "2026-07-10T16:00:33"
}
---

# DashedVMobject

Qualified name: `manim.mobject.types.vectorized\_mobject.DashedVMobject`

class DashedVMobject(*vmobject*, *num\_dashes=15*, *dashed\_ratio=0.5*, *dash\_offset=0*, *color=ManimColor('#FFFFFF')*, *equal\_lengths=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    A [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) composed of dashes instead of lines.

    Parameters:
    :   - **vmobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)) – The object that will get dashed
        - **num\_dashes** (*int*) – Number of dashes to add.
        - **dashed\_ratio** (*float*) – Ratio of dash to empty space.
        - **dash\_offset** (*float*) – Shifts the starting point of dashes along the
          path. Value 1 shifts by one full dash length.
        - **equal\_lengths** (*bool*) – If `True`, dashes will be (approximately) equally long.
          If `False`, dashes will be split evenly in the curve’s
          input t variable (legacy behavior).
        - **color** ([*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html))

    Examples

    Example: DashedVMobjectExample

    ![../_images/DashedVMobjectExample-1.png](https://docs.manim.community/en/stable/_images/DashedVMobjectExample-1.png)

    ```
    class DashedVMobjectExample(Scene):
        def construct(self):
            r = 0.5

            top_row = VGroup()  # Increasing num_dashes
            for dashes in range(1, 12):
                circ = DashedVMobject(Circle(radius=r, color=WHITE), num_dashes=dashes)
                top_row.add(circ)

            middle_row = VGroup()  # Increasing dashed_ratio
            for ratio in np.arange(1 / 11, 1, 1 / 11):
                circ = DashedVMobject(
                    Circle(radius=r, color=WHITE), dashed_ratio=ratio
                )
                middle_row.add(circ)

            func1 = FunctionGraph(lambda t: t**5,[-1,1],color=WHITE)
            func_even = DashedVMobject(func1,num_dashes=6,equal_lengths=True)
            func_stretched = DashedVMobject(func1, num_dashes=6, equal_lengths=False)
            bottom_row = VGroup(func_even,func_stretched)

            top_row.arrange(buff=0.3)
            middle_row.arrange()
            bottom_row.arrange(buff=1)
            everything = VGroup(top_row, middle_row, bottom_row).arrange(DOWN, buff=1)
            self.add(everything)
    ```

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

    \_original\_\_init\_\_(*vmobject*, *num\_dashes=15*, *dashed\_ratio=0.5*, *dash\_offset=0*, *color=ManimColor('#FFFFFF')*, *equal\_lengths=True*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **vmobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))
            - **num\_dashes** (*int*)
            - **dashed\_ratio** (*float*)
            - **dash\_offset** (*float*)
            - **color** ([*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html))
            - **equal\_lengths** (*bool*)

        Return type:
        :   None
