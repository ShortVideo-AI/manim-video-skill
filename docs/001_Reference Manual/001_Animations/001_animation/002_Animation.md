---
{
  "title": "Animation",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "animation",
    "Animation"
  ],
  "scraped_at": "2026-07-10T15:57:34"
}
---

# Animation

Qualified name: `manim.animation.animation.Animation`

class Animation(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
:   Bases: `object`

    An animation.

    Animations have a fixed time span.

    Parameters:
    :   - **mobject** – The mobject to be animated. This is not required for all types of animations.
        - **lag\_ratio** –

          Defines the delay after which the animation is applied to submobjects. This lag
          is relative to the duration of the animation.

          This does not influence the total
          runtime of the animation. Instead the runtime of individual animations is
          adjusted so that the complete animation has the defined run time.
        - **run\_time** – The duration of the animation in seconds.
        - **rate\_func** –

          The function defining the animation progress based on the relative runtime (see [`rate_functions`](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.html)) .

          For example `rate_func(0.5)` is the proportion of the animation that is done
          after half of the animations run time.
        - **reverse\_rate\_function** – Reverses the rate function of the animation. Setting `reverse_rate_function`
          does not have any effect on `remover` or `introducer`. These need to be
          set explicitly if an introducer-animation should be turned into a remover one
          and vice versa.
        - **name** – The name of the animation. This gets displayed while rendering the animation.
          Defaults to <class-name>(<Mobject-name>).
        - **remover** – Whether the given mobject should be removed from the scene after this animation.
        - **suspend\_mobject\_updating** – Whether updaters of the mobject should be suspended during the animation.

    Return type:
    :   Self

    Note

    In the current implementation of this class, the specified rate function is applied
    within [`Animation.interpolate_mobject()`](#manim.animation.animation.Animation.interpolate_mobject) call as part of the call to
    `Animation.interpolate_submobject()`. For subclasses of [`Animation`](#manim.animation.animation.Animation)
    that are implemented by overriding [`interpolate_mobject()`](#manim.animation.animation.Animation.interpolate_mobject), the rate function
    has to be applied manually (e.g., by passing `self.rate_func(alpha)` instead
    of just `alpha`).

    Examples

    Example: LagRatios

    [
    ](./LagRatios-1.mp4)

    ```
    class LagRatios(Scene):
        def construct(self):
            ratios = [0, 0.1, 0.5, 1, 2]  # demonstrated lag_ratios

            # Create dot groups
            group = VGroup(*[Dot() for _ in range(4)]).arrange_submobjects()
            groups = VGroup(*[group.copy() for _ in ratios]).arrange_submobjects(buff=1)
            self.add(groups)

            # Label groups
            self.add(Text("lag_ratio = ", font_size=36).next_to(groups, UP, buff=1.5))
            for group, ratio in zip(groups, ratios):
                self.add(Text(str(ratio), font_size=36).next_to(group, UP))

            #Animate groups with different lag_ratios
            self.play(AnimationGroup(*[
                group.animate(lag_ratio=ratio, run_time=1.5).shift(DOWN * 2)
                for group, ratio in zip(groups, ratios)
            ]))

            # lag_ratio also works recursively on nested submobjects:
            self.play(groups.animate(run_time=1, lag_ratio=0.1).shift(UP * 2))
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`begin`](#manim.animation.animation.Animation.begin) | Begin the animation. |
    | [`clean_up_from_scene`](#manim.animation.animation.Animation.clean_up_from_scene) | Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) after finishing the animation. |
    | [`copy`](#manim.animation.animation.Animation.copy) | Create a copy of the animation. |
    | `create_starting_mobject` |  |
    | [`finish`](#manim.animation.animation.Animation.finish) | Finish the animation. |
    | `get_all_families_zipped` |  |
    | [`get_all_mobjects`](#manim.animation.animation.Animation.get_all_mobjects) | Get all mobjects involved in the animation. |
    | [`get_all_mobjects_to_update`](#manim.animation.animation.Animation.get_all_mobjects_to_update) | Get all mobjects to be updated during the animation. |
    | [`get_rate_func`](#manim.animation.animation.Animation.get_rate_func) | Get the rate function of the animation. |
    | [`get_run_time`](#manim.animation.animation.Animation.get_run_time) | Get the run time of the animation. |
    | [`get_sub_alpha`](#manim.animation.animation.Animation.get_sub_alpha) | Get the animation progress of any submobjects subanimation. |
    | [`interpolate`](#manim.animation.animation.Animation.interpolate) | Set the animation progress. |
    | [`interpolate_mobject`](#manim.animation.animation.Animation.interpolate_mobject) | Interpolates the mobject of the [`Animation`](#manim.animation.animation.Animation) based on alpha value. |
    | `interpolate_submobject` |  |
    | [`is_introducer`](#manim.animation.animation.Animation.is_introducer) | Test if the animation is an introducer. |
    | [`is_remover`](#manim.animation.animation.Animation.is_remover) | Test if the animation is a remover. |
    | [`set_default`](#manim.animation.animation.Animation.set_default) | Sets the default values of keyword arguments. |
    | [`set_name`](#manim.animation.animation.Animation.set_name) | Set the name of the animation. |
    | [`set_rate_func`](#manim.animation.animation.Animation.set_rate_func) | Set the rate function of the animation. |
    | [`set_run_time`](#manim.animation.animation.Animation.set_run_time) | Set the run time of the animation. |
    | [`update_mobjects`](#manim.animation.animation.Animation.update_mobjects) | Updates things like starting\_mobject, and (for Transforms) target\_mobject. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *lag\_ratio=0.0*, *run\_time=1.0*, *rate\_func=<function smooth>*, *reverse\_rate\_function=False*, *name=None*, *remover=False*, *suspend\_mobject\_updating=True*, *introducer=False*, *\**, *\_on\_finish=<function Animation.<lambda>>*, *use\_override=True*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) *|* *OpenGLMobject* *|* *None*)
            - **lag\_ratio** (*float*)
            - **run\_time** (*float*)
            - **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
            - **reverse\_rate\_function** (*bool*)
            - **name** (*str*)
            - **remover** (*bool*)
            - **suspend\_mobject\_updating** (*bool*)
            - **introducer** (*bool*)
            - **\_on\_finish** (*Callable**[**[**]**,* *None**]*)
            - **use\_override** (*bool*)

        Return type:
        :   None

    \_setup\_scene(*scene*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Setup up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) before starting the animation.

        This includes to [`add()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) the Animation’s
        [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) if the animation is an introducer.

        Parameters:
        :   **scene** ([*Scene*](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html)) – The scene the animation should be cleaned up from.

        Return type:
        :   None

    begin()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Begin the animation.

        This method is called right as an animation is being played. As much
        initialization as possible, especially any mobject copying, should live in this
        method.

        Return type:
        :   None

    clean\_up\_from\_scene(*scene*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) after finishing the animation.

        This includes to [`remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) the Animation’s
        [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) if the animation is a remover.

        Parameters:
        :   **scene** ([*Scene*](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html)) – The scene the animation should be cleaned up from.

        Return type:
        :   None

    copy()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Create a copy of the animation.

        Returns:
        :   A copy of `self`

        Return type:
        :   [Animation](#manim.animation.animation.Animation)

    finish()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Finish the animation.

        This method gets called when the animation is over.

        Return type:
        :   None

    get\_all\_mobjects()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Get all mobjects involved in the animation.

        Ordering must match the ordering of arguments to interpolate\_submobject

        Returns:
        :   The sequence of mobjects.

        Return type:
        :   Sequence[[Mobject](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)]

    get\_all\_mobjects\_to\_update()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Get all mobjects to be updated during the animation.

        Returns:
        :   The list of mobjects to be updated during the animation.

        Return type:
        :   List[[Mobject](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)]

    get\_rate\_func()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Get the rate function of the animation.

        Returns:
        :   The rate function of the animation.

        Return type:
        :   Callable[[float], float]

    get\_run\_time()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Get the run time of the animation.

        Returns:
        :   The time the animation takes in seconds.

        Return type:
        :   float

    get\_sub\_alpha(*alpha*, *index*, *num\_submobjects*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Get the animation progress of any submobjects subanimation.

        Parameters:
        :   - **alpha** (*float*) – The overall animation progress
            - **index** (*int*) – The index of the subanimation.
            - **num\_submobjects** (*int*) – The total count of subanimations.

        Returns:
        :   The progress of the subanimation.

        Return type:
        :   float

    interpolate(*alpha*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Set the animation progress.

        This method gets called for every frame during an animation.

        Parameters:
        :   **alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
            the end.

        Return type:
        :   None

    interpolate\_mobject(*alpha*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Interpolates the mobject of the [`Animation`](#manim.animation.animation.Animation) based on alpha value.

        Parameters:
        :   **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
            is completed. For example, alpha-values of 0, 0.5, and 1 correspond
            to the animation being completed 0%, 50%, and 100%, respectively.

        Return type:
        :   None

    is\_introducer()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Test if the animation is an introducer.

        Returns:
        :   `True` if the animation is an introducer, `False` otherwise.

        Return type:
        :   bool

    is\_remover()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Test if the animation is a remover.

        Returns:
        :   `True` if the animation is a remover, `False` otherwise.

        Return type:
        :   bool

    classmethod set\_default(*\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Sets the default values of keyword arguments.

        If this method is called without any additional keyword
        arguments, the original default values of the initialization
        method of this class are restored.

        Parameters:
        :   **kwargs** – Passing any keyword argument will update the default
            values of the keyword arguments of the initialization
            function of this class.

        Return type:
        :   None

        Examples

        Example: ChangeDefaultAnimation

        [
        ](./ChangeDefaultAnimation-1.mp4)

        ```
        class ChangeDefaultAnimation(Scene):
            def construct(self):
                Rotate.set_default(run_time=2, rate_func=rate_functions.linear)
                Indicate.set_default(color=None)

                S = Square(color=BLUE, fill_color=BLUE, fill_opacity=0.25)
                self.add(S)
                self.play(Rotate(S, PI))
                self.play(Indicate(S))

                Rotate.set_default()
                Indicate.set_default()
        ```

    set\_name(*name*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Set the name of the animation.

        Parameters:
        :   **name** (*str*) – The new name of the animation.

        Returns:
        :   `self`

        Return type:
        :   [Animation](#manim.animation.animation.Animation)

    set\_rate\_func(*rate\_func*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Set the rate function of the animation.

        Parameters:
        :   **rate\_func** (*Callable**[**[**float**]**,* *float**]*) – The new function defining the animation progress based on the
            relative runtime (see [`rate_functions`](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.html)).

        Returns:
        :   `self`

        Return type:
        :   [Animation](#manim.animation.animation.Animation)

    set\_run\_time(*run\_time*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Set the run time of the animation.

        Parameters:
        :   - **run\_time** (*float*) – The new time the animation should take in seconds.
            - **note::** (*..*) – The run\_time of an animation should not be changed while it is already
              running.

        Returns:
        :   `self`

        Return type:
        :   [Animation](#manim.animation.animation.Animation)

    update\_mobjects(*dt*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Updates things like starting\_mobject, and (for
        Transforms) target\_mobject. Note, since typically
        (always?) self.mobject will have its updating
        suspended during the animation, this will do
        nothing to self.mobject.

        Parameters:
        :   **dt** (*float*)

        Return type:
        :   None
