---
{
  "title": "ChangeSpeed",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "speedmodifier",
    "ChangeSpeed"
  ],
  "scraped_at": "2026-07-10T15:58:09"
}
---

# ChangeSpeed

Qualified name: `manim.animation.speedmodifier.ChangeSpeed`

class ChangeSpeed(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html)
:   Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)

    Modifies the speed of passed animation.
    `AnimationGroup` with different `lag_ratio` can also be used
    which combines multiple animations into one.
    The `run_time` of the passed animation is changed to modify the speed.

    Parameters:
    :   - **anim** ([*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html) *|* *\_AnimationBuilder*) – Animation of which the speed is to be modified.
        - **speedinfo** (*dict**[**float**,* *float**]*) – Contains nodes (percentage of `run_time`) and its corresponding speed factor.
        - **rate\_func** (*Callable**[**[**float**]**,* *float**]* *|* *None*) – Overrides `rate_func` of passed animation, applied before changing speed.
        - **affects\_speed\_updaters** (*bool*)

    Examples

    Example: SpeedModifierExample

    [
    ](./SpeedModifierExample-1.mp4)

    ```
    class SpeedModifierExample(Scene):
        def construct(self):
            a = Dot().shift(LEFT * 4)
            b = Dot().shift(RIGHT * 4)
            self.add(a, b)
            self.play(
                ChangeSpeed(
                    AnimationGroup(
                        a.animate(run_time=1).shift(RIGHT * 8),
                        b.animate(run_time=1).shift(LEFT * 8),
                    ),
                    speedinfo={0.3: 1, 0.4: 0.1, 0.6: 0.1, 1: 1},
                    rate_func=linear,
                )
            )
    ```

    Example: SpeedModifierUpdaterExample

    [
    ](./SpeedModifierUpdaterExample-1.mp4)

    ```
    class SpeedModifierUpdaterExample(Scene):
        def construct(self):
            a = Dot().shift(LEFT * 4)
            self.add(a)

            ChangeSpeed.add_updater(a, lambda x, dt: x.shift(RIGHT * 4 * dt))
            self.play(
                ChangeSpeed(
                    Wait(2),
                    speedinfo={0.4: 1, 0.5: 0.2, 0.8: 0.2, 1: 1},
                    affects_speed_updaters=True,
                )
            )
    ```

    Example: SpeedModifierUpdaterExample2

    [
    ](./SpeedModifierUpdaterExample2-1.mp4)

    ```
    class SpeedModifierUpdaterExample2(Scene):
        def construct(self):
            a = Dot().shift(LEFT * 4)
            self.add(a)

            ChangeSpeed.add_updater(a, lambda x, dt: x.shift(RIGHT * 4 * dt))
            self.wait()
            self.play(
                ChangeSpeed(
                    Wait(),
                    speedinfo={1: 0},
                    affects_speed_updaters=True,
                )
            )
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`add_updater`](#manim.animation.speedmodifier.ChangeSpeed.add_updater) | This static method can be used to apply speed change to updaters. |
    | [`begin`](#manim.animation.speedmodifier.ChangeSpeed.begin) | Begin the animation. |
    | [`clean_up_from_scene`](#manim.animation.speedmodifier.ChangeSpeed.clean_up_from_scene) | Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) after finishing the animation. |
    | [`finish`](#manim.animation.speedmodifier.ChangeSpeed.finish) | Finish the animation. |
    | [`get_scaled_total_time`](#manim.animation.speedmodifier.ChangeSpeed.get_scaled_total_time) | The time taken by the animation under the assumption that the `run_time` is 1. |
    | [`interpolate`](#manim.animation.speedmodifier.ChangeSpeed.interpolate) | Set the animation progress. |
    | `setup` |  |
    | [`update_mobjects`](#manim.animation.speedmodifier.ChangeSpeed.update_mobjects) | Updates things like starting\_mobject, and (for Transforms) target\_mobject. |

    Attributes

    |  |  |
    | --- | --- |
    | `dt` |  |
    | `is_changing_dt` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*anim*, *speedinfo*, *rate\_func=None*, *affects\_speed\_updaters=True*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **anim** ([*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html) *|* *\_AnimationBuilder*)
            - **speedinfo** (*dict**[**float**,* *float**]*)
            - **rate\_func** (*Callable**[**[**float**]**,* *float**]* *|* *None*)
            - **affects\_speed\_updaters** (*bool*)

        Return type:
        :   None

    \_setup\_scene(*scene*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html)
    :   Setup up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) before starting the animation.

        This includes to [`add()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) the Animation’s
        [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) if the animation is an introducer.

        Parameters:
        :   **scene** – The scene the animation should be cleaned up from.

        Return type:
        :   None

    classmethod add\_updater(*mobject*, *update\_function*, *index=None*, *call\_updater=False*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html)
    :   This static method can be used to apply speed change to updaters.

        This updater will follow speed and rate function of any [`ChangeSpeed`](#manim.animation.speedmodifier.ChangeSpeed)
        animation that is playing with `affects_speed_updaters=True`. By default,
        updater functions added via the usual [`Mobject.add_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) method
        do not respect the change of animation speed.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobject to which the updater should be attached.
            - **update\_function** ([*Updater*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html)) – The function that is called whenever a new frame is rendered.
            - **index** (*int* *|* *None*) – The position in the list of the mobject’s updaters at which the
              function should be inserted.
            - **call\_updater** (*bool*) – If `True`, calls the update function when attaching it to the
              mobject.

        See also

        [`ChangeSpeed`](#manim.animation.speedmodifier.ChangeSpeed), [`Mobject.add_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)

    begin()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html)
    :   Begin the animation.

        This method is called right as an animation is being played. As much
        initialization as possible, especially any mobject copying, should live in this
        method.

        Return type:
        :   None

    clean\_up\_from\_scene(*scene*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html)
    :   Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) after finishing the animation.

        This includes to [`remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) the Animation’s
        [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) if the animation is a remover.

        Parameters:
        :   **scene** ([*Scene*](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html)) – The scene the animation should be cleaned up from.

        Return type:
        :   None

    finish()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html)
    :   Finish the animation.

        This method gets called when the animation is over.

        Return type:
        :   None

    get\_scaled\_total\_time()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html)
    :   The time taken by the animation under the assumption that the `run_time` is 1.

        Return type:
        :   float

    interpolate(*alpha*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html)
    :   Set the animation progress.

        This method gets called for every frame during an animation.

        Parameters:
        :   **alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
            the end.

        Return type:
        :   None

    update\_mobjects(*dt*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html)
    :   Updates things like starting\_mobject, and (for
        Transforms) target\_mobject. Note, since typically
        (always?) self.mobject will have its updating
        suspended during the animation, this will do
        nothing to self.mobject.

        Parameters:
        :   **dt** (*float*)

        Return type:
        :   None
