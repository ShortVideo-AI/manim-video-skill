---
{
  "title": "color",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.color.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "color"
  ],
  "scraped_at": "2026-07-10T16:01:03"
}
---

# color

Utilities for working with colors and predefined color constants.

## Color data structure

| Name | Description |
| --- | --- |
| [`core`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html) | Manim's (internal) color data structure and some utilities for color conversion. |

## Predefined colors

There are several predefined colors available in Manim:

- The colors listed in [`color.manim_colors`](https://docs.manim.community/en/stable/reference/manim.utils.color.manim_colors.html) are loaded into
  Manim’s global name space.
- The colors in [`color.AS2700`](https://docs.manim.community/en/stable/reference/manim.utils.color.AS2700.html), [`color.BS381`](https://docs.manim.community/en/stable/reference/manim.utils.color.BS381.html),
  [`color.DVIPSNAMES`](https://docs.manim.community/en/stable/reference/manim.utils.color.DVIPSNAMES.html), [`color.SVGNAMES`](https://docs.manim.community/en/stable/reference/manim.utils.color.SVGNAMES.html), [`color.X11`](https://docs.manim.community/en/stable/reference/manim.utils.color.X11.html) and
  [`color.XKCD`](https://docs.manim.community/en/stable/reference/manim.utils.color.XKCD.html) need to be accessed via their module (which are available
  in Manim’s global name space), or imported separately. For example:

  ```
  >>> from manim import XKCD
  >>> XKCD.AVOCADO
  ManimColor('#90B134')
  ```

  Or, alternatively:

The following modules contain the predefined color constants:

| Name | Description |
| --- | --- |
| [`manim_colors`](https://docs.manim.community/en/stable/reference/manim.utils.color.manim_colors.html) | Colors included in the global name space. |
| [`AS2700`](https://docs.manim.community/en/stable/reference/manim.utils.color.AS2700.html) | Australian Color Standard |
| [`BS381`](https://docs.manim.community/en/stable/reference/manim.utils.color.BS381.html) | British Color Standard |
| [`DVIPSNAMES`](https://docs.manim.community/en/stable/reference/manim.utils.color.DVIPSNAMES.html) | dvips Colors |
| [`SVGNAMES`](https://docs.manim.community/en/stable/reference/manim.utils.color.SVGNAMES.html) | SVG 1.1 Colors |
| [`XKCD`](https://docs.manim.community/en/stable/reference/manim.utils.color.XKCD.html) | Colors from the XKCD Color Name Survey |
| [`X11`](https://docs.manim.community/en/stable/reference/manim.utils.color.X11.html) | X11 Colors |
