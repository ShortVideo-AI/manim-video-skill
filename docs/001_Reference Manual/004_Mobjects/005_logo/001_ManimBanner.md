---
{
  "title": "ManimBanner",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "logo",
    "ManimBanner"
  ],
  "scraped_at": "2026-07-10T15:59:41"
}
---

# ManimBanner

Qualified name: `manim.mobject.logo.ManimBanner`

class ManimBanner(*dark\_theme=True*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/logo.html)
:   Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    Convenience class representing Manim’s banner.

    Can be animated using custom methods.

    Parameters:
    :   **dark\_theme** (*bool*) – If `True` (the default), the dark theme version of the logo
        (with light text font) will be rendered. Otherwise, if `False`,
        the light theme version (with dark text font) is used.

    Examples

    Example: DarkThemeBanner

    [
    ](./DarkThemeBanner-1.mp4)

    ```
    class DarkThemeBanner(Scene):
        def construct(self):
            banner = ManimBanner()
            self.play(banner.create())
            self.play(banner.expand())
            self.wait()
            self.play(Unwrite(banner))
    ```

    Example: LightThemeBanner

    [
    ](./LightThemeBanner-1.mp4)

    ```
    class LightThemeBanner(Scene):
        def construct(self):
            self.camera.background_color = "#ece6e2"
            banner = ManimBanner(dark_theme=False)
            self.play(banner.create())
            self.play(banner.expand())
            self.wait()
            self.play(Unwrite(banner))
    ```

    Methods

    |  |  |
    | --- | --- |
    | [`create`](#manim.mobject.logo.ManimBanner.create) | The creation animation for Manim's logo. |
    | [`expand`](#manim.mobject.logo.ManimBanner.expand) | An animation that expands Manim's logo into its banner. |
    | [`scale`](#manim.mobject.logo.ManimBanner.scale) | Scale the banner by the specified scale factor. |

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

    \_original\_\_init\_\_(*dark\_theme=True*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **dark\_theme** (*bool*)

    create(*run\_time=2*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/logo.html)
    :   The creation animation for Manim’s logo.

        Parameters:
        :   **run\_time** (*float*) – The run time of the animation.

        Returns:
        :   An animation to be used in a [`Scene.play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) call.

        Return type:
        :   [`AnimationGroup`](https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html)

    expand(*run\_time=1.5*, *direction='center'*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/logo.html)
    :   An animation that expands Manim’s logo into its banner.

        The returned animation transforms the banner from its initial
        state (representing Manim’s logo with just the icons) to its
        expanded state (showing the full name together with the icons).

        See the class documentation for how to use this.

        Note

        Before calling this method, the text “anim” is not a
        submobject of the banner object. After the expansion,
        it is added as a submobject so subsequent animations
        to the banner object apply to the text “anim” as well.

        Parameters:
        :   - **run\_time** (*float*) – The run time of the animation.
            - **direction** (*str*) – The direction in which the logo is expanded.

        Returns:
        :   An animation to be used in a [`Scene.play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) call.

        Return type:
        :   [`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html)

        Examples

        Example: ExpandDirections

        [
        ](./ExpandDirections-1.mp4)

        ```
        class ExpandDirections(Scene):
            def construct(self):
                banners = [ManimBanner().scale(0.5).shift(UP*x) for x in [-2, 0, 2]]
                self.play(
                    banners[0].expand(direction="right"),
                    banners[1].expand(direction="center"),
                    banners[2].expand(direction="left"),
                )
        ```

    scale(*scale\_factor*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/logo.html)
    :   Scale the banner by the specified scale factor.

        Parameters:
        :   - **scale\_factor** (*float*) – The factor used for scaling the banner.
            - **kwargs** (*Any*)

        Returns:
        :   The scaled banner.

        Return type:
        :   [`ManimBanner`](#manim.mobject.logo.ManimBanner)
