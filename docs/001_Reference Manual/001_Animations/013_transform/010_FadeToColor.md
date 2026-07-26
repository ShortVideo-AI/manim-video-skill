---
{
  "title": "FadeToColor",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeToColor.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "FadeToColor"
  ],
  "scraped_at": "2026-07-10T15:58:17"
}
---

# FadeToColor

Qualified name: `manim.animation.transform.FadeToColor`

class FadeToColor(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`ApplyMethod`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html)

    Animation that changes color of a mobject.

    Examples

    Example: FadeToColorExample

    [
    ](./FadeToColorExample-1.mp4)

    ```
    class FadeToColorExample(Scene):
        def construct(self):
            self.play(FadeToColor(Text("Hello World!"), color=RED))
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
        - **color** (*str*)

    \_original\_\_init\_\_(*mobject*, *color*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **color** (*str*)

        Return type:
        :   None
