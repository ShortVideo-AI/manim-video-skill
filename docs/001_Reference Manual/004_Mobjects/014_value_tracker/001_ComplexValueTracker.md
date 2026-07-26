---
{
  "title": "ComplexValueTracker",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "value_tracker",
    "ComplexValueTracker"
  ],
  "scraped_at": "2026-07-10T16:00:39"
}
---

# ComplexValueTracker

Qualified name: `manim.mobject.value\_tracker.ComplexValueTracker`

class ComplexValueTracker(*value=0*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/value_tracker.html)
:   Bases: [`ValueTracker`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html)

    Tracks a complex-valued parameter.

    The value is internally stored as a points array [a, b, 0]. This can be accessed directly
    to represent the value geometrically, see the usage example.
    When the value is set through `animate`, the value will take a straight path from the
    source point to the destination point.

    Examples

    Example: ComplexValueTrackerExample

    [
    ](./ComplexValueTrackerExample-1.mp4)

    ```
    class ComplexValueTrackerExample(Scene):
        def construct(self):
            tracker = ComplexValueTracker(-2+1j)
            dot = Dot().add_updater(
                lambda x: x.move_to(tracker.points)
            )

            self.add(NumberPlane(), dot)

            self.play(tracker.animate.set_value(3+2j))
            self.play(tracker.animate.set_value(tracker.get_value() * 1j))
            self.play(tracker.animate.set_value(tracker.get_value() - 2j))
            self.play(tracker.animate.set_value(tracker.get_value() / (-2 + 3j)))
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`get_value`](#manim.mobject.value_tracker.ComplexValueTracker.get_value) | Get the current value of this ComplexValueTracker as a complex number. |
    | [`set_value`](#manim.mobject.value_tracker.ComplexValueTracker.set_value) | Sets a new complex value to the ComplexValueTracker. |

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `depth` | The depth of the mobject. |
    | `height` | The height of the mobject. |
    | `width` | The width of the mobject. |

    Parameters:
    :   - **value** (*float*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*value=0*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **value** (*float*)
            - **kwargs** (*Any*)

        Return type:
        :   None

    get\_value()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/value_tracker.html)
    :   Get the current value of this ComplexValueTracker as a complex number.

        Return type:
        :   complex

    set\_value(*value*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/value_tracker.html)
    :   Sets a new complex value to the ComplexValueTracker.

        Parameters:
        :   **value** (*complex* *|* *float*)

        Return type:
        :   Self
