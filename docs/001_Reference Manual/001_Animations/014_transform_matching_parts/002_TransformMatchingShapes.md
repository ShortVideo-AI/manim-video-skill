---
{
  "title": "TransformMatchingShapes",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform_matching_parts",
    "TransformMatchingShapes"
  ],
  "scraped_at": "2026-07-10T15:58:24"
}
---

# TransformMatchingShapes

Qualified name: `manim.animation.transform\_matching\_parts.TransformMatchingShapes`

class TransformMatchingShapes(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform_matching_parts.html)
:   Bases: [`TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html)

    An animation trying to transform groups by matching the shape
    of their submobjects.

    Two submobjects match if the hash of their point coordinates after
    normalization (i.e., after translation to the origin, fixing the submobject
    height at 1 unit, and rounding the coordinates to three decimal places)
    matches.

    See also

    [`TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html)

    Examples

    Example: Anagram

    [
    ](./Anagram-1.mp4)

    ```
    class Anagram(Scene):
        def construct(self):
            src = Text("the morse code")
            tar = Text("here come dots")
            self.play(Write(src))
            self.wait(0.5)
            self.play(TransformMatchingShapes(src, tar, path_arc=PI/2))
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
