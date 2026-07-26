---
{
  "title": "RandomColorGenerator",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.color.core.RandomColorGenerator.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "color",
    "core",
    "RandomColorGenerator"
  ],
  "scraped_at": "2026-07-10T16:01:07"
}
---

# RandomColorGenerator

Qualified name: `manim.utils.color.core.RandomColorGenerator`

class RandomColorGenerator(*seed=None*, *sample\_colors=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Bases: `object`

    A generator for producing random colors from a given list of Manim colors,
    optionally in a reproducible sequence using a seed value.

    When initialized with a specific seed, this class produces a deterministic
    sequence of [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) instances. If no seed is provided, the selection is
    non-deterministic using Python’s global random state.

    Parameters:
    :   - **seed** (*int* *|* *None*) – A seed value to initialize the internal random number generator.
          If `None` (the default), colors are chosen using the global random state.
        - **sample\_colors** (*list**[*[*ManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)*]* *|* *None*) – A custom list of Manim colors to sample from. Defaults to the full Manim
          color palette.

    Examples

    Without a seed (non-deterministic):

    With a seed (deterministic sequence):

    Re-initializing with the same seed gives the same sequence:

    Using a custom color list:

    Without a seed and custom palette (non-deterministic):

    Methods

    |  |  |
    | --- | --- |
    | [`next`](#manim.utils.color.core.RandomColorGenerator.next) | Returns the next color from the configured color list. |

    classmethod \_random\_color()[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
    :   Internal method to generate a random color using the singleton instance of
        RandomColorGenerator.
        It will be used by proxy method random\_color publicly available
        and makes it backwards compatible.

        Returns:
        :   A randomly selected color from the configured color list of
            the singleton instance.

        Return type:
        :   [ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)

    next()[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
    :   Returns the next color from the configured color list.

        Returns:
        :   A randomly selected color from the specified color list.

        Return type:
        :   [ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)

        Examples

        Usage:
