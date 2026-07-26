---
{
  "title": "ShowPassingFlash",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "indication",
    "ShowPassingFlash"
  ],
  "scraped_at": "2026-07-10T15:57:58"
}
---

# ShowPassingFlash

Qualified name: `manim.animation.indication.ShowPassingFlash`

class ShowPassingFlash(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html)
:   Bases: [`ShowPartial`](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowPartial.html)

    Show only a sliver of the VMobject each frame.

    Parameters:
    :   - **mobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)) – The mobject whose stroke is animated.
        - **time\_width** (*float*) – The length of the sliver relative to the length of the stroke.
        - **kwargs** (*Any*)

    Examples

    Example: TimeWidthValues

    [
    ](./TimeWidthValues-1.mp4)

    ```
    class TimeWidthValues(Scene):
        def construct(self):
            p = RegularPolygon(5, color=DARK_GRAY, stroke_width=6).scale(3)
            lbl = VMobject()
            self.add(p, lbl)
            p = p.copy().set_color(BLUE)
            for time_width in [0.2, 0.5, 1, 2]:
                lbl.become(Tex(r"\texttt{time\_width={{%.1f}}}"%time_width))
                self.play(ShowPassingFlash(
                    p.copy().set_color(BLUE),
                    run_time=2,
                    time_width=time_width
                ))
    ```

    See also

    [`Create`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html)

    Methods

    |  |  |
    | --- | --- |
    | [`clean_up_from_scene`](#manim.animation.indication.ShowPassingFlash.clean_up_from_scene) | Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) after finishing the animation. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *time\_width=0.1*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))
            - **time\_width** (*float*)
            - **kwargs** (*Any*)

        Return type:
        :   None

    clean\_up\_from\_scene(*scene*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html)
    :   Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) after finishing the animation.

        This includes to [`remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) the Animation’s
        [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) if the animation is a remover.

        Parameters:
        :   **scene** ([*Scene*](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html)) – The scene the animation should be cleaned up from.

        Return type:
        :   None
