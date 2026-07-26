---
{
  "title": "MobjectTable",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.table.MobjectTable.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "table",
    "MobjectTable"
  ],
  "scraped_at": "2026-07-10T15:59:58"
}
---

# MobjectTable

Qualified name: `manim.mobject.table.MobjectTable`

class MobjectTable(*table*, *element\_to\_mobject=<function MobjectTable.<lambda>>*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
:   Bases: [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html)

    A specialized [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html) mobject for use with [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).

    Examples

    Example: MobjectTableExample

    ![../_images/MobjectTableExample-1.png](https://docs.manim.community/en/stable/_images/MobjectTableExample-1.png)

    ```
    class MobjectTableExample(Scene):
        def construct(self):
            cross = VGroup(
                Line(UP + LEFT, DOWN + RIGHT),
                Line(UP + RIGHT, DOWN + LEFT),
            )
            a = Circle().set_color(RED).scale(0.5)
            b = cross.set_color(BLUE).scale(0.5)
            t0 = MobjectTable(
                [[a.copy(),b.copy(),a.copy()],
                [b.copy(),a.copy(),a.copy()],
                [a.copy(),b.copy(),b.copy()]]
            )
            line = Line(
                t0.get_corner(DL), t0.get_corner(UR)
            ).set_color(RED)
            self.add(t0, line)
    ```

    Special case of [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html) with `element_to_mobject` set to an identity function.
    Here, every item in `table` must already be of type [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).

    Parameters:
    :   - **table** (*Iterable**[**Iterable**[*[*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]**]*) – A 2D array or list of lists. Content of the table must be of type [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).
        - **element\_to\_mobject** (*Callable**[**[*[*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]**,* [*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]*) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) class applied to the table entries. Set as `lambda m : m` to return itself.
        - **kwargs** – Additional arguments to be passed to [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html).

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

    \_original\_\_init\_\_(*table*, *element\_to\_mobject=<function MobjectTable.<lambda>>*, *\*\*kwargs*)
    :   Special case of [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html) with `element_to_mobject` set to an identity function.
        Here, every item in `table` must already be of type [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).

        Parameters:
        :   - **table** (*Iterable**[**Iterable**[*[*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]**]*) – A 2D array or list of lists. Content of the table must be of type [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).
            - **element\_to\_mobject** (*Callable**[**[*[*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]**,* [*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]*) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) class applied to the table entries. Set as `lambda m : m` to return itself.
            - **kwargs** – Additional arguments to be passed to [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html).
