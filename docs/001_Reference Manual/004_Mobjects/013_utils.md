---
{
  "title": "utils",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.utils.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "utils"
  ],
  "scraped_at": "2026-07-10T16:00:38"
}
---

# utils

Utilities for working with mobjects.

Functions

get\_mobject\_class()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/utils.html)
:   Gets the base mobject class, depending on the currently active renderer.

    Note

    This method is intended to be used in the code base of Manim itself
    or in plugins where code should work independent of the selected
    renderer.

    Examples

    The function has to be explicitly imported. We test that
    the name of the returned class is one of the known mobject
    base classes:

    Return type:
    :   type

get\_point\_mobject\_class()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/utils.html)
:   Gets the point cloud mobject class, depending on the currently
    active renderer.

    Note

    This method is intended to be used in the code base of Manim itself
    or in plugins where code should work independent of the selected
    renderer.

    Examples

    The function has to be explicitly imported. We test that
    the name of the returned class is one of the known mobject
    base classes:

    Return type:
    :   type

get\_vectorized\_mobject\_class()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/utils.html)
:   Gets the vectorized mobject class, depending on the currently
    active renderer.

    Note

    This method is intended to be used in the code base of Manim itself
    or in plugins where code should work independent of the selected
    renderer.

    Examples

    The function has to be explicitly imported. We test that
    the name of the returned class is one of the known mobject
    base classes:

    Return type:
    :   type
