---
{
  "title": "Title",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Title.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "text",
    "tex_mobject",
    "Title"
  ],
  "scraped_at": "2026-07-10T16:00:07"
}
---

# Title

Qualified name: `manim.mobject.text.tex\_mobject.Title`

class Title(*\*text\_parts*, *include\_underline=True*, *match\_underline\_width\_to\_text=False*, *underline\_buff=0.25*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/tex_mobject.html)
:   Bases: [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html)

    A mobject representing an underlined title.

    Examples

    Example: TitleExample

    ![../_images/TitleExample-1.png](https://docs.manim.community/en/stable/_images/TitleExample-1.png)

    ```
    import manim

    class TitleExample(Scene):
        def construct(self):
            banner = ManimBanner()
            title = Title(f"Manim version {manim.__version__}")
            self.add(banner, title)
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
    | `font_size` | The font size of the tex mobject. |
    | `hash_seed` | A unique hash representing the result of the generated mobject points. |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    Parameters:
    :   - **text\_parts** (*str*)
        - **include\_underline** (*bool*)
        - **match\_underline\_width\_to\_text** (*bool*)
        - **underline\_buff** (*float*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*\*text\_parts*, *include\_underline=True*, *match\_underline\_width\_to\_text=False*, *underline\_buff=0.25*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **text\_parts** (*str*)
            - **include\_underline** (*bool*)
            - **match\_underline\_width\_to\_text** (*bool*)
            - **underline\_buff** (*float*)
            - **kwargs** (*Any*)
