---
{
  "title": "ZoomedScene",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html",
  "tree_path": [
    "Reference Manual",
    "Scenes",
    "zoomed_scene",
    "ZoomedScene"
  ],
  "scraped_at": "2026-07-10T16:00:58"
}
---

# ZoomedScene

Qualified name: `manim.scene.zoomed\_scene.ZoomedScene`

class ZoomedScene(*camera\_class=<class 'manim.camera.multi\_camera.MultiCamera'>*, *zoomed\_display\_height=3*, *zoomed\_display\_width=3*, *zoomed\_display\_center=None*, *zoomed\_display\_corner=array([1.*, *1.*, *0.])*, *zoomed\_display\_corner\_buff=0.5*, *zoomed\_camera\_config={'background\_opacity': 1*, *'default\_frame\_stroke\_width': 2}*, *zoomed\_camera\_image\_mobject\_config={}*, *zoomed\_camera\_frame\_starting\_position=array([0.*, *0.*, *0.])*, *zoom\_factor=0.15*, *image\_frame\_stroke\_width=3*, *zoom\_activated=False*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html)
:   Bases: [`MovingCameraScene`](https://docs.manim.community/en/stable/reference/manim.scene.moving_camera_scene.MovingCameraScene.html)

    This is a Scene with special configurations made for when
    a particular part of the scene must be zoomed in on and displayed
    separately.

    Methods

    |  |  |
    | --- | --- |
    | [`activate_zooming`](#manim.scene.zoomed_scene.ZoomedScene.activate_zooming) | This method is used to activate the zooming for the zoomed\_camera. |
    | [`get_zoom_factor`](#manim.scene.zoomed_scene.ZoomedScene.get_zoom_factor) | Returns the Zoom factor of the Zoomed camera. |
    | [`get_zoom_in_animation`](#manim.scene.zoomed_scene.ZoomedScene.get_zoom_in_animation) | Returns the animation of camera zooming in. |
    | [`get_zoomed_display_pop_out_animation`](#manim.scene.zoomed_scene.ZoomedScene.get_zoomed_display_pop_out_animation) | This is the animation of the popping out of the mini-display that shows the content of the zoomed camera. |
    | [`setup`](#manim.scene.zoomed_scene.ZoomedScene.setup) | This method is used internally by Manim to setup the scene for proper use. |

    Attributes

    |  |  |
    | --- | --- |
    | `camera` |  |
    | `time` | The time since the start of the scene. |

    Parameters:
    :   - **camera\_class** (*type**[*[*Camera*](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html)*]*)
        - **zoomed\_display\_height** (*float*)
        - **zoomed\_display\_width** (*float*)
        - **zoomed\_display\_center** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* *None*)
        - **zoomed\_display\_corner** ([*Vector3D*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **zoomed\_display\_corner\_buff** (*float*)
        - **zoomed\_camera\_config** (*dict**[**str**,* *Any**]*)
        - **zoomed\_camera\_image\_mobject\_config** (*dict**[**str**,* *Any**]*)
        - **zoomed\_camera\_frame\_starting\_position** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **zoom\_factor** (*float*)
        - **image\_frame\_stroke\_width** (*float*)
        - **zoom\_activated** (*bool*)
        - **kwargs** (*Any*)

    activate\_zooming(*animate=False*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html)
    :   This method is used to activate the zooming for the zoomed\_camera.

        Parameters:
        :   **animate** (*bool*) – Whether or not to animate the activation
            of the zoomed camera.

        Return type:
        :   None

    get\_zoom\_factor()[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html)
    :   Returns the Zoom factor of the Zoomed camera.

        Defined as the ratio between the height of the zoomed camera and
        the height of the zoomed mini display.

        Returns:
        :   The zoom factor.

        Return type:
        :   float

    get\_zoom\_in\_animation(*run\_time=2*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html)
    :   Returns the animation of camera zooming in.

        Parameters:
        :   - **run\_time** (*float*) – The run\_time of the animation of the camera zooming in.
            - **\*\*kwargs** (*Any*) – Any valid keyword arguments of ApplyMethod()

        Returns:
        :   The animation of the camera zooming in.

        Return type:
        :   [ApplyMethod](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html)

    get\_zoomed\_display\_pop\_out\_animation(*\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html)
    :   This is the animation of the popping out of the mini-display that
        shows the content of the zoomed camera.

        Returns:
        :   The Animation of the Zoomed Display popping out.

        Return type:
        :   [ApplyMethod](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html)

        Parameters:
        :   **kwargs** (*Any*)

    setup()[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html)
    :   This method is used internally by Manim to
        setup the scene for proper use.

        Return type:
        :   None
