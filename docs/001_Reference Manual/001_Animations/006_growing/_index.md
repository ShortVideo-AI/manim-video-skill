---
{
  "title": "growing",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.growing.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "growing"
  ],
  "scraped_at": "2026-07-10T15:57:50"
}
---

# growing

Animations that introduce mobjects to scene by growing them from points.

Example: Growing

[
](./Growing-1.mp4)

```
class Growing(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        triangle = Triangle()
        arrow = Arrow(LEFT, RIGHT)
        star = Star()

        VGroup(square, circle, triangle).set_x(0).arrange(buff=1.5).set_y(2)
        VGroup(arrow, star).move_to(DOWN).set_x(0).arrange(buff=1.5).set_y(-2)

        self.play(GrowFromPoint(square, ORIGIN))
        self.play(GrowFromCenter(circle))
        self.play(GrowFromEdge(triangle, DOWN))
        self.play(GrowArrow(arrow))
        self.play(SpinInFromNothing(star))
```

Classes

| Name | Description |
| --- | --- |
| [`GrowArrow`](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowArrow.html) | Introduce an [`Arrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html) by growing it from its start toward its tip. |
| [`GrowFromCenter`](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromCenter.html) | Introduce an [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) by growing it from its center. |
| [`GrowFromEdge`](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromEdge.html) | Introduce an [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) by growing it from one of its bounding box edges. |
| [`GrowFromPoint`](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromPoint.html) | Introduce an [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) by growing it from a point. |
| [`SpinInFromNothing`](https://docs.manim.community/en/stable/reference/manim.animation.growing.SpinInFromNothing.html) | Introduce an [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) spinning and growing it from its center. |
