---
{
  "title": "MoveAlongPath",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.movement.MoveAlongPath.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "movement",
    "MoveAlongPath"
  ],
  "scraped_at": "2026-07-10T15:58:02"
}
---

# MoveAlongPath

Qualified name: `manim.animation.movement.MoveAlongPath`

class MoveAlongPath(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/movement.html)
:   Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)

    Make one mobject move along the path of another mobject.

    Example: MoveAlongPathExample

    [
    ](./MoveAlongPathExample-1.mp4)

    ```
    class MoveAlongPathExample(Scene):
        def construct(self):
            d1 = Dot().set_color(ORANGE)
            l1 = Line(LEFT, RIGHT)
            l2 = VMobject()
            self.add(d1, l1, l2)
            l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)))
            self.play(MoveAlongPath(d1, l1), rate_func=linear)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`interpolate_mobject`](#manim.animation.movement.MoveAlongPath.interpolate_mobject) | Interpolates the mobject of the `Animation` based on alpha value. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
        - **path** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))
        - **suspend\_mobject\_updating** (*bool*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*mobject*, *path*, *suspend\_mobject\_updating=False*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **path** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html))
            - **suspend\_mobject\_updating** (*bool*)
            - **kwargs** (*Any*)

    interpolate\_mobject(*alpha*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/movement.html)
    :   Interpolates the mobject of the `Animation` based on alpha value.

        Parameters:
        :   **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
            is completed. For example, alpha-values of 0, 0.5, and 1 correspond
            to the animation being completed 0%, 50%, and 100%, respectively.

        Return type:
        :   None
