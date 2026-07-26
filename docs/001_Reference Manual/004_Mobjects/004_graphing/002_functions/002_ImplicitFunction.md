---
{
  "title": "ImplicitFunction",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ImplicitFunction.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "graphing",
    "functions",
    "ImplicitFunction"
  ],
  "scraped_at": "2026-07-10T15:59:34"
}
---

# ImplicitFunction

Qualified name: `manim.mobject.graphing.functions.ImplicitFunction`

class ImplicitFunction(*func*, *x\_range=None*, *y\_range=None*, *min\_depth=5*, *max\_quads=1500*, *use\_smoothing=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/functions.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    An implicit function.

    Parameters:
    :   - **func** (*Callable**[**[**float**,* *float**]**,* *float**]*) – The implicit function in the form `f(x, y) = 0`.
        - **x\_range** (*Sequence**[**float**]* *|* *None*) – The x min and max of the function.
        - **y\_range** (*Sequence**[**float**]* *|* *None*) – The y min and max of the function.
        - **min\_depth** (*int*) – The minimum depth of the function to calculate.
        - **max\_quads** (*int*) – The maximum number of quads to use.
        - **use\_smoothing** (*bool*) – Whether or not to smoothen the curves.
        - **kwargs** (*Any*) – Additional parameters to pass into `VMobject`

    Note

    A small `min_depth` \(d\) means that some small details might
    be ignored if they don’t cross an edge of one of the
    \(4^d\) uniform quads.

    The value of `max_quads` strongly corresponds to the
    quality of the curve, but a higher number of quads
    may take longer to render.

    Examples

    Example: ImplicitFunctionExample

    ![../_images/ImplicitFunctionExample-1.png](https://docs.manim.community/en/stable/_images/ImplicitFunctionExample-1.png)

    ```
    class ImplicitFunctionExample(Scene):
        def construct(self):
            graph = ImplicitFunction(
                lambda x, y: x * y ** 2 - x ** 2 * y - 2,
                color=YELLOW
            )
            self.add(NumberPlane(), graph)
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.graphing.functions.ImplicitFunction.generate_points) | Initializes `points` and therefore the shape. |
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

    \_original\_\_init\_\_(*func*, *x\_range=None*, *y\_range=None*, *min\_depth=5*, *max\_quads=1500*, *use\_smoothing=True*, *\*\*kwargs*)
    :   An implicit function.

        Parameters:
        :   - **func** (*Callable**[**[**float**,* *float**]**,* *float**]*) – The implicit function in the form `f(x, y) = 0`.
            - **x\_range** (*Sequence**[**float**]* *|* *None*) – The x min and max of the function.
            - **y\_range** (*Sequence**[**float**]* *|* *None*) – The y min and max of the function.
            - **min\_depth** (*int*) – The minimum depth of the function to calculate.
            - **max\_quads** (*int*) – The maximum number of quads to use.
            - **use\_smoothing** (*bool*) – Whether or not to smoothen the curves.
            - **kwargs** (*Any*) – Additional parameters to pass into `VMobject`

        Note

        A small `min_depth` \(d\) means that some small details might
        be ignored if they don’t cross an edge of one of the
        \(4^d\) uniform quads.

        The value of `max_quads` strongly corresponds to the
        quality of the curve, but a higher number of quads
        may take longer to render.

        Examples

        Example: ImplicitFunctionExample

        ![../_images/ImplicitFunctionExample-2.png](https://docs.manim.community/en/stable/_images/ImplicitFunctionExample-2.png)

        ```
        class ImplicitFunctionExample(Scene):
            def construct(self):
                graph = ImplicitFunction(
                    lambda x, y: x * y ** 2 - x ** 2 * y - 2,
                    color=YELLOW
                )
                self.add(NumberPlane(), graph)
        ```

    generate\_points()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/functions.html)
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   Self
