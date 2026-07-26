---
{
  "title": "SpiralIn",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.creation.SpiralIn.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "creation",
    "SpiralIn"
  ],
  "scraped_at": "2026-07-10T15:57:45"
}
---

# SpiralIn

Qualified name: `manim.animation.creation.SpiralIn`

class SpiralIn(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
:   Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)

    Create the Mobject with sub-Mobjects flying in on spiral trajectories.

    Parameters:
    :   - **shapes** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The Mobject on which to be operated.
        - **scale\_factor** (*float*) – The factor used for scaling the effect.
        - **fade\_in\_fraction** – Fractional duration of initial fade-in of sub-Mobjects as they fly inward.

    Examples

    Example: SpiralInExample

    [
    ](./SpiralInExample-1.mp4)

    ```
    class SpiralInExample(Scene):
        def construct(self):
            pi = MathTex(r"\pi").scale(7)
            pi.shift(2.25 * LEFT + 1.5 * UP)
            circle = Circle(color=GREEN_C, fill_opacity=1).shift(LEFT)
            square = Square(color=BLUE_D, fill_opacity=1).shift(UP)
            shapes = VGroup(pi, circle, square)
            self.play(SpiralIn(shapes))
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`interpolate_mobject`](#manim.animation.creation.SpiralIn.interpolate_mobject) | Interpolates the mobject of the `Animation` based on alpha value. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*shapes*, *scale\_factor=8*, *fade\_in\_fraction=0.3*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **shapes** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **scale\_factor** (*float*)

        Return type:
        :   None

    interpolate\_mobject(*alpha*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
    :   Interpolates the mobject of the `Animation` based on alpha value.

        Parameters:
        :   **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
            is completed. For example, alpha-values of 0, 0.5, and 1 correspond
            to the animation being completed 0%, 50%, and 100%, respectively.

        Return type:
        :   None
