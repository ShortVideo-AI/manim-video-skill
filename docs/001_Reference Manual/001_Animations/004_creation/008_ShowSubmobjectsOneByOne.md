---
{
  "title": "ShowSubmobjectsOneByOne",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowSubmobjectsOneByOne.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "creation",
    "ShowSubmobjectsOneByOne"
  ],
  "scraped_at": "2026-07-10T15:57:44"
}
---

# ShowSubmobjectsOneByOne

Qualified name: `manim.animation.creation.ShowSubmobjectsOneByOne`

class ShowSubmobjectsOneByOne(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
:   Bases: [`ShowIncreasingSubsets`](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowIncreasingSubsets.html)

    Show one submobject at a time, removing all previously displayed ones from screen.

    Methods

    |  |  |
    | --- | --- |
    | `update_submobject_list` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   - **group** (*Iterable**[*[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]*)
        - **int\_func** (*Callable**[**[**np.ndarray**]**,* *np.ndarray**]*)

    \_original\_\_init\_\_(*group*, *int\_func=<ufunc 'ceil'>*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **group** (*Iterable**[*[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]*)
            - **int\_func** (*Callable**[**[**ndarray**]**,* *ndarray**]*)

        Return type:
        :   None
