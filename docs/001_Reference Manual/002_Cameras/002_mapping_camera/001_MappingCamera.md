---
{
  "title": "MappingCamera",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.camera.mapping_camera.MappingCamera.html",
  "tree_path": [
    "Reference Manual",
    "Cameras",
    "mapping_camera",
    "MappingCamera"
  ],
  "scraped_at": "2026-07-10T15:58:31"
}
---

# MappingCamera

Qualified name: `manim.camera.mapping\_camera.MappingCamera`

class MappingCamera(*mapping\_func=<function MappingCamera.<lambda>>*, *min\_num\_curves=50*, *allow\_object\_intrusion=False*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/mapping_camera.html)
:   Bases: [`Camera`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html)

    Parameters:
    :   - **mapping\_func** (*callable*) – Function to map 3D points to new 3D points (identity by default).
        - **min\_num\_curves** (*int*) – Minimum number of curves for VMobjects to avoid visual glitches.
        - **allow\_object\_intrusion** (*bool*) – If True, modifies original mobjects; else works on copies.
        - **kwargs** (*dict*) – Additional arguments passed to Camera base class.

    Methods

    |  |  |
    | --- | --- |
    | [`capture_mobjects`](#manim.camera.mapping_camera.MappingCamera.capture_mobjects) | Capture mobjects for rendering after applying the spatial mapping. |
    | `points_to_pixel_coords` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `background_color` |  |
    | `background_opacity` |  |

    capture\_mobjects(*mobjects*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/mapping_camera.html)
    :   Capture mobjects for rendering after applying the spatial mapping.

        Copies mobjects unless intrusion is allowed, and ensures
        vector objects have enough curves for smooth distortion.
