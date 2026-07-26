---
{
  "title": "images",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.images.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "images"
  ],
  "scraped_at": "2026-07-10T16:01:33"
}
---

# images

Image manipulation utilities.

Functions

change\_to\_rgba\_array(*image*, *dtype='uint8'*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/images.html)
:   Converts an RGB array into RGBA with the alpha value opacity maxed.

    Parameters:
    :   - **image** ([*RGBPixelArray*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **dtype** (*str*)

    Return type:
    :   [*RGBAPixelArray*](https://docs.manim.community/en/stable/reference/manim.typing.html)

drag\_pixels(*frames*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/images.html)
:   Parameters:
    :   **frames** (*Sequence**[*[*PixelArray*](https://docs.manim.community/en/stable/reference/manim.typing.html)*]*)

    Return type:
    :   list[np.ndarray]

get\_full\_raster\_image\_path(*image\_file\_name*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/images.html)
:   Parameters:
    :   **image\_file\_name** (*str* *|* *PurePath*)

    Return type:
    :   *Path*

get\_full\_vector\_image\_path(*image\_file\_name*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/images.html)
:   Parameters:
    :   **image\_file\_name** (*str* *|* *PurePath*)

    Return type:
    :   *Path*

invert\_image(*image*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/images.html)
:   Parameters:
    :   **image** ([*PixelArray*](https://docs.manim.community/en/stable/reference/manim.typing.html))

    Return type:
    :   <module ‘PIL.Image’ from ‘/home/docs/checkouts/readthedocs.org/user\_builds/manimce/envs/stable/lib/python3.13/site-packages/PIL/Image.py’>
