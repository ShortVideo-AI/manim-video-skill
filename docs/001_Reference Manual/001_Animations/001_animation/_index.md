---
{
  "title": "animation",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.animation.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "animation"
  ],
  "scraped_at": "2026-07-10T15:57:33"
}
---

# animation

Animate mobjects.

Classes

| Name | Description |
| --- | --- |
| [`Add`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html) | Add Mobjects to a scene, without animating them in any other way. |
| [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html) | An animation. |
| [`Wait`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html) | A "no operation" animation. |

Functions

override\_animation(*animation\_class*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
:   Decorator used to mark methods as overrides for specific [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html) types.

    Should only be used to decorate methods of classes derived from [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html).
    `Animation` overrides get inherited to subclasses of the `Mobject` who defined
    them. They don’t override subclasses of the `Animation` they override.

    See also

    [`add_animation_override()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)

    Parameters:
    :   **animation\_class** (*type**[*[*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)*]*) – The animation to be overridden.

    Returns:
    :   The actual decorator. This marks the method as overriding an animation.

    Return type:
    :   Callable[[Callable], Callable]

    Examples

    Example: OverrideAnimationExample

    [
    ](./OverrideAnimationExample-1.mp4)

    ```
    class MySquare(Square):
        @override_animation(FadeIn)
        def _fade_in_override(self, **kwargs):
            return Create(self, **kwargs)

    class OverrideAnimationExample(Scene):
        def construct(self):
            self.play(FadeIn(MySquare()))
    ```

prepare\_animation(*anim*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html)
:   Returns either an unchanged animation, or the animation built
    from a passed animation factory.

    Examples

    Parameters:
    :   **anim** ([*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html) *|* *\_AnimationBuilder* *|* *\_AnimationBuilder*)

    Return type:
    :   [*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)
