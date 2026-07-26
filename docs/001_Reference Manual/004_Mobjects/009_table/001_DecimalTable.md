---
{
  "title": "DecimalTable",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.table.DecimalTable.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "table",
    "DecimalTable"
  ],
  "scraped_at": "2026-07-10T15:59:57"
}
---

# DecimalTable

Qualified name: `manim.mobject.table.DecimalTable`

class DecimalTable(*table*, *element\_to\_mobject=<class 'manim.mobject.text.numbers.DecimalNumber'>*, *element\_to\_mobject\_config={'num\_decimal\_places': 1}*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
:   Bases: [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html)

    A specialized [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html) mobject for use with [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html) to display decimal entries.

    Examples

    Example: DecimalTableExample

    ![../_images/DecimalTableExample-1.png](https://docs.manim.community/en/stable/_images/DecimalTableExample-1.png)

    ```
    class DecimalTableExample(Scene):
        def construct(self):
            x_vals = [-2,-1,0,1,2]
            y_vals = np.exp(x_vals)
            t0 = DecimalTable(
                [x_vals, y_vals],
                row_labels=[MathTex("x"), MathTex("f(x)=e^{x}")],
                h_buff=1,
                element_to_mobject_config={"num_decimal_places": 2})
            self.add(t0)
    ```

    Special case of [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html) with `element_to_mobject` set to [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html).
    By default, `num_decimal_places` is set to 1.
    Will round/truncate the decimal places based on the provided `element_to_mobject_config`.

    Parameters:
    :   - **table** (*Iterable**[**Iterable**[**float* *|* *str**]**]*) – A 2D array, or a list of lists. Content of the table must be valid input
          for [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html).
        - **element\_to\_mobject** (*Callable**[**[**float* *|* *str**]**,* [*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]*) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) class applied to the table entries. Set as [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html).
        - **element\_to\_mobject\_config** (*dict*) – Element to mobject config, here set as {“num\_decimal\_places”: 1}.
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

    \_original\_\_init\_\_(*table*, *element\_to\_mobject=<class 'manim.mobject.text.numbers.DecimalNumber'>*, *element\_to\_mobject\_config={'num\_decimal\_places': 1}*, *\*\*kwargs*)
    :   Special case of [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html) with `element_to_mobject` set to [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html).
        By default, `num_decimal_places` is set to 1.
        Will round/truncate the decimal places based on the provided `element_to_mobject_config`.

        Parameters:
        :   - **table** (*Iterable**[**Iterable**[**float* *|* *str**]**]*) – A 2D array, or a list of lists. Content of the table must be valid input
              for [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html).
            - **element\_to\_mobject** (*Callable**[**[**float* *|* *str**]**,* [*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]*) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) class applied to the table entries. Set as [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html).
            - **element\_to\_mobject\_config** (*dict*) – Element to mobject config, here set as {“num\_decimal\_places”: 1}.
            - **kwargs** – Additional arguments to be passed to [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html).
