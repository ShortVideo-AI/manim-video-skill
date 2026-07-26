---
{
  "title": "RendererType",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.constants.RendererType.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "constants",
    "RendererType"
  ],
  "scraped_at": "2026-07-10T16:01:22"
}
---

# RendererType

Qualified name: `manim.constants.RendererType`

class RendererType(*\*values*)[[source]](https://docs.manim.community/en/stable/_modules/manim/constants.html)
:   Bases: `Enum`

    An enumeration of all renderer types that can be assigned to
    the `config.renderer` attribute.

    Manim’s configuration allows assigning string values to the renderer
    setting, the values are then replaced by the corresponding enum object.
    In other words, you can run:

    ```
    config.renderer = "opengl"
    ```

    and checking the renderer afterwards reveals that the attribute has
    assumed the value:

    ```
    <RendererType.OPENGL: 'opengl'>
    ```

    Attributes

    |  |  |
    | --- | --- |
    | [`CAIRO`](#manim.constants.RendererType.CAIRO) | A renderer based on the cairo backend. |
    | [`OPENGL`](#manim.constants.RendererType.OPENGL) | An OpenGL-based renderer. |

    CAIRO = 'cairo'
    :   A renderer based on the cairo backend.

    OPENGL = 'opengl'
    :   An OpenGL-based renderer.
