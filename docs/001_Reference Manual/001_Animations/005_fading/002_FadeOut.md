---
{
  "title": "FadeOut",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "fading",
    "FadeOut"
  ],
  "scraped_at": "2026-07-10T15:57:50"
}
---

# FadeOut

Qualified name: `manim.animation.fading.FadeOut`

class FadeOut(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/fading.html)
:   Bases: `_Fade`

    Fade out [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) s.

    Parameters:
    :   - **mobjects** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobjects to be faded out.
        - **shift** – The vector by which the mobject shifts while being faded out.
        - **target\_position** – The position to which the mobject moves while being faded out. In case another
          mobject is given as target position, its center is used.
        - **scale** – The factor by which the mobject is scaled while being faded out.
        - **kwargs** (*Any*)

    Examples

    Example: FadeInExample

    [
    ](./FadeInExample-2.mp4)

    ```
    class FadeInExample(Scene):
        def construct(self):
            dot = Dot(UP * 2 + LEFT)
            self.add(dot)
            tex = Tex(
                "FadeOut with ", "shift ", r" or target\_position", " and scale"
            ).scale(1)
            animations = [
                FadeOut(tex[0]),
                FadeOut(tex[1], shift=DOWN),
                FadeOut(tex[2], target_position=dot),
                FadeOut(tex[3], scale=0.5),
            ]
            self.play(AnimationGroup(*animations, lag_ratio=0.5))
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`clean_up_from_scene`](#manim.animation.fading.FadeOut.clean_up_from_scene) | Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) after finishing the animation. |
    | `create_target` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*\*mobjects*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobjects** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **kwargs** (*Any*)

        Return type:
        :   None

    clean\_up\_from\_scene(*scene*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/fading.html)
    :   Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) after finishing the animation.

        This includes to [`remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) the Animation’s
        [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) if the animation is a remover.

        Parameters:
        :   **scene** ([*Scene*](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html)) – The scene the animation should be cleaned up from.

        Return type:
        :   None
