---
{
  "title": "Wait",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "animation",
    "Wait"
  ],
  "scraped_at": "2026-07-10T15:57:34"
}
---

# Wait

Qualified name: `manim.animation.animation.Wait`

class Wait(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
:   Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)

    A “no operation” animation.

    Parameters:
    :   - **run\_time** (*float*) – The amount of time that should pass.
        - **stop\_condition** (*Callable**[**[**]**,* *bool**]* *|* *None*) – A function without positional arguments that evaluates to a boolean.
          The function is evaluated after every new frame has been rendered.
          Playing the animation stops after the return value is truthy, or
          after the specified `run_time` has passed.
        - **frozen\_frame** (*bool* *|* *None*) – Controls whether or not the wait animation is static, i.e., corresponds
          to a frozen frame. If `False` is passed, the render loop still
          progresses through the animation as usual and (among other things)
          continues to call updater functions. If `None` (the default value),
          the [`Scene.play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) call tries to determine whether the Wait call
          can be static or not itself via `Scene.should_mobjects_update()`.
        - **kwargs** – Keyword arguments to be passed to the parent class, [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html).
        - **rate\_func** (*Callable**[**[**float**]**,* *float**]*)

    Methods

    |  |  |
    | --- | --- |
    | [`begin`](#manim.animation.animation.Wait.begin) | Begin the animation. |
    | [`clean_up_from_scene`](#manim.animation.animation.Wait.clean_up_from_scene) | Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) after finishing the animation. |
    | [`finish`](#manim.animation.animation.Wait.finish) | Finish the animation. |
    | [`interpolate`](#manim.animation.animation.Wait.interpolate) | Set the animation progress. |
    | [`update_mobjects`](#manim.animation.animation.Wait.update_mobjects) | Updates things like starting\_mobject, and (for Transforms) target\_mobject. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*run\_time=1*, *stop\_condition=None*, *frozen\_frame=None*, *rate\_func=<function linear>*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **run\_time** (*float*)
            - **stop\_condition** (*Callable**[**[**]**,* *bool**]* *|* *None*)
            - **frozen\_frame** (*bool* *|* *None*)
            - **rate\_func** (*Callable**[**[**float**]**,* *float**]*)

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

    finish()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Finish the animation.

        This method gets called when the animation is over.

        Return type:
        :   None

    interpolate(*alpha*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
    :   Set the animation progress.

        This method gets called for every frame during an animation.

        Parameters:
        :   **alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
            the end.

        Return type:
        :   None

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
