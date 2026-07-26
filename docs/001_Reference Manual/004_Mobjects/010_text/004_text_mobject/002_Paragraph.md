---
{
  "title": "Paragraph",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "text",
    "text_mobject",
    "Paragraph"
  ],
  "scraped_at": "2026-07-10T16:00:09"
}
---

# Paragraph

Qualified name: `manim.mobject.text.text\_mobject.Paragraph`

class Paragraph(*\*text*, *line\_spacing=-1*, *alignment=None*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/text_mobject.html)
:   Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    Display a paragraph of text.

    For a given [`Paragraph`](#manim.mobject.text.text_mobject.Paragraph) `par`, the attribute `par.chars` is a
    [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) containing all the lines. In this context, every line is
    constructed as a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) of characters contained in the line.

    Parameters:
    :   - **line\_spacing** (*float*) – Represents the spacing between lines. Defaults to -1, which means auto.
        - **alignment** (*str* *|* *None*) – Defines the alignment of paragraph. Defaults to None. Possible values are “left”, “right” or “center”.
        - **text** (*str*)
        - **kwargs** (*Any*)

    Examples

    Normal usage:

    Remove unwanted invisible characters:

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

    \_change\_alignment\_for\_a\_line(*alignment*, *line\_no*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/text_mobject.html)
    :   Function to change one line’s alignment to a specific value.

        Parameters:
        :   - **alignment** (*str*) – Defines the alignment of paragraph. Possible values are “left”, “right”, “center”.
            - **line\_no** (*int*) – Defines the line number for which we want to set given alignment.

        Return type:
        :   None

    \_gen\_chars(*lines\_str\_list*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/text_mobject.html)
    :   Function to convert a list of plain strings to a VGroup of VGroups of chars.

        Parameters:
        :   **lines\_str\_list** (*list*) – List of plain text strings.

        Returns:
        :   The generated 2d-VGroup of chars.

        Return type:
        :   [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    \_original\_\_init\_\_(*\*text*, *line\_spacing=-1*, *alignment=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **text** (*str*)
            - **line\_spacing** (*float*)
            - **alignment** (*str* *|* *None*)
            - **kwargs** (*Any*)

    \_set\_all\_lines\_alignments(*alignment*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/text_mobject.html)
    :   Function to set all line’s alignment to a specific value.

        Parameters:
        :   **alignment** (*str*) – Defines the alignment of paragraph. Possible values are “left”, “right”, “center”.

        Return type:
        :   [*Paragraph*](#manim.mobject.text.text_mobject.Paragraph)

    \_set\_all\_lines\_to\_initial\_positions()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/text_mobject.html)
    :   Set all lines to their initial positions.

        Return type:
        :   [*Paragraph*](#manim.mobject.text.text_mobject.Paragraph)

    \_set\_line\_alignment(*alignment*, *line\_no*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/text_mobject.html)
    :   Function to set one line’s alignment to a specific value.

        Parameters:
        :   - **alignment** (*str*) – Defines the alignment of paragraph. Possible values are “left”, “right”, “center”.
            - **line\_no** (*int*) – Defines the line number for which we want to set given alignment.

        Return type:
        :   [*Paragraph*](#manim.mobject.text.text_mobject.Paragraph)

    \_set\_line\_to\_initial\_position(*line\_no*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/text_mobject.html)
    :   Function to set one line to initial positions.

        Parameters:
        :   **line\_no** (*int*) – Defines the line number for which we want to set given alignment.

        Return type:
        :   [*Paragraph*](#manim.mobject.text.text_mobject.Paragraph)
