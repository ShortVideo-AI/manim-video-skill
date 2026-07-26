---
{
  "title": "CyclicReplace",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.CyclicReplace.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "CyclicReplace"
  ],
  "scraped_at": "2026-07-10T15:58:16"
}
---

# CyclicReplace

Qualified name: `manim.animation.transform.CyclicReplace`

class CyclicReplace(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html)

    An animation moving mobjects cyclically.

    In particular, this means: the first mobject takes the place
    of the second mobject, the second one takes the place of
    the third mobject, and so on. The last mobject takes the
    place of the first one.

    Parameters:
    :   - **mobjects** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – List of mobjects to be transformed.
        - **path\_arc** (*float*) – The angle of the arc (in radians) that the mobjects will follow to reach
          their target.
        - **kwargs** – Further keyword arguments that are passed to [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html).

    Examples

    Example: CyclicReplaceExample

    [
    ](./CyclicReplaceExample-1.mp4)

    ```
    class CyclicReplaceExample(Scene):
        def construct(self):
            group = VGroup(Square(), Circle(), Triangle(), Star())
            group.arrange(RIGHT)
            self.add(group)

            for _ in range(4):
                self.play(CyclicReplace(*group))
    ```

    Methods

    |  |  |
    | --- | --- |
    | `create_target` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*\*mobjects*, *path\_arc=1.5707963267948966*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobjects** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **path\_arc** (*float*)

        Return type:
        :   None
