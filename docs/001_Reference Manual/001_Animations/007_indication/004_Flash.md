---
{
  "title": "Flash",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.indication.Flash.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "indication",
    "Flash"
  ],
  "scraped_at": "2026-07-10T15:57:56"
}
---

# Flash

Qualified name: `manim.animation.indication.Flash`

class Flash(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html)
:   Bases: [`AnimationGroup`](https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html)

    Send out lines in all directions.

    Parameters:
    :   - **point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* [*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The center of the flash lines. If it is a `Mobject` its center will be used.
        - **line\_length** (*float*) – The length of the flash lines.
        - **num\_lines** (*int*) – The number of flash lines.
        - **flash\_radius** (*float*) – The distance from point at which the flash lines start.
        - **line\_stroke\_width** (*int*) – The stroke width of the flash lines.
        - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html)) – The color of the flash lines.
        - **time\_width** (*float*) – The time width used for the flash lines. See `ShowPassingFlash` for more details.
        - **run\_time** (*float*) – The duration of the animation.
        - **kwargs** (*Any*) – Additional arguments to be passed to the [`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html) constructor

    Examples

    Example: UsingFlash

    [
    ](./UsingFlash-1.mp4)

    ```
    class UsingFlash(Scene):
        def construct(self):
            dot = Dot(color=PURE_YELLOW).shift(DOWN)
            self.add(Tex("Flash the dot below:"), dot)
            self.play(Flash(dot))
            self.wait()
    ```

    Example: FlashOnCircle

    [
    ](./FlashOnCircle-1.mp4)

    ```
    class FlashOnCircle(Scene):
        def construct(self):
            radius = 2
            circle = Circle(radius)
            self.add(circle)
            self.play(Flash(
                circle, line_length=1,
                num_lines=30, color=RED,
                flash_radius=radius+SMALL_BUFF,
                time_width=0.3, run_time=2,
                rate_func = rush_from
            ))
    ```

    Methods

    |  |  |
    | --- | --- |
    | `create_line_anims` |  |
    | `create_lines` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*point*, *line\_length=0.2*, *num\_lines=12*, *flash\_radius=0.1*, *line\_stroke\_width=3*, *color=ManimColor('#FFFF00')*, *time\_width=1*, *run\_time=1.0*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **point** (*TypeAliasForwardRef**(**'~manim.typing.Point3DLike'**)* *|* [*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **line\_length** (*float*)
            - **num\_lines** (*int*)
            - **flash\_radius** (*float*)
            - **line\_stroke\_width** (*int*)
            - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
            - **time\_width** (*float*)
            - **run\_time** (*float*)
            - **kwargs** (*Any*)
