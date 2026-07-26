---
{
  "title": "Group",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Group.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "mobject",
    "Group"
  ],
  "scraped_at": "2026-07-10T15:59:46"
}
---

# Group

Qualified name: `manim.mobject.mobject.Group`

class Group(*\*mobjects*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html)
:   Bases: [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)

    Groups together multiple [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).

    Notes

    When adding the same mobject more than once, repetitions are ignored.
    Use [`Mobject.copy()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) to create a separate copy which can then
    be added to the group.

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `depth` | The depth of the mobject. |
    | `height` | The height of the mobject. |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*\*mobjects*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Return type:
        :   None
