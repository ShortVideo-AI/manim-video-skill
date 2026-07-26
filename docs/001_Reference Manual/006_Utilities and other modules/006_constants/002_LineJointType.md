---
{
  "title": "LineJointType",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.constants.LineJointType.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "constants",
    "LineJointType"
  ],
  "scraped_at": "2026-07-10T16:01:21"
}
---

# LineJointType

Qualified name: `manim.constants.LineJointType`

class LineJointType(*\*values*)[[source]](https://docs.manim.community/en/stable/_modules/manim/constants.html)
:   Bases: `Enum`

    Collection of available line joint types.

    See the example below for a visual illustration of the different
    joint types.

    Examples

    Example: LineJointVariants

    ![../_images/LineJointVariants-1.png](https://docs.manim.community/en/stable/_images/LineJointVariants-1.png)

    ```
    class LineJointVariants(Scene):
        def construct(self):
            mob = VMobject(stroke_width=20, color=GREEN).set_points_as_corners([
                np.array([-2, 0, 0]),
                np.array([0, 0, 0]),
                np.array([-2, 1, 0]),
            ])
            lines = VGroup(*[mob.copy() for _ in range(len(LineJointType))])
            for line, joint_type in zip(lines, LineJointType):
                line.joint_type = joint_type

            lines.arrange(RIGHT, buff=1)
            self.add(lines)
            for line in lines:
                label = Text(line.joint_type.name).next_to(line, DOWN)
                self.add(label)
    ```

    Attributes

    |  |  |
    | --- | --- |
    | `AUTO` |  |
    | `ROUND` |  |
    | `BEVEL` |  |
    | `MITER` |  |
