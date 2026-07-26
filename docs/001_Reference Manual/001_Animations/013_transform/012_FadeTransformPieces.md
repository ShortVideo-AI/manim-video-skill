---
{
  "title": "FadeTransformPieces",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransformPieces.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "FadeTransformPieces"
  ],
  "scraped_at": "2026-07-10T15:58:18"
}
---

# FadeTransformPieces

Qualified name: `manim.animation.transform.FadeTransformPieces`

class FadeTransformPieces(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`FadeTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html)

    Fades submobjects of one mobject into submobjects of another one.

    See also

    [`FadeTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html)

    Examples

    Example: FadeTransformSubmobjects

    [
    ](./FadeTransformSubmobjects-1.mp4)

    ```
    class FadeTransformSubmobjects(Scene):
        def construct(self):
            src = VGroup(Square(), Circle().shift(LEFT + UP))
            src.shift(3*LEFT + 2*UP)
            src_copy = src.copy().shift(4*DOWN)

            target = VGroup(Circle(), Triangle().shift(RIGHT + DOWN))
            target.shift(3*RIGHT + 2*UP)
            target_copy = target.copy().shift(4*DOWN)

            self.play(FadeIn(src), FadeIn(src_copy))
            self.play(
                FadeTransform(src, target),
                FadeTransformPieces(src_copy, target_copy)
            )
            self.play(*[FadeOut(mobj) for mobj in self.mobjects])
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`begin`](#manim.animation.transform.FadeTransformPieces.begin) | Initial setup for the animation. |
    | [`ghost_to`](#manim.animation.transform.FadeTransformPieces.ghost_to) | Replaces the source submobjects by the target submobjects and sets the opacity to 0. |

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

    ghost\_to(*source*, *target*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
    :   Replaces the source submobjects by the target submobjects and sets
        the opacity to 0.
