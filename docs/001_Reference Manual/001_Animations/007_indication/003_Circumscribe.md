---
{
  "title": "Circumscribe",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "indication",
    "Circumscribe"
  ],
  "scraped_at": "2026-07-10T15:57:56"
}
---

# Circumscribe

Qualified name: `manim.animation.indication.Circumscribe`

class Circumscribe(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html)
:   Bases: [`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html)

    Draw a temporary line surrounding the mobject.

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobject to be circumscribed.
        - **shape** (*type**[*[*Rectangle*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Rectangle.html)*]* *|* *type**[*[*Circle*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html)*]*) – The shape with which to surround the given mobject. Should be either
          [`Rectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Rectangle.html) or [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html)
        - **fade\_in** (*bool*) – Whether to make the surrounding shape to fade in. It will be drawn otherwise.
        - **fade\_out** (*bool*) – Whether to make the surrounding shape to fade out. It will be undrawn otherwise.
        - **time\_width** (*float*) – The time\_width of the drawing and undrawing. Gets ignored if either fade\_in or fade\_out is True.
        - **buff** (*float*) – The distance between the surrounding shape and the given mobject.
        - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html)) – The color of the surrounding shape.
        - **run\_time** (*float*) – The duration of the entire animation.
        - **kwargs** (*Any*) – Additional arguments to be passed to the [`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html) constructor
        - **stroke\_width** (*float*)

    Examples

    Example: UsingCircumscribe

    [
    ](./UsingCircumscribe-1.mp4)

    ```
    class UsingCircumscribe(Scene):
        def construct(self):
            lbl = Tex(r"Circum-\\scribe").scale(2)
            self.add(lbl)
            self.play(Circumscribe(lbl))
            self.play(Circumscribe(lbl, Circle))
            self.play(Circumscribe(lbl, fade_out=True))
            self.play(Circumscribe(lbl, time_width=2))
            self.play(Circumscribe(lbl, Circle, True))
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *shape=<class 'manim.mobject.geometry.polygram.Rectangle'>*, *fade\_in=False*, *fade\_out=False*, *time\_width=0.3*, *buff=0.1*, *color=ManimColor('#FFFF00')*, *run\_time=1*, *stroke\_width=4*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **shape** (*type**[*[*Rectangle*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Rectangle.html)*]* *|* *type**[*[*Circle*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html)*]*)
            - **fade\_in** (*bool*)
            - **fade\_out** (*bool*)
            - **time\_width** (*float*)
            - **buff** (*float*)
            - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
            - **run\_time** (*float*)
            - **stroke\_width** (*float*)
            - **kwargs** (*Any*)
