---
{
  "title": "Blink",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "indication",
    "Blink"
  ],
  "scraped_at": "2026-07-10T15:57:55"
}
---

# Blink

Qualified name: `manim.animation.indication.Blink`

class Blink(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html)
:   Bases: [`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html)

    Blink the mobject.

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobject to be blinked.
        - **time\_on** (*float*) – The duration that the mobject is shown for one blink.
        - **time\_off** (*float*) – The duration that the mobject is hidden for one blink.
        - **blinks** (*int*) – The number of blinks
        - **hide\_at\_end** (*bool*) – Whether to hide the mobject at the end of the animation.
        - **kwargs** (*Any*) – Additional arguments to be passed to the [`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html) constructor.

    Examples

    Example: BlinkingExample

    [
    ](./BlinkingExample-1.mp4)

    ```
    class BlinkingExample(Scene):
        def construct(self):
            text = Text("Blinking").scale(1.5)
            self.add(text)
            self.play(Blink(text, blinks=3))
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *time\_on=0.5*, *time\_off=0.5*, *blinks=1*, *hide\_at\_end=False*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **time\_on** (*float*)
            - **time\_off** (*float*)
            - **blinks** (*int*)
            - **hide\_at\_end** (*bool*)
            - **kwargs** (*Any*)
