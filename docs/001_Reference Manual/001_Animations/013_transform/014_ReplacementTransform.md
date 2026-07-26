---
{
  "title": "ReplacementTransform",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.ReplacementTransform.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "ReplacementTransform"
  ],
  "scraped_at": "2026-07-10T15:58:19"
}
---

# ReplacementTransform

Qualified name: `manim.animation.transform.ReplacementTransform`

class ReplacementTransform(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html)

    Replaces and morphs a mobject into a target mobject.

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The starting [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).
        - **target\_mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The target [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).
        - **kwargs** – Further keyword arguments that are passed to [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html).

    Examples

    Example: ReplacementTransformOrTransform

    [
    ](./ReplacementTransformOrTransform-1.mp4)

    ```
    class ReplacementTransformOrTransform(Scene):
        def construct(self):
            # set up the numbers
            r_transform = VGroup(*[Integer(i) for i in range(1,4)])
            text_1 = Text("ReplacementTransform", color=RED)
            r_transform.add(text_1)

            transform = VGroup(*[Integer(i) for i in range(4,7)])
            text_2 = Text("Transform", color=BLUE)
            transform.add(text_2)

            ints = VGroup(r_transform, transform)
            texts = VGroup(text_1, text_2).scale(0.75)
            r_transform.arrange(direction=UP, buff=1)
            transform.arrange(direction=UP, buff=1)

            ints.arrange(buff=2)
            self.add(ints, texts)

            # The mobs replace each other and none are left behind
            self.play(ReplacementTransform(r_transform[0], r_transform[1]))
            self.play(ReplacementTransform(r_transform[1], r_transform[2]))

            # The mobs linger after the Transform()
            self.play(Transform(transform[0], transform[1]))
            self.play(Transform(transform[1], transform[2]))
            self.wait()
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *target\_mobject*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **target\_mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))

        Return type:
        :   None
