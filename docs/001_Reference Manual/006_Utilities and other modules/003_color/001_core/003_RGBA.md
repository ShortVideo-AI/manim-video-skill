---
{
  "title": "RGBA",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.color.core.RGBA.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "color",
    "core",
    "RGBA"
  ],
  "scraped_at": "2026-07-10T16:01:06"
}
---

# RGBA

Qualified name: `manim.utils.color.core.RGBA`

RGBA
:   RGBA Color Space

    Methods

    |  |  |
    | --- | --- |
    | `contrasting` | Return one of two colors, light or dark (by default white or black), that contrasts with the current color (depending on its luminance). |
    | `darker` | Return a new color that is darker than the current color, i.e. interpolated with `BLACK`. |
    | `from_hex` | Create a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) from a hex string. |
    | `from_hsl` | Create a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) from an HSL array. |
    | `from_hsv` | Create a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) from an HSV array. |
    | `from_rgb` | Create a ManimColor from an RGB array. |
    | `from_rgba` | Create a ManimColor from an RGBA Array. |
    | `gradient` | This method is currently not implemented. |
    | `interpolate` | Interpolate between the current and the given [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html), and return the result. |
    | `into` | Convert the current color into a different colorspace given by `class_type`, without changing the `_internal_value`. |
    | `invert` | Return a new, linearly inverted version of this [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) (no inplace changes). |
    | `lighter` | Return a new color that is lighter than the current color, i.e. interpolated with `WHITE`. |
    | `opacity` | Create a new [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) with the given opacity and the same color values as before. |
    | `parse` | Parse one color as a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) or a sequence of colors as a list of [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)'s. |
    | `to_hex` | Convert the [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) to a hexadecimal representation of the color. |
    | `to_hsl` | Convert the [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) to an HSL array. |
    | `to_hsv` | Convert the [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) to an HSV array. |
    | `to_int_rgb` | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) into an RGB array of integers. |
    | `to_int_rgba` | Convert the current ManimColor into an RGBA array of integers. |
    | `to_int_rgba_with_alpha` | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) into an RGBA array of integers. |
    | `to_integer` | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) into an integer. |
    | `to_rgb` | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) into an RGB array of floats. |
    | `to_rgba` | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) into an RGBA array of floats. |
    | `to_rgba_with_alpha` | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) into an RGBA array of floats. |
