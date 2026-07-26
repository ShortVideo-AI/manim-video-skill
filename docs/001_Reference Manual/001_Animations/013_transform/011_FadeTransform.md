---
{
  "title": "FadeTransform",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "FadeTransform"
  ],
  "scraped_at": "2026-07-10T15:58:17"
}
---

# FadeTransform

Qualified name: `manim.animation.transform.FadeTransform`

class FadeTransform(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html)

    Fades one mobject into another.

    Parameters:
    :   - **mobject** – The starting [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).
        - **target\_mobject** – The target [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).
        - **stretch** – Controls whether the target [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) is stretched during
          the animation. Default: `True`.
        - **dim\_to\_match** – If the target mobject is not stretched automatically, this allows
          to adjust the initial scale of the target [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) while
          it is shifted in. Setting this to 0, 1, and 2, respectively,
          matches the length of the target with the length of the starting
          [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) in x, y, and z direction, respectively.
        - **kwargs** – Further keyword arguments are passed to the parent class.

    Examples

    Example: DifferentFadeTransforms

    [
    ](./DifferentFadeTransforms-1.mp4)

    ```
    class DifferentFadeTransforms(Scene):
        def construct(self):
            starts = [Rectangle(width=4, height=1) for _ in range(3)]
            VGroup(*starts).arrange(DOWN, buff=1).shift(3*LEFT)
            targets = [Circle(fill_opacity=1).scale(0.25) for _ in range(3)]
            VGroup(*targets).arrange(DOWN, buff=1).shift(3*RIGHT)

            self.play(*[FadeIn(s) for s in starts])
            self.play(
                FadeTransform(starts[0], targets[0], stretch=True),
                FadeTransform(starts[1], targets[1], stretch=False, dim_to_match=0),
                FadeTransform(starts[2], targets[2], stretch=False, dim_to_match=1)
            )

            self.play(*[FadeOut(mobj) for mobj in self.mobjects])
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`begin`](#manim.animation.transform.FadeTransform.begin) | Initial setup for the animation. |
    | [`clean_up_from_scene`](#manim.animation.transform.FadeTransform.clean_up_from_scene) | Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) after finishing the animation. |
    | `get_all_families_zipped` |  |
    | [`get_all_mobjects`](#manim.animation.transform.FadeTransform.get_all_mobjects) | Get all mobjects involved in the animation. |
    | [`ghost_to`](#manim.animation.transform.FadeTransform.ghost_to) | Replaces the source by the target and sets the opacity to 0. |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *target\_mobject*, *stretch=True*, *dim\_to\_match=1*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

    begin()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
    :   Initial setup for the animation.

        The mobject to which this animation is bound is a group consisting of
        both the starting and the ending mobject. At the start, the ending
        mobject replaces the starting mobject (and is completely faded). In the
        end, it is set to be the other way around.

    clean\_up\_from\_scene(*scene*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
    :   Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) after finishing the animation.

        This includes to [`remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) the Animation’s
        [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) if the animation is a remover.

        Parameters:
        :   **scene** – The scene the animation should be cleaned up from.

    get\_all\_mobjects()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
    :   Get all mobjects involved in the animation.

        Ordering must match the ordering of arguments to interpolate\_submobject

        Returns:
        :   The sequence of mobjects.

        Return type:
        :   Sequence[[Mobject](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)]

    ghost\_to(*source*, *target*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
    :   Replaces the source by the target and sets the opacity to 0.

        If the provided target has no points, and thus a location of [0, 0, 0]
        the source will simply fade out where it currently is.
