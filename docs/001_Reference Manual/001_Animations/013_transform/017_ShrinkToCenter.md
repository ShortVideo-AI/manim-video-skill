---
{
  "title": "ShrinkToCenter",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.ShrinkToCenter.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "ShrinkToCenter"
  ],
  "scraped_at": "2026-07-10T15:58:20"
}
---

# ShrinkToCenter

Qualified name: `manim.animation.transform.ShrinkToCenter`

class ShrinkToCenter(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`ScaleInPlace`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ScaleInPlace.html)

    Animation that makes a mobject shrink to center.

    Examples

    Example: ShrinkToCenterExample

    [
    ](./ShrinkToCenterExample-1.mp4)

    ```
    class ShrinkToCenterExample(Scene):
        def construct(self):
            self.play(ShrinkToCenter(Text("Hello World!")))
    ```

    Methods

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
