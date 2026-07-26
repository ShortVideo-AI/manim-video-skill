---
{
  "title": "fading",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.fading.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "fading"
  ],
  "scraped_at": "2026-07-10T15:57:48"
}
---

# fading

Fading in and out of view.

Example: Fading

[
](./Fading-1.mp4)

```
class Fading(Scene):
    def construct(self):
        tex_in = Tex("Fade", "In").scale(3)
        tex_out = Tex("Fade", "Out").scale(3)
        self.play(FadeIn(tex_in, shift=DOWN, scale=0.66))
        self.play(ReplacementTransform(tex_in, tex_out))
        self.play(FadeOut(tex_out, shift=DOWN * 2, scale=1.5))
```

Classes

| Name | Description |
| --- | --- |
| [`FadeIn`](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeIn.html) | Fade in [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) s. |
| [`FadeOut`](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html) | Fade out [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) s. |
