---
{
  "title": "ScaleInPlace",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.ScaleInPlace.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "ScaleInPlace"
  ],
  "scraped_at": "2026-07-10T15:58:20"
}
---

# ScaleInPlace

Qualified name: `manim.animation.transform.ScaleInPlace`

class ScaleInPlace(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`ApplyMethod`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html)

    Animation that scales a mobject by a certain factor.

    Examples

    Example: ScaleInPlaceExample

    [
    ](./ScaleInPlaceExample-1.mp4)

    ```
    class ScaleInPlaceExample(Scene):
        def construct(self):
            self.play(ScaleInPlace(Text("Hello World!"), 2))
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
        - **scale\_factor** (*float*)

    \_original\_\_init\_\_(*mobject*, *scale\_factor*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **scale\_factor** (*float*)

        Return type:
        :   None
