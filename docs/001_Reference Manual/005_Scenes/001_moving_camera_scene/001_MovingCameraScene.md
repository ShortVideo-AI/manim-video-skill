---
{
  "title": "MovingCameraScene",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.scene.moving_camera_scene.MovingCameraScene.html",
  "tree_path": [
    "Reference Manual",
    "Scenes",
    "moving_camera_scene",
    "MovingCameraScene"
  ],
  "scraped_at": "2026-07-10T16:00:46"
}
---

# MovingCameraScene

Qualified name: `manim.scene.moving\_camera\_scene.MovingCameraScene`

class MovingCameraScene(*camera\_class=<class 'manim.camera.moving\_camera.MovingCamera'>*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/moving_camera_scene.html)
:   Bases: [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html)

    This is a Scene, with special configurations and properties that
    make it suitable for cases where the camera must be moved around.

    Note: Examples are included in the moving\_camera\_scene module
    documentation, see below in the ‘see also’ section.

    See also

    [`moving_camera_scene`](https://docs.manim.community/en/stable/reference/manim.scene.moving_camera_scene.html)
    [`MovingCamera`](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html)

    Methods

    |  |  |
    | --- | --- |
    | [`get_moving_mobjects`](#manim.scene.moving_camera_scene.MovingCameraScene.get_moving_mobjects) | This method returns a list of all of the Mobjects in the Scene that are moving, that are also in the animations passed. |

    Attributes

    |  |  |
    | --- | --- |
    | `camera` |  |
    | `time` | The time since the start of the scene. |

    Parameters:
    :   - **camera\_class** (*type**[*[*Camera*](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html)*]*)
        - **kwargs** (*Any*)

    get\_moving\_mobjects(*\*animations*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/moving_camera_scene.html)
    :   This method returns a list of all of the Mobjects in the Scene that
        are moving, that are also in the animations passed.

        Parameters:
        :   **\*animations** ([*Animation*](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html)) – The Animations whose mobjects will be checked.

        Return type:
        :   list[[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)]
