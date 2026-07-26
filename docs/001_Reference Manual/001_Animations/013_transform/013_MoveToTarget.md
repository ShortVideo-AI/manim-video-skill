---
{
  "title": "MoveToTarget",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.MoveToTarget.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "MoveToTarget"
  ],
  "scraped_at": "2026-07-10T15:58:18"
}
---

# MoveToTarget

Qualified name: `manim.animation.transform.MoveToTarget`

class MoveToTarget(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html)

    Transforms a mobject to the mobject stored in its `target` attribute.

    After calling the `generate_target()` method, the `target`
    attribute of the mobject is populated with a copy of it. After modifying the attribute,
    playing the [`MoveToTarget`](#manim.animation.transform.MoveToTarget) animation transforms the original mobject
    into the modified one stored in the `target` attribute.

    Examples

    Example: MoveToTargetExample

    [
    ](./MoveToTargetExample-1.mp4)

    ```
    class MoveToTargetExample(Scene):
        def construct(self):
            c = Circle()

            c.generate_target()
            c.target.set_fill(color=GREEN, opacity=0.5)
            c.target.shift(2*RIGHT + UP).scale(0.5)

            self.add(c)
            self.play(MoveToTarget(c))
    ```

    Methods

    |  |  |
    | --- | --- |
    | `check_validity_of_input` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    Parameters:
    :   **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))

    \_original\_\_init\_\_(*mobject*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))

        Return type:
        :   None
