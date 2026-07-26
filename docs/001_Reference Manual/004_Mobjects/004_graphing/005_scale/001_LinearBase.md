---
{
  "title": "LinearBase",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LinearBase.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "graphing",
    "scale",
    "LinearBase"
  ],
  "scraped_at": "2026-07-10T15:59:40"
}
---

# LinearBase

Qualified name: `manim.mobject.graphing.scale.LinearBase`

class LinearBase(*scale\_factor=1.0*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/scale.html)
:   Bases: `_ScaleBase`

    The default scaling class.

    Parameters:
    :   **scale\_factor** (*float*) – The slope of the linear function, by default 1.0

    Methods

    |  |  |
    | --- | --- |
    | [`function`](#manim.mobject.graphing.scale.LinearBase.function) | Multiplies the value by the scale factor. |
    | [`inverse_function`](#manim.mobject.graphing.scale.LinearBase.inverse_function) | Inverse of function. |

    function(*value*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/scale.html)
    :   Multiplies the value by the scale factor.

        Parameters:
        :   **value** (*float*) – Value to be multiplied by the scale factor.

        Return type:
        :   float

    inverse\_function(*value*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/scale.html)
    :   Inverse of function. Divides the value by the scale factor.

        Parameters:
        :   **value** (*float*) – value to be divided by the scale factor.

        Return type:
        :   float
