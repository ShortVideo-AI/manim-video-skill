---
{
  "title": "Table",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "table",
    "Table"
  ],
  "scraped_at": "2026-07-10T15:59:59"
}
---

# Table

Qualified name: `manim.mobject.table.Table`

class Table(*table*, *row\_labels=None*, *col\_labels=None*, *top\_left\_entry=None*, *v\_buff=0.8*, *h\_buff=1.3*, *include\_outer\_lines=False*, *add\_background\_rectangles\_to\_entries=False*, *entries\_background\_color=ManimColor('#000000')*, *include\_background\_rectangle=False*, *background\_rectangle\_color=ManimColor('#000000')*, *element\_to\_mobject=<class 'manim.mobject.text.text\_mobject.Paragraph'>*, *element\_to\_mobject\_config={}*, *arrange\_in\_grid\_config={}*, *line\_config={}*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
:   Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    A mobject that displays a table on the screen.

    Parameters:
    :   - **table** (*Iterable**[**Iterable**[**float* *|* *str* *|* [*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]**]*) – A 2D array or list of lists. Content of the table has to be a valid input
          for the callable set in `element_to_mobject`.
        - **row\_labels** (*Iterable**[*[*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]* *|* *None*) – List of [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) representing the labels of each row.
        - **col\_labels** (*Iterable**[*[*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]* *|* *None*) – List of [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) representing the labels of each column.
        - **top\_left\_entry** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* *None*) – The top-left entry of the table, can only be specified if row and
          column labels are given.
        - **v\_buff** (*float*) – Vertical buffer passed to [`arrange_in_grid()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html), by default 0.8.
        - **h\_buff** (*float*) – Horizontal buffer passed to [`arrange_in_grid()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html), by default 1.3.
        - **include\_outer\_lines** (*bool*) – `True` if the table should include outer lines, by default False.
        - **add\_background\_rectangles\_to\_entries** (*bool*) – `True` if background rectangles should be added to entries, by default `False`.
        - **entries\_background\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html)) – Background color of entries if `add_background_rectangles_to_entries` is `True`.
        - **include\_background\_rectangle** (*bool*) – `True` if the table should have a background rectangle, by default `False`.
        - **background\_rectangle\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html)) – Background color of table if `include_background_rectangle` is `True`.
        - **element\_to\_mobject** (*Callable**[**[**float* *|* *str* *|* [*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]**,* [*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]*) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) class applied to the table entries. by default [`Paragraph`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html). For common choices, see [`text_mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.html)/[`tex_mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.html).
        - **element\_to\_mobject\_config** (*dict*) – Custom configuration passed to `element_to_mobject`, by default {}.
        - **arrange\_in\_grid\_config** (*dict*) – Dict passed to [`arrange_in_grid()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html), customizes the arrangement of the table.
        - **line\_config** (*dict*) – Dict passed to [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html), customizes the lines of the table.
        - **kwargs** – Additional arguments to be passed to [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html).

    Examples

    Example: TableExamples

    ![../_images/TableExamples-2.png](https://docs.manim.community/en/stable/_images/TableExamples-2.png)

    ```
    class TableExamples(Scene):
        def construct(self):
            t0 = Table(
                [["This", "is a"],
                ["simple", "Table in \\n Manim."]])
            t1 = Table(
                [["This", "is a"],
                ["simple", "Table."]],
                row_labels=[Text("R1"), Text("R2")],
                col_labels=[Text("C1"), Text("C2")])
            t1.add_highlighted_cell((2,2), color=YELLOW)
            t2 = Table(
                [["This", "is a"],
                ["simple", "Table."]],
                row_labels=[Text("R1"), Text("R2")],
                col_labels=[Text("C1"), Text("C2")],
                top_left_entry=Star().scale(0.3),
                include_outer_lines=True,
                arrange_in_grid_config={"cell_alignment": RIGHT})
            t2.add(t2.get_cell((2,2), color=RED))
            t3 = Table(
                [["This", "is a"],
                ["simple", "Table."]],
                row_labels=[Text("R1"), Text("R2")],
                col_labels=[Text("C1"), Text("C2")],
                top_left_entry=Star().scale(0.3),
                include_outer_lines=True,
                line_config={"stroke_width": 1, "color": YELLOW})
            t3.remove(*t3.get_vertical_lines())
            g = Group(
                t0,t1,t2,t3
            ).scale(0.7).arrange_in_grid(buff=1)
            self.add(g)
    ```

    Example: BackgroundRectanglesExample

    ![../_images/BackgroundRectanglesExample-2.png](https://docs.manim.community/en/stable/_images/BackgroundRectanglesExample-2.png)

    ```
    class BackgroundRectanglesExample(Scene):
        def construct(self):
            background = Rectangle(height=6.5, width=13)
            background.set_fill(opacity=.5)
            background.set_color([TEAL, RED, YELLOW])
            self.add(background)
            t0 = Table(
                [["This", "is a"],
                ["simple", "Table."]],
                add_background_rectangles_to_entries=True)
            t1 = Table(
                [["This", "is a"],
                ["simple", "Table."]],
                include_background_rectangle=True)
            g = Group(t0, t1).scale(0.7).arrange(buff=0.5)
            self.add(g)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`add_background_to_entries`](#manim.mobject.table.Table.add_background_to_entries) | Adds a black [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html) to each entry of the table. |
    | [`add_highlighted_cell`](#manim.mobject.table.Table.add_highlighted_cell) | Highlights one cell at a specific position on the table by adding a [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html). |
    | [`create`](#manim.mobject.table.Table.create) | Customized create-type function for tables. |
    | [`get_cell`](#manim.mobject.table.Table.get_cell) | Returns one specific cell as a rectangular [`Polygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html) without the entry. |
    | [`get_col_labels`](#manim.mobject.table.Table.get_col_labels) | Return the column labels of the table. |
    | [`get_columns`](#manim.mobject.table.Table.get_columns) | Return columns of the table as a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) of [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html). |
    | [`get_entries`](#manim.mobject.table.Table.get_entries) | Return the individual entries of the table (including labels) or one specific entry if the parameter, `pos`, is set. |
    | [`get_entries_without_labels`](#manim.mobject.table.Table.get_entries_without_labels) | Return the individual entries of the table (without labels) or one specific entry if the parameter, `pos`, is set. |
    | [`get_highlighted_cell`](#manim.mobject.table.Table.get_highlighted_cell) | Returns a [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html) of the cell at the given position. |
    | [`get_horizontal_lines`](#manim.mobject.table.Table.get_horizontal_lines) | Return the horizontal lines of the table. |
    | [`get_labels`](#manim.mobject.table.Table.get_labels) | Returns the labels of the table. |
    | [`get_row_labels`](#manim.mobject.table.Table.get_row_labels) | Return the row labels of the table. |
    | [`get_rows`](#manim.mobject.table.Table.get_rows) | Return the rows of the table as a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) of [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html). |
    | [`get_vertical_lines`](#manim.mobject.table.Table.get_vertical_lines) | Return the vertical lines of the table. |
    | [`scale`](#manim.mobject.table.Table.scale) | Scale the size by a factor. |
    | [`set_column_colors`](#manim.mobject.table.Table.set_column_colors) | Set individual colors for each column of the table. |
    | [`set_row_colors`](#manim.mobject.table.Table.set_row_colors) | Set individual colors for each row of the table. |

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

    \_add\_horizontal\_lines()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Adds the horizontal lines to the table.

        Return type:
        :   [*Table*](#manim.mobject.table.Table)

    \_add\_labels(*mob\_table*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Adds labels to an in a grid arranged [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html).

        Parameters:
        :   **mob\_table** ([*VGroup*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)) – An in a grid organized class:~.VGroup.

        Returns:
        :   Returns the `mob_table` with added labels.

        Return type:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    \_add\_vertical\_lines()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Adds the vertical lines to the table

        Return type:
        :   [*Table*](#manim.mobject.table.Table)

    \_organize\_mob\_table(*table*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Arranges the [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) of `table` in a grid.

        Parameters:
        :   **table** (*Iterable**[**Iterable**[*[*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]**]*) – A 2D iterable object with [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) entries.

        Returns:
        :   The [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) of the `table` in a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) already
            arranged in a table-like grid.

        Return type:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    \_original\_\_init\_\_(*table*, *row\_labels=None*, *col\_labels=None*, *top\_left\_entry=None*, *v\_buff=0.8*, *h\_buff=1.3*, *include\_outer\_lines=False*, *add\_background\_rectangles\_to\_entries=False*, *entries\_background\_color=ManimColor('#000000')*, *include\_background\_rectangle=False*, *background\_rectangle\_color=ManimColor('#000000')*, *element\_to\_mobject=<class 'manim.mobject.text.text\_mobject.Paragraph'>*, *element\_to\_mobject\_config={}*, *arrange\_in\_grid\_config={}*, *line\_config={}*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **table** (*Iterable**[**Iterable**[**float* *|* *str* *|* [*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]**]*)
            - **row\_labels** (*Iterable**[*[*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]* *|* *None*)
            - **col\_labels** (*Iterable**[*[*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]* *|* *None*)
            - **top\_left\_entry** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* *None*)
            - **v\_buff** (*float*)
            - **h\_buff** (*float*)
            - **include\_outer\_lines** (*bool*)
            - **add\_background\_rectangles\_to\_entries** (*bool*)
            - **entries\_background\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
            - **include\_background\_rectangle** (*bool*)
            - **background\_rectangle\_color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
            - **element\_to\_mobject** (*Callable**[**[**float* *|* *str* *|* [*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]**,* [*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]*)
            - **element\_to\_mobject\_config** (*dict*)
            - **arrange\_in\_grid\_config** (*dict*)
            - **line\_config** (*dict*)

    \_table\_to\_mob\_table(*table*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Initializes the entries of `table` as [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html).

        Parameters:
        :   **table** (*Iterable**[**Iterable**[**float* *|* *str* *|* [*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)*]**]*) – A 2D array or list of lists. Content of the table has to be a valid input
            for the callable set in `element_to_mobject`.

        Returns:
        :   List of [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) from the entries of `table`.

        Return type:
        :   List

    add\_background\_to\_entries(*color=ManimColor('#000000')*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Adds a black [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html) to each entry of the table.

        Parameters:
        :   **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))

        Return type:
        :   [*Table*](#manim.mobject.table.Table)

    add\_highlighted\_cell(*pos=(1, 1)*, *color=ManimColor('#FFFF00')*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Highlights one cell at a specific position on the table by adding a [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html).

        Parameters:
        :   - **pos** (*Sequence**[**int**]*) – The position of a specific entry on the table. `(1,1)` being the top left entry
              of the table.
            - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html)) – The color used to highlight the cell.
            - **kwargs** – Additional arguments to be passed to [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html).

        Return type:
        :   [*Table*](#manim.mobject.table.Table)

        Examples

        Example: AddHighlightedCellExample

        ![../_images/AddHighlightedCellExample-1.png](https://docs.manim.community/en/stable/_images/AddHighlightedCellExample-1.png)

        ```
        class AddHighlightedCellExample(Scene):
            def construct(self):
                table = Table(
                    [["First", "Second"],
                    ["Third","Fourth"]],
                    row_labels=[Text("R1"), Text("R2")],
                    col_labels=[Text("C1"), Text("C2")])
                table.add_highlighted_cell((2,2), color=GREEN)
                self.add(table)
        ```

    create(*lag\_ratio=1*, *line\_animation=<class 'manim.animation.creation.Create'>*, *label\_animation=<class 'manim.animation.creation.Write'>*, *element\_animation=<class 'manim.animation.creation.Create'>*, *entry\_animation=<class 'manim.animation.fading.FadeIn'>*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Customized create-type function for tables.

        Parameters:
        :   - **lag\_ratio** (*float*) – The lag ratio of the animation.
            - **line\_animation** (*Callable**[**[*[*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* [*VGroup*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)*]**,* [*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)*]*) – The animation style of the table lines, see [`creation`](https://docs.manim.community/en/stable/reference/manim.animation.creation.html) for examples.
            - **label\_animation** (*Callable**[**[*[*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* [*VGroup*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)*]**,* [*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)*]*) – The animation style of the table labels, see [`creation`](https://docs.manim.community/en/stable/reference/manim.animation.creation.html) for examples.
            - **element\_animation** (*Callable**[**[*[*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* [*VGroup*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)*]**,* [*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)*]*) – The animation style of the table elements, see [`creation`](https://docs.manim.community/en/stable/reference/manim.animation.creation.html) for examples.
            - **entry\_animation** (*Callable**[**[*[*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* [*VGroup*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)*]**,* [*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)*]*) – The entry animation of the table background, see [`creation`](https://docs.manim.community/en/stable/reference/manim.animation.creation.html) for examples.
            - **kwargs** – Further arguments passed to the creation animations.

        Returns:
        :   AnimationGroup containing creation of the lines and of the elements.

        Return type:
        :   [`AnimationGroup`](https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html)

        Examples

        Example: CreateTableExample

        [
        ](./CreateTableExample-1.mp4)

        ```
        class CreateTableExample(Scene):
            def construct(self):
                table = Table(
                    [["First", "Second"],
                    ["Third","Fourth"]],
                    row_labels=[Text("R1"), Text("R2")],
                    col_labels=[Text("C1"), Text("C2")],
                    include_outer_lines=True)
                self.play(table.create())
                self.wait()
        ```

    get\_cell(*pos=(1, 1)*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Returns one specific cell as a rectangular [`Polygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html) without the entry.

        Parameters:
        :   - **pos** (*Sequence**[**int**]*) – The position of a specific entry on the table. `(1,1)` being the top left entry
              of the table.
            - **kwargs** – Additional arguments to be passed to [`Polygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html).

        Returns:
        :   Polygon mimicking one specific cell of the Table.

        Return type:
        :   [`Polygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html)

        Examples

        Example: GetCellExample

        ![../_images/GetCellExample-1.png](https://docs.manim.community/en/stable/_images/GetCellExample-1.png)

        ```
        class GetCellExample(Scene):
            def construct(self):
                table = Table(
                    [["First", "Second"],
                    ["Third","Fourth"]],
                    row_labels=[Text("R1"), Text("R2")],
                    col_labels=[Text("C1"), Text("C2")])
                cell = table.get_cell((2,2), color=RED)
                self.add(table, cell)
        ```

    get\_col\_labels()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Return the column labels of the table.

        Returns:
        :   VGroup containing the column labels of the table.

        Return type:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

        Examples

        Example: GetColLabelsExample

        ![../_images/GetColLabelsExample-1.png](https://docs.manim.community/en/stable/_images/GetColLabelsExample-1.png)

        ```
        class GetColLabelsExample(Scene):
            def construct(self):
                table = Table(
                    [["First", "Second"],
                    ["Third","Fourth"]],
                    row_labels=[Text("R1"), Text("R2")],
                    col_labels=[Text("C1"), Text("C2")])
                lab = table.get_col_labels()
                for item in lab:
                    item.set_color(random_bright_color())
                self.add(table)
        ```

    get\_columns()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Return columns of the table as a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) of [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html).

        Returns:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) containing each column in a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html).

        Return type:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

        Examples

        Example: GetColumnsExample

        ![../_images/GetColumnsExample-2.png](https://docs.manim.community/en/stable/_images/GetColumnsExample-2.png)

        ```
        class GetColumnsExample(Scene):
            def construct(self):
                table = Table(
                    [["First", "Second"],
                    ["Third","Fourth"]],
                    row_labels=[Text("R1"), Text("R2")],
                    col_labels=[Text("C1"), Text("C2")])
                table.add(SurroundingRectangle(table.get_columns()[1]))
                self.add(table)
        ```

    get\_entries(*pos=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Return the individual entries of the table (including labels) or one specific entry
        if the parameter, `pos`, is set.

        Parameters:
        :   **pos** (*Sequence**[**int**]* *|* *None*) – The position of a specific entry on the table. `(1,1)` being the top left entry
            of the table.

        Returns:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) containing all entries of the table (including labels)
            or the [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) at the given position if `pos` is set.

        Return type:
        :   Union[[`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html), [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)]

        Examples

        Example: GetEntriesExample

        ![../_images/GetEntriesExample-2.png](https://docs.manim.community/en/stable/_images/GetEntriesExample-2.png)

        ```
        class GetEntriesExample(Scene):
            def construct(self):
                table = Table(
                    [["First", "Second"],
                    ["Third","Fourth"]],
                    row_labels=[Text("R1"), Text("R2")],
                    col_labels=[Text("C1"), Text("C2")])
                ent = table.get_entries()
                for item in ent:
                    item.set_color(random_bright_color())
                table.get_entries((2,2)).rotate(PI)
                self.add(table)
        ```

    get\_entries\_without\_labels(*pos=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Return the individual entries of the table (without labels) or one specific entry
        if the parameter, `pos`, is set.

        Parameters:
        :   **pos** (*Sequence**[**int**]* *|* *None*) – The position of a specific entry on the table. `(1,1)` being the top left entry
            of the table (without labels).

        Returns:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) containing all entries of the table (without labels)
            or the [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) at the given position if `pos` is set.

        Return type:
        :   Union[[`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html), [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)]

        Examples

        Example: GetEntriesWithoutLabelsExample

        ![../_images/GetEntriesWithoutLabelsExample-1.png](https://docs.manim.community/en/stable/_images/GetEntriesWithoutLabelsExample-1.png)

        ```
        class GetEntriesWithoutLabelsExample(Scene):
            def construct(self):
                table = Table(
                    [["First", "Second"],
                    ["Third","Fourth"]],
                    row_labels=[Text("R1"), Text("R2")],
                    col_labels=[Text("C1"), Text("C2")])
                ent = table.get_entries_without_labels()
                colors = [BLUE, GREEN, YELLOW, RED]
                for k in range(len(colors)):
                    ent[k].set_color(colors[k])
                table.get_entries_without_labels((2,2)).rotate(PI)
                self.add(table)
        ```

    get\_highlighted\_cell(*pos=(1, 1)*, *color=ManimColor('#FFFF00')*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Returns a [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html) of the cell at the given position.

        Parameters:
        :   - **pos** (*Sequence**[**int**]*) – The position of a specific entry on the table. `(1,1)` being the top left entry
              of the table.
            - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html)) – The color used to highlight the cell.
            - **kwargs** – Additional arguments to be passed to [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html).

        Return type:
        :   [*BackgroundRectangle*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html)

        Examples

        Example: GetHighlightedCellExample

        ![../_images/GetHighlightedCellExample-1.png](https://docs.manim.community/en/stable/_images/GetHighlightedCellExample-1.png)

        ```
        class GetHighlightedCellExample(Scene):
            def construct(self):
                table = Table(
                    [["First", "Second"],
                    ["Third","Fourth"]],
                    row_labels=[Text("R1"), Text("R2")],
                    col_labels=[Text("C1"), Text("C2")])
                highlight = table.get_highlighted_cell((2,2), color=GREEN)
                table.add_to_back(highlight)
                self.add(table)
        ```

    get\_horizontal\_lines()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Return the horizontal lines of the table.

        Returns:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) containing all the horizontal lines of the table.

        Return type:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

        Examples

        Example: GetHorizontalLinesExample

        ![../_images/GetHorizontalLinesExample-1.png](https://docs.manim.community/en/stable/_images/GetHorizontalLinesExample-1.png)

        ```
        class GetHorizontalLinesExample(Scene):
            def construct(self):
                table = Table(
                    [["First", "Second"],
                    ["Third","Fourth"]],
                    row_labels=[Text("R1"), Text("R2")],
                    col_labels=[Text("C1"), Text("C2")])
                table.get_horizontal_lines().set_color(RED)
                self.add(table)
        ```

    get\_labels()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Returns the labels of the table.

        Returns:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) containing all the labels of the table.

        Return type:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

        Examples

        Example: GetLabelsExample

        ![../_images/GetLabelsExample-1.png](https://docs.manim.community/en/stable/_images/GetLabelsExample-1.png)

        ```
        class GetLabelsExample(Scene):
            def construct(self):
                table = Table(
                    [["First", "Second"],
                    ["Third","Fourth"]],
                    row_labels=[Text("R1"), Text("R2")],
                    col_labels=[Text("C1"), Text("C2")])
                lab = table.get_labels()
                colors = [BLUE, GREEN, YELLOW, RED]
                for k in range(len(colors)):
                    lab[k].set_color(colors[k])
                self.add(table)
        ```

    get\_row\_labels()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Return the row labels of the table.

        Returns:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) containing the row labels of the table.

        Return type:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

        Examples

        Example: GetRowLabelsExample

        ![../_images/GetRowLabelsExample-1.png](https://docs.manim.community/en/stable/_images/GetRowLabelsExample-1.png)

        ```
        class GetRowLabelsExample(Scene):
            def construct(self):
                table = Table(
                    [["First", "Second"],
                    ["Third","Fourth"]],
                    row_labels=[Text("R1"), Text("R2")],
                    col_labels=[Text("C1"), Text("C2")])
                lab = table.get_row_labels()
                for item in lab:
                    item.set_color(random_bright_color())
                self.add(table)
        ```

    get\_rows()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Return the rows of the table as a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) of [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html).

        Returns:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) containing each row in a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html).

        Return type:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

        Examples

        Example: GetRowsExample

        ![../_images/GetRowsExample-2.png](https://docs.manim.community/en/stable/_images/GetRowsExample-2.png)

        ```
        class GetRowsExample(Scene):
            def construct(self):
                table = Table(
                    [["First", "Second"],
                    ["Third","Fourth"]],
                    row_labels=[Text("R1"), Text("R2")],
                    col_labels=[Text("C1"), Text("C2")])
                table.add(SurroundingRectangle(table.get_rows()[1]))
                self.add(table)
        ```

    get\_vertical\_lines()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Return the vertical lines of the table.

        Returns:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) containing all the vertical lines of the table.

        Return type:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

        Examples

        Example: GetVerticalLinesExample

        ![../_images/GetVerticalLinesExample-1.png](https://docs.manim.community/en/stable/_images/GetVerticalLinesExample-1.png)

        ```
        class GetVerticalLinesExample(Scene):
            def construct(self):
                table = Table(
                    [["First", "Second"],
                    ["Third","Fourth"]],
                    row_labels=[Text("R1"), Text("R2")],
                    col_labels=[Text("C1"), Text("C2")])
                table.get_vertical_lines()[0].set_color(RED)
                self.add(table)
        ```

    scale(*scale\_factor*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Scale the size by a factor.

        Default behavior is to scale about the center of the vmobject.

        Parameters:
        :   - **scale\_factor** (*float*) – The scaling factor \(\alpha\). If \(0 < |\alpha| < 1\), the mobject
              will shrink, and for \(|\alpha| > 1\) it will grow. Furthermore,
              if \(\alpha < 0\), the mobject is also flipped.
            - **scale\_stroke** – Boolean determining if the object’s outline is scaled when the object is scaled.
              If enabled, and object with 2px outline is scaled by a factor of .5, it will have an outline of 1px.
            - **kwargs** – Additional keyword arguments passed to
              [`scale()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).

        Returns:
        :   `self`

        Return type:
        :   `VMobject`

        Examples

        Example: MobjectScaleExample

        ![../_images/MobjectScaleExample-2.png](https://docs.manim.community/en/stable/_images/MobjectScaleExample-2.png)

        ```
        class MobjectScaleExample(Scene):
            def construct(self):
                c1 = Circle(1, RED).set_x(-1)
                c2 = Circle(1, GREEN).set_x(1)

                vg = VGroup(c1, c2)
                vg.set_stroke(width=50)
                self.add(vg)

                self.play(
                    c1.animate.scale(.25),
                    c2.animate.scale(.25,
                        scale_stroke=True)
                )
        ```

        See also

        `move_to()`

    set\_column\_colors(*\*colors*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Set individual colors for each column of the table.

        Parameters:
        :   **colors** (*Iterable**[**TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)**]*) – An iterable of colors; each color corresponds to a column.

        Return type:
        :   [*Table*](#manim.mobject.table.Table)

        Examples

        Example: SetColumnColorsExample

        ![../_images/SetColumnColorsExample-2.png](https://docs.manim.community/en/stable/_images/SetColumnColorsExample-2.png)

        ```
        class SetColumnColorsExample(Scene):
            def construct(self):
                table = Table(
                    [["First", "Second"],
                    ["Third","Fourth"]],
                    row_labels=[Text("R1"), Text("R2")],
                    col_labels=[Text("C1"), Text("C2")]
                ).set_column_colors([RED,BLUE], GREEN)
                self.add(table)
        ```

    set\_row\_colors(*\*colors*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html)
    :   Set individual colors for each row of the table.

        Parameters:
        :   **colors** (*Iterable**[**TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)**]*) – An iterable of colors; each color corresponds to a row.

        Return type:
        :   [*Table*](#manim.mobject.table.Table)

        Examples

        Example: SetRowColorsExample

        ![../_images/SetRowColorsExample-2.png](https://docs.manim.community/en/stable/_images/SetRowColorsExample-2.png)

        ```
        class SetRowColorsExample(Scene):
            def construct(self):
                table = Table(
                    [["First", "Second"],
                    ["Third","Fourth"]],
                    row_labels=[Text("R1"), Text("R2")],
                    col_labels=[Text("C1"), Text("C2")]
                ).set_row_colors([RED,BLUE], GREEN)
                self.add(table)
        ```
