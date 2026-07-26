---
{
  "title": "indication",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.indication.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "indication"
  ],
  "scraped_at": "2026-07-10T15:57:54"
}
---

# indication

Animations drawing attention to particular mobjects.

Examples

Example: Indications

[
](./Indications-1.mp4)

```
class Indications(Scene):
    def construct(self):
        indications = [ApplyWave,Circumscribe,Flash,FocusOn,Indicate,ShowPassingFlash,Wiggle]
        names = [Tex(i.__name__).scale(3) for i in indications]

        self.add(names[0])
        for i in range(len(names)):
            if indications[i] is Flash:
                self.play(Flash(UP))
            elif indications[i] is ShowPassingFlash:
                self.play(ShowPassingFlash(Underline(names[i])))
            else:
                self.play(indications[i](names[i]))
            self.play(AnimationGroup(
                FadeOut(names[i], shift=UP*1.5),
                FadeIn(names[(i+1)%len(names)], shift=UP*1.5),
            ))
```

Classes

| Name | Description |
| --- | --- |
| [`ApplyWave`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ApplyWave.html) | Send a wave through the Mobject distorting it temporarily. |
| [`Blink`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html) | Blink the mobject. |
| [`Circumscribe`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html) | Draw a temporary line surrounding the mobject. |
| [`Flash`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Flash.html) | Send out lines in all directions. |
| [`FocusOn`](https://docs.manim.community/en/stable/reference/manim.animation.indication.FocusOn.html) | Shrink a spotlight to a position. |
| [`Indicate`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Indicate.html) | Indicate a Mobject by temporarily resizing and recoloring it. |
| [`ShowPassingFlash`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html) | Show only a sliver of the VMobject each frame. |
| [`ShowPassingFlashWithThinningStrokeWidth`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth.html) |  |
| [`Wiggle`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Wiggle.html) | Wiggle a Mobject. |
