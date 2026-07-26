---
{
  "title": "Underline",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.Underline.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "shape_matchers",
    "Underline"
  ],
  "scraped_at": "2026-07-10T15:59:14"
}
---

# Underline

Qualified name: `manim.mobject.geometry.shape\_matchers.Underline`

class Underline(*mobject*, *buff=0.1*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/shape_matchers.html)
:   Bases: [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html)

    Creates an underline.

    Examples

    Example: UnderLine

    ![../_images/UnderLine-1.png](https://docs.manim.community/en/stable/_images/UnderLine-1.png)

    ```
    class UnderLine(Scene):
        def construct(self):
            man = Tex("Manim")  # Full Word
            ul = Underline(man)  # Underlining the word
            self.add(man, ul)
    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    Parameters:
    :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
        - **buff** (*float*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*mobject*, *buff=0.1*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **mobject** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html))
            - **buff** (*float*)
            - **kwargs** (*Any*)

        Return type:
        :   None
