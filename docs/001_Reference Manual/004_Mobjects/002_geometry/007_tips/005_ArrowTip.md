---
{
  "title": "ArrowTip",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowTip.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "tips",
    "ArrowTip"
  ],
  "scraped_at": "2026-07-10T15:59:18"
}
---

# ArrowTip

Qualified name: `manim.mobject.geometry.tips.ArrowTip`

class ArrowTip(*\*args*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/tips.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    Base class for arrow tips.

    See also

    [`ArrowTriangleTip`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowTriangleTip.html)
    [`ArrowTriangleFilledTip`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowTriangleFilledTip.html)
    [`ArrowCircleTip`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowCircleTip.html)
    [`ArrowCircleFilledTip`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowCircleFilledTip.html)
    [`ArrowSquareTip`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowSquareTip.html)
    [`ArrowSquareFilledTip`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowSquareFilledTip.html)
    [`StealthTip`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html)

    Examples

    Cannot be used directly, only intended for inheritance:

    Instead, use one of the pre-defined ones, or make
    a custom one like this:

    Example: CustomTipExample

    [
    ](./CustomTipExample-1.mp4)

    ```
    >>> from manim import RegularPolygon, Arrow
    >>> class MyCustomArrowTip(ArrowTip, RegularPolygon):
    ...     def __init__(self, length=0.35, **kwargs):
    ...         RegularPolygon.__init__(self, n=5, **kwargs)
    ...         self.width = length
    ...         self.stretch_to_fit_height(length)
    >>> arr = Arrow(
    ...     np.array([-2, -2, 0]), np.array([2, 2, 0]), tip_shape=MyCustomArrowTip
    ... )
    >>> isinstance(arr.tip, RegularPolygon)
    True
    >>> from manim import Scene, Create
    >>> class CustomTipExample(Scene):
    ...     def construct(self):
    ...         self.play(Create(arr))
    ```

    Using a class inherited from [`ArrowTip`](#manim.mobject.geometry.tips.ArrowTip) to get a non-filled
    tip is a shorthand to manually specifying the arrow tip style as follows:

    The following example illustrates the usage of all of the predefined
    arrow tips.

    Example: ArrowTipsShowcase

    ![../_images/ArrowTipsShowcase-1.png](https://docs.manim.community/en/stable/_images/ArrowTipsShowcase-1.png)

    ```
    class ArrowTipsShowcase(Scene):
        def construct(self):
            tip_names = [
                'Default (YELLOW)', 'ArrowTriangleTip', 'Default', 'ArrowSquareTip',
                'ArrowSquareFilledTip', 'ArrowCircleTip', 'ArrowCircleFilledTip', 'StealthTip'
            ]

            big_arrows = [
                Arrow(start=[-4, 3.5, 0], end=[2, 3.5, 0], color=YELLOW),
                Arrow(start=[-4, 2.5, 0], end=[2, 2.5, 0], tip_shape=ArrowTriangleTip),
                Arrow(start=[-4, 1.5, 0], end=[2, 1.5, 0]),
                Arrow(start=[-4, 0.5, 0], end=[2, 0.5, 0], tip_shape=ArrowSquareTip),

                Arrow([-4, -0.5, 0], [2, -0.5, 0], tip_shape=ArrowSquareFilledTip),
                Arrow([-4, -1.5, 0], [2, -1.5, 0], tip_shape=ArrowCircleTip),
                Arrow([-4, -2.5, 0], [2, -2.5, 0], tip_shape=ArrowCircleFilledTip),
                Arrow([-4, -3.5, 0], [2, -3.5, 0], tip_shape=StealthTip)
            ]

            small_arrows = (
                arrow.copy().scale(0.5, scale_tips=True).next_to(arrow, RIGHT) for arrow in big_arrows
            )

            labels = (
                Text(tip_names[i], font='monospace', font_size=20, color=BLUE).next_to(big_arrows[i], LEFT) for i in range(len(big_arrows))
            )

            self.add(*big_arrows, *small_arrows, *labels)
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | [`base`](#manim.mobject.geometry.tips.ArrowTip.base) | The base point of the arrow tip. |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | [`length`](#manim.mobject.geometry.tips.ArrowTip.length) | The length of the arrow tip. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | [`tip_angle`](#manim.mobject.geometry.tips.ArrowTip.tip_angle) | The angle of the arrow tip. |
    | [`tip_point`](#manim.mobject.geometry.tips.ArrowTip.tip_point) | The tip point of the arrow tip. |
    | [`vector`](#manim.mobject.geometry.tips.ArrowTip.vector) | The vector pointing from the base point to the tip point. |
    | `width` | The width of the mobject. |

    Parameters:
    :   - **args** (*Any*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*\*args*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **args** (*Any*)
            - **kwargs** (*Any*)

        Return type:
        :   None

    property base: [Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html)
    :   The base point of the arrow tip.

        This is the point connecting to the arrow line.

        Examples

    property length: float
    :   The length of the arrow tip.

        Examples

    property tip\_angle: float
    :   The angle of the arrow tip.

        Examples

    property tip\_point: [Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html)
    :   The tip point of the arrow tip.

        Examples

    property vector: [Vector3D](https://docs.manim.community/en/stable/reference/manim.typing.html)
    :   The vector pointing from the base point to the tip point.

        Examples
