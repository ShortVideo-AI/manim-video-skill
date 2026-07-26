---
{
  "title": "DrawBorderThenFill",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "creation",
    "DrawBorderThenFill"
  ],
  "scraped_at": "2026-07-10T15:57:42"
}
---

# DrawBorderThenFill

Qualified name: `manim.animation.creation.DrawBorderThenFill`

class DrawBorderThenFill(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
:   Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)

    Draw the border first and then show the fill.

    Examples

    Example: ShowDrawBorderThenFill

    [
    ](./ShowDrawBorderThenFill-1.mp4)

    ```
    class ShowDrawBorderThenFill(Scene):
        def construct(self):
            self.play(DrawBorderThenFill(Square(fill_opacity=1, fill_color=ORANGE)))
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`begin`](#manim.animation.creation.DrawBorderThenFill.begin) | Begin the animation. |
    | [`get_all_mobjects`](#manim.animation.creation.DrawBorderThenFill.get_all_mobjects) | Get all mobjects involved in the animation. |
    | `get_outline` |  |
    | `get_stroke_color` |  |
    | `interpolate_submobject` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   - **vmobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* *OpenGLVMobject*)
        - **run\_time** (*float*)
        - **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
        - **stroke\_width** (*float*)
        - **stroke\_color** (*str*)
        - **introducer** (*bool*)

    \_original\_\_init\_\_(*vmobject*, *run\_time=2*, *rate\_func=<function double\_smooth>*, *stroke\_width=2*, *stroke\_color=None*, *introducer=True*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **vmobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) *|* *OpenGLVMobject*)
            - **run\_time** (*float*)
            - **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
            - **stroke\_width** (*float*)
            - **stroke\_color** (*str*)
            - **introducer** (*bool*)

        Return type:
        :   None

    begin()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
    :   Begin the animation.

        This method is called right as an animation is being played. As much
        initialization as possible, especially any mobject copying, should live in this
        method.

        Return type:
        :   None

    get\_all\_mobjects()[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
    :   Get all mobjects involved in the animation.

        Ordering must match the ordering of arguments to interpolate\_submobject

        Returns:
        :   The sequence of mobjects.

        Return type:
        :   Sequence[[Mobject](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)]
