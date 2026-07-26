---
{
  "title": "ApplyMethod",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html",
  "tree_path": [
    "Reference Manual",
    "Animations",
    "transform",
    "ApplyMethod"
  ],
  "scraped_at": "2026-07-10T15:58:12"
}
---

# ApplyMethod

Qualified name: `manim.animation.transform.ApplyMethod`

class ApplyMethod(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html)
:   Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html)

    Animates a mobject by applying a method.

    Note that only the method needs to be passed to this animation,
    it is not required to pass the corresponding mobject. Furthermore,
    this animation class only works if the method returns the modified
    mobject.

    Parameters:
    :   - **method** (*Callable*) – The method that will be applied in the animation.
        - **args** – Any positional arguments to be passed when applying the method.
        - **kwargs** – Any keyword arguments passed to [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html).

    Methods

    |  |  |
    | --- | --- |
    | `check_validity_of_input` |  |
    | `create_target` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*method*, *\*args*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **method** (*Callable*)

        Return type:
        :   None
