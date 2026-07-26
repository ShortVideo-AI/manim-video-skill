---
{
  "title": "Rotate",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotate.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "rotation",
    "Rotate"
  ],
  "scraped_at": "2026-07-10T15:58:06"
}
---

# Rotate

Qualified name: `manim.animation.rotation.Rotate`

class Rotate(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/rotation.html)
:   Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html)

    Animation that rotates a Mobject.

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobject to be rotated.
        - **angle** (*float*) – The rotation angle.
        - **axis** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The rotation axis as a numpy vector.
        - **about\_point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* *None*) – The rotation center.
        - **about\_edge** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* *None*) – If `about_point` is `None`, this argument specifies
          the direction of the bounding box point to be taken as
          the rotation center.
        - **kwargs** (*Any*)

    Examples

    Example: UsingRotate

    [
    ](./UsingRotate-1.mp4)

    ```
    class UsingRotate(Scene):
        def construct(self):
            self.play(
                Rotate(
                    Square(side_length=0.5).shift(UP * 2),
                    angle=2*PI,
                    about_point=ORIGIN,
                    rate_func=linear,
                ),
                Rotate(Square(side_length=0.5), angle=2*PI, rate_func=linear),
                )
    ```

    See also

    [`Rotating`](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotating.html), [`rotate()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)

    Methods

    |  |  |
    | --- | --- |
    | `create_target` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *angle=3.141592653589793*, *axis=array([0., 0., 1.])*, *about\_point=None*, *about\_edge=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **angle** (*float*)
            - **axis** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **about\_point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* *None*)
            - **about\_edge** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* *None*)
            - **kwargs** (*Any*)

        Return type:
        :   None
