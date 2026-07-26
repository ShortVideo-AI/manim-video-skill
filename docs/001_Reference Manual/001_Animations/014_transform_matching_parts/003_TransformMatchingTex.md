---
{
  "title": "TransformMatchingTex",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingTex.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform_matching_parts",
    "TransformMatchingTex"
  ],
  "scraped_at": "2026-07-10T15:58:25"
}
---

# TransformMatchingTex

Qualified name: `manim.animation.transform\_matching\_parts.TransformMatchingTex`

class TransformMatchingTex(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform_matching_parts.html)
:   Bases: [`TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html)

    A transformation trying to transform rendered LaTeX strings.

    Two submobjects match if their `tex_string` matches.

    See also

    [`TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html)

    Examples

    Example: MatchingEquationParts

    [
    ](./MatchingEquationParts-1.mp4)

    ```
    class MatchingEquationParts(Scene):
        def construct(self):
            variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)

            eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
            eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
            eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

            self.add(eq1)
            self.wait(0.5)
            self.play(TransformMatchingTex(Group(eq1, variables), eq2))
            self.wait(0.5)
            self.play(TransformMatchingTex(eq2, eq3))
            self.wait(0.5)
    ```

    Methods

    |  |  |
    | --- | --- |
    | `get_mobject_key` |  |
    | `get_mobject_parts` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
        - **target\_mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
        - **transform\_mismatches** (*bool*)
        - **fade\_transform\_mismatches** (*bool*)
        - **key\_map** (*dict* *|* *None*)

    \_original\_\_init\_\_(*mobject*, *target\_mobject*, *transform\_mismatches=False*, *fade\_transform\_mismatches=False*, *key\_map=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **target\_mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **transform\_mismatches** (*bool*)
            - **fade\_transform\_mismatches** (*bool*)
            - **key\_map** (*dict* *|* *None*)
