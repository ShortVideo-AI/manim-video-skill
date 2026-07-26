---
{
  "title": "Restore",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "Restore"
  ],
  "scraped_at": "2026-07-10T15:58:19"
}
---

# Restore

Qualified name: `manim.animation.transform.Restore`

class Restore(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`ApplyMethod`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html)

    Transforms a mobject to its last saved state.

    To save the state of a mobject, use the [`save_state()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) method.

    Examples

    Example: RestoreExample

    [
    ](./RestoreExample-1.mp4)

    ```
    class RestoreExample(Scene):
        def construct(self):
            s = Square()
            s.save_state()
            self.play(FadeIn(s))
            self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2*LEFT).scale(3))
            self.play(s.animate.shift(5*DOWN).rotate(PI/4))
            self.wait()
            self.play(Restore(s), run_time=2)
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
