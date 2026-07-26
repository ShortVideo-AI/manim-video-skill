---
{
  "title": "Tetrahedron",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "three_d",
    "polyhedra",
    "Tetrahedron"
  ],
  "scraped_at": "2026-07-10T16:00:15"
}
---

# Tetrahedron

Qualified name: `manim.mobject.three\_d.polyhedra.Tetrahedron`

class Tetrahedron(*edge\_length=1*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/polyhedra.html)
:   Bases: [`Polyhedron`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Polyhedron.html)

    A tetrahedron, one of the five platonic solids. It has 4 faces, 6 edges, and 4 vertices.

    Parameters:
    :   - **edge\_length** (*float*) – The length of an edge between any two vertices.
        - **kwargs** (*Any*)

    Examples

    Example: TetrahedronScene

    ![../_images/TetrahedronScene-1.png](https://docs.manim.community/en/stable/_images/TetrahedronScene-1.png)

    ```
    class TetrahedronScene(ThreeDScene):
        def construct(self):
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            obj = Tetrahedron()
            self.add(obj)
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
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*edge\_length=1*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **edge\_length** (*float*)
            - **kwargs** (*Any*)
