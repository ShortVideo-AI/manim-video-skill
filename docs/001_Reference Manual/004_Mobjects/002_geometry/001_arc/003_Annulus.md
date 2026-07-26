---
{
  "title": "Annulus",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Annulus.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "arc",
    "Annulus"
  ],
  "scraped_at": "2026-07-10T15:58:44"
}
---

# Annulus

Qualified name: `manim.mobject.geometry.arc.Annulus`

class Annulus(*inner\_radius=1*, *outer\_radius=2*, *fill\_opacity=1*, *stroke\_width=0*, *color=ManimColor('#FFFFFF')*, *mark\_paths\_closed=False*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
:   Bases: [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html)

    Region between two concentric [`Circles`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html).

    Parameters:
    :   - **inner\_radius** (*float*) – The radius of the inner [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html).
        - **outer\_radius** (*float*) – The radius of the outer [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html).
        - **kwargs** (*Any*) – Additional arguments to be passed to [`Annulus`](#manim.mobject.geometry.arc.Annulus)
        - **fill\_opacity** (*float*)
        - **stroke\_width** (*float*)
        - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
        - **mark\_paths\_closed** (*bool*)

    Examples

    Example: AnnulusExample

    ![../_images/AnnulusExample-1.png](https://docs.manim.community/en/stable/_images/AnnulusExample-1.png)

    ```
    class AnnulusExample(Scene):
        def construct(self):
            annulus_1 = Annulus(inner_radius=0.5, outer_radius=1).shift(UP)
            annulus_2 = Annulus(inner_radius=0.3, outer_radius=0.6, color=RED).next_to(annulus_1, DOWN)
            self.add(annulus_1, annulus_2)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.geometry.arc.Annulus.generate_points) | Initializes `points` and therefore the shape. |
    | `init_points` |  |

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

    \_original\_\_init\_\_(*inner\_radius=1*, *outer\_radius=2*, *fill\_opacity=1*, *stroke\_width=0*, *color=ManimColor('#FFFFFF')*, *mark\_paths\_closed=False*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **inner\_radius** (*float*)
            - **outer\_radius** (*float*)
            - **fill\_opacity** (*float*)
            - **stroke\_width** (*float*)
            - **color** ([*ParsableManimColor*](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html))
            - **mark\_paths\_closed** (*bool*)
            - **kwargs** (*Any*)

        Return type:
        :   None

    generate\_points()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   None
