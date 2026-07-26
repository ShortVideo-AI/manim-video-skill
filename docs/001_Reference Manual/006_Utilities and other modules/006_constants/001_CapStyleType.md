---
{
  "title": "CapStyleType",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "constants",
    "CapStyleType"
  ],
  "scraped_at": "2026-07-10T16:01:20"
}
---

# CapStyleType

Qualified name: `manim.constants.CapStyleType`

class CapStyleType(*\*values*)[[source]](https://docs.manim.community/en/stable/_modules/manim/constants.html)
:   Bases: `Enum`

    Collection of available cap styles.

    See the example below for a visual illustration of the different
    cap styles.

    Examples

    Example: CapStyleVariants

    ![../_images/CapStyleVariants-1.png](https://docs.manim.community/en/stable/_images/CapStyleVariants-1.png)

    ```
    class CapStyleVariants(Scene):
        def construct(self):
            arcs = VGroup(*[
                Arc(
                    radius=1,
                    start_angle=0,
                    angle=TAU / 4,
                    stroke_width=20,
                    color=GREEN,
                    cap_style=cap_style,
                )
                for cap_style in CapStyleType
            ])
            arcs.arrange(RIGHT, buff=1)
            self.add(arcs)
            for arc in arcs:
                label = Text(arc.cap_style.name, font_size=24).next_to(arc, DOWN)
                self.add(label)
    ```

    Attributes

    |  |  |
    | --- | --- |
    | `AUTO` |  |
    | `ROUND` |  |
    | `BUTT` |  |
    | `SQUARE` |  |
