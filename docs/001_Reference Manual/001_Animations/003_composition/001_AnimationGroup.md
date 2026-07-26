---
{
  "title": "AnimationGroup",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "composition",
    "AnimationGroup"
  ],
  "scraped_at": "2026-07-10T15:57:37"
}
---

# AnimationGroup

Qualified name: `manim.animation.composition.AnimationGroup`

class AnimationGroup(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html)
:   Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)

    Plays a group or series of [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html).

    Parameters:
    :   - **animations** ([*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html) *|* *Iterable**[*[*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)*]*) – Sequence of [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html) objects to be played.
        - **group** ([*Group*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Group.html) *|* [*VGroup*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) *|* *OpenGLGroup* *|* *OpenGLVGroup* *|* *None*) – A group of multiple [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).
        - **run\_time** (*float* *|* *None*) – The duration of the animation in seconds.
        - **rate\_func** (*Callable**[**[**float**]**,* *float**]*) – The function defining the animation progress based on the relative
          runtime (see [`rate_functions`](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.html)) .
        - **lag\_ratio** (*float*) –

          Defines the delay after which the animation is applied to submobjects. A lag\_ratio of
          `n.nn` means the next animation will play when `nnn%` of the current animation has played.
          Defaults to 0.0, meaning that all animations will be played together.

          This does not influence the total runtime of the animation. Instead the runtime
          of individual animations is adjusted so that the complete animation has the defined
          run time.
        - **kwargs** (*Any*)

    Methods

    |  |  |
    | --- | --- |
    | [`begin`](#manim.animation.composition.AnimationGroup.begin) | Begin the animation. |
    | [`build_animations_with_timings`](#manim.animation.composition.AnimationGroup.build_animations_with_timings) | Creates a list of triplets of the form (anim, start\_time, end\_time). |
    | [`clean_up_from_scene`](#manim.animation.composition.AnimationGroup.clean_up_from_scene) | Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) after finishing the animation. |
    | [`finish`](#manim.animation.composition.AnimationGroup.finish) | Finish the animation. |
    | [`get_all_mobjects`](#manim.animation.composition.AnimationGroup.get_all_mobjects) | Get all mobjects involved in the animation. |
    | [`init_run_time`](#manim.animation.composition.AnimationGroup.init_run_time) | Calculates the run time of the animation, if different from `run_time`. |
    | [`interpolate`](#manim.animation.composition.AnimationGroup.interpolate) | Set the animation progress. |
    | [`update_mobjects`](#manim.animation.composition.AnimationGroup.update_mobjects) | Updates things like starting\_mobject, and (for Transforms) target\_mobject. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*\*animations*, *group=None*, *run\_time=None*, *rate\_func=<function linear>*, *lag\_ratio=0*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **animations** ([*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html) *|* *Iterable**[*[*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)*]*)
            - **group** ([*Group*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Group.html) *|* [*VGroup*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html) *|* *OpenGLGroup* *|* *OpenGLVGroup* *|* *None*)
            - **run\_time** (*float* *|* *None*)
            - **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
            - **lag\_ratio** (*float*)
            - **kwargs** (*Any*)

    \_setup\_scene(*scene*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html)
    :   Setup up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) before starting the animation.

        This includes to [`add()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) the Animation’s
        [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) if the animation is an introducer.

        Parameters:
        :   **scene** ([*Scene*](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html)) – The scene the animation should be cleaned up from.

        Return type:
        :   None

    begin()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html)
    :   Begin the animation.

        This method is called right as an animation is being played. As much
        initialization as possible, especially any mobject copying, should live in this
        method.

        Return type:
        :   None

    build\_animations\_with\_timings()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html)
    :   Creates a list of triplets of the form (anim, start\_time, end\_time).

        Return type:
        :   None

    clean\_up\_from\_scene(*scene*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html)
    :   Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) after finishing the animation.

        This includes to [`remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) the Animation’s
        [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) if the animation is a remover.

        Parameters:
        :   **scene** ([*Scene*](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html)) – The scene the animation should be cleaned up from.

        Return type:
        :   None

    finish()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html)
    :   Finish the animation.

        This method gets called when the animation is over.

        Return type:
        :   None

    get\_all\_mobjects()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html)
    :   Get all mobjects involved in the animation.

        Ordering must match the ordering of arguments to interpolate\_submobject

        Returns:
        :   The sequence of mobjects.

        Return type:
        :   Sequence[[Mobject](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)]

    init\_run\_time(*run\_time*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html)
    :   Calculates the run time of the animation, if different from `run_time`.

        Parameters:
        :   **run\_time** (*float* *|* *None*) – The duration of the animation in seconds.

        Returns:
        :   The duration of the animation in seconds.

        Return type:
        :   run\_time

    interpolate(*alpha*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html)
    :   Set the animation progress.

        This method gets called for every frame during an animation.

        Parameters:
        :   **alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
            the end.

        Return type:
        :   None

    update\_mobjects(*dt*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html)
    :   Updates things like starting\_mobject, and (for
        Transforms) target\_mobject. Note, since typically
        (always?) self.mobject will have its updating
        suspended during the animation, this will do
        nothing to self.mobject.

        Parameters:
        :   **dt** (*float*)

        Return type:
        :   None
