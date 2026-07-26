---
{
  "title": "ShowIncreasingSubsets",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowIncreasingSubsets.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "creation",
    "ShowIncreasingSubsets"
  ],
  "scraped_at": "2026-07-10T15:57:43"
}
---

# ShowIncreasingSubsets

Qualified name: `manim.animation.creation.ShowIncreasingSubsets`

class ShowIncreasingSubsets(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
:   Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)

    Show one submobject at a time, leaving all previous ones displayed on screen.

    Examples

    Example: ShowIncreasingSubsetsScene

    [
    ](./ShowIncreasingSubsetsScene-1.mp4)

    ```
    class ShowIncreasingSubsetsScene(Scene):
        def construct(self):
            p = VGroup(Dot(), Square(), Triangle())
            self.add(p)
            self.play(ShowIncreasingSubsets(p))
            self.wait()
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`interpolate_mobject`](#manim.animation.creation.ShowIncreasingSubsets.interpolate_mobject) | Interpolates the mobject of the `Animation` based on alpha value. |
    | `update_submobject_list` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   - **group** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
        - **suspend\_mobject\_updating** (*bool*)
        - **int\_func** (*Callable**[**[**np.ndarray**]**,* *np.ndarray**]*)

    \_original\_\_init\_\_(*group*, *suspend\_mobject\_updating=False*, *int\_func=<ufunc 'floor'>*, *reverse\_rate\_function=False*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **group** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **suspend\_mobject\_updating** (*bool*)
            - **int\_func** (*Callable**[**[**ndarray**]**,* *ndarray**]*)

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
