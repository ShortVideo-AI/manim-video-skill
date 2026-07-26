---
{
  "title": "BraceBetweenPoints",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "svg",
    "brace",
    "BraceBetweenPoints"
  ],
  "scraped_at": "2026-07-10T15:59:53"
}
---

# BraceBetweenPoints

Qualified name: `manim.mobject.svg.brace.BraceBetweenPoints`

class BraceBetweenPoints(*point\_1*, *point\_2*, *direction=array([0., 0., 0.])*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/svg/brace.html)
:   Bases: [`Brace`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.Brace.html)

    Similar to Brace, but instead of taking a mobject it uses 2
    points to place the brace.

    A fitting direction for the brace is
    computed, but it still can be manually overridden.
    If the points go from left to right, the brace is drawn from below.
    Swapping the points places the brace on the opposite side.

    Parameters:
    :   - **point\_1** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The first point.
        - **point\_2** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The second point.
        - **direction** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The direction from which the brace faces towards the points.
        - **kwargs** (*Any*)

    Examples

    Example: BraceBPExample

    [
    ](./BraceBPExample-1.mp4)

    ```
    class BraceBPExample(Scene):
        def construct(self):
            p1 = [0,0,0]
            p2 = [1,2,0]
            brace = BraceBetweenPoints(p1,p2)
            self.play(Create(NumberPlane()))
            self.play(Create(brace))
            self.wait(2)
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*point\_1*, *point\_2*, *direction=array([0., 0., 0.])*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **point\_1** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **point\_2** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **direction** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **kwargs** (*Any*)
