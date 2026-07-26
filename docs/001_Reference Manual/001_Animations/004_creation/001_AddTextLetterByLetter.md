---
{
  "title": "AddTextLetterByLetter",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.creation.AddTextLetterByLetter.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "creation",
    "AddTextLetterByLetter"
  ],
  "scraped_at": "2026-07-10T15:57:40"
}
---

# AddTextLetterByLetter

Qualified name: `manim.animation.creation.AddTextLetterByLetter`

class AddTextLetterByLetter(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html)
:   Bases: [`ShowIncreasingSubsets`](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowIncreasingSubsets.html)

    Show a [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html) letter by letter on the scene.

    Parameters:
    :   - **time\_per\_char** (*float*) – Frequency of appearance of the letters.
        - **tip::** (*..*) – This is currently only possible for class:~.Text and not for class:~.MathTex
        - **text** ([*Text*](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html))
        - **suspend\_mobject\_updating** (*bool*)
        - **int\_func** (*Callable**[**[**np.ndarray**]**,* *np.ndarray**]*)
        - **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
        - **run\_time** (*float* *|* *None*)

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*text*, *suspend\_mobject\_updating=False*, *int\_func=<ufunc 'ceil'>*, *rate\_func=<function linear>*, *time\_per\_char=0.1*, *run\_time=None*, *reverse\_rate\_function=False*, *introducer=True*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **text** ([*Text*](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html))
            - **suspend\_mobject\_updating** (*bool*)
            - **int\_func** (*Callable**[**[**np.ndarray**]**,* *np.ndarray**]*)
            - **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
            - **time\_per\_char** (*float*)
            - **run\_time** (*float* *|* *None*)

        Return type:
        :   None
