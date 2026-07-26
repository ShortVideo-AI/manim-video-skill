---
{
  "title": "mobject",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "mobject"
  ],
  "scraped_at": "2026-07-10T15:59:46"
}
---

# mobject

Base classes for objects that can be displayed.

Type Aliases

class TimeBasedUpdater
:   ```
    Callable[['Mobject', float], object]
    ```

class NonTimeBasedUpdater
:   ```
    Callable[['Mobject'], object]
    ```

class Updater
:   ```
    NonTimeBasedUpdater | TimeBasedUpdater
    ```

Classes

| Name | Description |
| --- | --- |
| [`Group`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Group.html) | Groups together multiple [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html). |
| [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) | Mathematical Object: base class for objects that can be displayed on screen. |

Functions

override\_animate(*method*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html)
:   Decorator for overriding method animations.

    This allows to specify a method (returning an [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html))
    which is called when the decorated method is used with the `.animate` syntax
    for animating the application of a method.

    See also

    [`animate`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)

    Note

    Overridden methods cannot be combined with normal or other overridden
    methods using method chaining with the `.animate` syntax.

    Examples

    Example: AnimationOverrideExample

    [
    ](./AnimationOverrideExample-1.mp4)

    ```
    class CircleWithContent(VGroup):
        def __init__(self, content):
            super().__init__()
            self.circle = Circle()
            self.content = content
            self.add(self.circle, content)
            content.move_to(self.circle.get_center())

        def clear_content(self):
            self.remove(self.content)
            self.content = None

        @override_animate(clear_content)
        def _clear_content_animation(self, anim_args=None):
            if anim_args is None:
                anim_args = {}
            anim = Uncreate(self.content, **anim_args)
            self.clear_content()
            return anim

    class AnimationOverrideExample(Scene):
        def construct(self):
            t = Text("hello!")
            my_mobject = CircleWithContent(t)
            self.play(Create(my_mobject))
            self.play(my_mobject.animate.clear_content())
            self.wait()
    ```

    Return type:
    :   *LambdaType*
