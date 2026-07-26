---
{
  "title": "IntegerTable",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.table.IntegerTable.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "table",
    "IntegerTable"
  ],
  "scraped_at": "2026-07-10T15:59:57"
}
---

# IntegerTable

Qualified name: `manim.mobject.table.IntegerTable`

class IntegerTable(*table*, *element\_to\_mobject=<class 'manim.mobject.text.numbers.Integer'>*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
:   Bases: [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html)

    A specialized [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html) mobject for use with [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html).

    Examples

    Example: IntegerTableExample

    ![../_images/IntegerTableExample-1.png](https://docs.manim.community/en/stable/_images/IntegerTableExample-1.png)

    ```
    class IntegerTableExample(Scene):
        def construct(self):
            t0 = IntegerTable(
                [[0,30,45,60,90],
                [90,60,45,30,0]],
                col_labels=[
                    MathTex(r"\frac{ \sqrt{0} }{2}"),
                    MathTex(r"\frac{ \sqrt{1} }{2}"),
                    MathTex(r"\frac{ \sqrt{2} }{2}"),
                    MathTex(r"\frac{ \sqrt{3} }{2}"),
                    MathTex(r"\frac{ \sqrt{4} }{2}")],
                row_labels=[MathTex(r"\sin"), MathTex(r"\cos")],
                h_buff=1,
                element_to_mobject_config={"unit": r"^{\circ}"})
            self.add(t0)
    ```

    Special case of [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html) with element\_to\_mobject set to [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html).
    Will round if there are decimal entries in the table.

    Parameters:
    :   - **table** (*Iterable**[**Iterable**[**float* *|* *str**]**]*) – A 2d array or list of lists. Content of the table has to be valid input
          for [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html).
        - **element\_to\_mobject** (*Callable**[**[**float* *|* *str**]**,* [*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]*) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) class applied to the table entries. Set as [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html).
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

    \_original\_\_init\_\_(*table*, *element\_to\_mobject=<class 'manim.mobject.text.numbers.Integer'>*, *\*\*kwargs*)
    :   Special case of [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html) with element\_to\_mobject set to [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html).
        Will round if there are decimal entries in the table.

        Parameters:
        :   - **table** (*Iterable**[**Iterable**[**float* *|* *str**]**]*) – A 2d array or list of lists. Content of the table has to be valid input
              for [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html).
            - **element\_to\_mobject** (*Callable**[**[**float* *|* *str**]**,* [*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]*) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) class applied to the table entries. Set as [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html).
            - **kwargs** – Additional arguments to be passed to [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html).
