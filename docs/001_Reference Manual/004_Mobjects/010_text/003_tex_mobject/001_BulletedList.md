---
{
  "title": "BulletedList",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.BulletedList.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "text",
    "tex_mobject",
    "BulletedList"
  ],
  "scraped_at": "2026-07-10T16:00:04"
}
---

# BulletedList

Qualified name: `manim.mobject.text.tex\_mobject.BulletedList`

class BulletedList(*\*items*, *buff=0.5*, *dot\_scale\_factor=2*, *tex\_environment=None*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/tex_mobject.html)
:   Bases: [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html)

    A bulleted list.

    Examples

    Example: BulletedListExample

    ![../_images/BulletedListExample-1.png](https://docs.manim.community/en/stable/_images/BulletedListExample-1.png)

    ```
    class BulletedListExample(Scene):
        def construct(self):
            blist = BulletedList("Item 1", "Item 2", "Item 3", height=2, width=2)
            blist.set_color_by_tex("Item 1", RED)
            blist.set_color_by_tex("Item 2", GREEN)
            blist.set_color_by_tex("Item 3", BLUE)
            self.add(blist)
    ```

    Methods

    |  |  |
    | --- | --- |
    | `fade_all_but` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `font_size` | The font size of the tex mobject. |
    | `hash_seed` | A unique hash representing the result of the generated mobject points. |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    Parameters:
    :   - **items** (*str*)
        - **buff** (*float*)
        - **dot\_scale\_factor** (*float*)
        - **tex\_environment** (*str* *|* *None*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*\*items*, *buff=0.5*, *dot\_scale\_factor=2*, *tex\_environment=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **items** (*str*)
            - **buff** (*float*)
            - **dot\_scale\_factor** (*float*)
            - **tex\_environment** (*str* *|* *None*)
            - **kwargs** (*Any*)
