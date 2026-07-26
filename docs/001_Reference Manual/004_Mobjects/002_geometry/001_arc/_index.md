---
{
  "title": "arc",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "arc"
  ],
  "scraped_at": "2026-07-10T15:58:42"
}
---

# arc

Mobjects that are curved.

Examples

Example: UsefulAnnotations

![../_images/UsefulAnnotations-1.png](https://docs.manim.community/en/stable/_images/UsefulAnnotations-1.png)

```
class UsefulAnnotations(Scene):
    def construct(self):
        m0 = Dot()
        m1 = AnnotationDot()
        m2 = LabeledDot("ii")
        m3 = LabeledDot(MathTex(r"\alpha").set_color(ORANGE))
        m4 = CurvedArrow(2*LEFT, 2*RIGHT, radius= -5)
        m5 = CurvedArrow(2*LEFT, 2*RIGHT, radius= 8)
        m6 = CurvedDoubleArrow(ORIGIN, 2*RIGHT)

        self.add(m0, m1, m2, m3, m4, m5, m6)
        for i, mobj in enumerate(self.mobjects):
            mobj.shift(DOWN * (i-3))
```

Classes

| Name | Description |
| --- | --- |
| [`AnnotationDot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.AnnotationDot.html) | A dot with bigger radius and bold stroke to annotate scenes. |
| [`AnnularSector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.AnnularSector.html) | A sector of an annulus. |
| [`Annulus`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Annulus.html) | Region between two concentric [`Circles`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html). |
| [`Arc`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html) | A circular arc. |
| [`ArcBetweenPoints`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcBetweenPoints.html) | Inherits from Arc and additionally takes 2 points between which the arc is spanned. |
| [`ArcPolygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcPolygon.html) | A generalized polygon allowing for points to be connected with arcs. |
| [`ArcPolygonFromArcs`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcPolygonFromArcs.html) | A generalized polygon allowing for points to be connected with arcs. |
| [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html) | A circle. |
| [`CubicBezier`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CubicBezier.html) | A cubic Bézier curve. |
| [`CurvedArrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CurvedArrow.html) |  |
| [`CurvedDoubleArrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CurvedDoubleArrow.html) |  |
| [`Dot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html) | A circle with a very small radius. |
| [`Ellipse`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Ellipse.html) | A circular shape; oval, circle. |
| [`LabeledDot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.LabeledDot.html) | A [`Dot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html) containing a label in its center. |
| [`Sector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Sector.html) | A sector of a circle. |
| [`TangentialArc`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.TangentialArc.html) | Construct an arc that is tangent to two intersecting lines. |
| [`TipableVMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.TipableVMobject.html) | Meant for shared functionality between Arc and Line. |
