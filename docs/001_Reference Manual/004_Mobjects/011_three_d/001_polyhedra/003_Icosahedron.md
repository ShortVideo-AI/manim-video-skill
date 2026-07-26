---
{
  "title": "Icosahedron",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Icosahedron.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "three_d",
    "polyhedra",
    "Icosahedron"
  ],
  "scraped_at": "2026-07-10T16:00:13"
}
---

# Icosahedron

Qualified name: `manim.mobject.three\_d.polyhedra.Icosahedron`

class Icosahedron(*edge\_length=1*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/polyhedra.html)
:   Bases: [`Polyhedron`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Polyhedron.html)

    An icosahedron, one of the five platonic solids. It has 20 faces, 30 edges and 12 vertices.

    Parameters:
    :   - **edge\_length** (*float*) – The length of an edge between any two vertices.
        - **kwargs** (*Any*)

    Examples

    Example: IcosahedronScene

    ![../_images/IcosahedronScene-1.png](https://docs.manim.community/en/stable/_images/IcosahedronScene-1.png)

    ```
    class IcosahedronScene(ThreeDScene):
        def construct(self):
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            obj = Icosahedron()
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
