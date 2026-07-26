---
{
  "title": "TransformMatchingAbstractBase",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform_matching_parts",
    "TransformMatchingAbstractBase"
  ],
  "scraped_at": "2026-07-10T15:58:24"
}
---

# TransformMatchingAbstractBase

Qualified name: `manim.animation.transform\_matching\_parts.TransformMatchingAbstractBase`

class TransformMatchingAbstractBase(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform_matching_parts.html)
:   Bases: [`AnimationGroup`](https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html)

    Abstract base class for transformations that keep track of matching parts.

    Subclasses have to implement the two static methods
    `get_mobject_parts()` and
    `get_mobject_key()`.

    Basically, this transformation first maps all submobjects returned
    by the `get_mobject_parts` method to certain keys by applying the
    `get_mobject_key` method. Then, submobjects with matching keys
    are transformed into each other.

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The starting [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).
        - **target\_mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The target [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).
        - **transform\_mismatches** (*bool*) – Controls whether submobjects without a matching key are transformed
          into each other by using [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html). Default: `False`.
        - **fade\_transform\_mismatches** (*bool*) – Controls whether submobjects without a matching key are transformed
          into each other by using [`FadeTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html). Default: `False`.
        - **key\_map** (*dict* *|* *None*) – Optional. A dictionary mapping keys belonging to some of the starting mobject’s
          submobjects (i.e., the return values of the `get_mobject_key` method)
          to some keys belonging to the target mobject’s submobjects that should
          be transformed although the keys don’t match.
        - **kwargs** – All further keyword arguments are passed to the submobject transformations.

    Note

    If neither `transform_mismatches` nor `fade_transform_mismatches`
    are set to `True`, submobjects without matching keys in the starting
    mobject are faded out in the direction of the unmatched submobjects in
    the target mobject, and unmatched submobjects in the target mobject
    are faded in from the direction of the unmatched submobjects in the
    start mobject.

    Methods

    |  |  |
    | --- | --- |
    | [`clean_up_from_scene`](#manim.animation.transform_matching_parts.TransformMatchingAbstractBase.clean_up_from_scene) | Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) after finishing the animation. |
    | `get_mobject_key` |  |
    | `get_mobject_parts` |  |
    | `get_shape_map` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *target\_mobject*, *transform\_mismatches=False*, *fade\_transform\_mismatches=False*, *key\_map=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **target\_mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **transform\_mismatches** (*bool*)
            - **fade\_transform\_mismatches** (*bool*)
            - **key\_map** (*dict* *|* *None*)

    clean\_up\_from\_scene(*scene*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform_matching_parts.html)
    :   Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) after finishing the animation.

        This includes to [`remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) the Animation’s
        [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) if the animation is a remover.

        Parameters:
        :   **scene** ([*Scene*](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html)) – The scene the animation should be cleaned up from.

        Return type:
        :   None
