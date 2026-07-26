---
{
  "title": "BackgroundColoredVMobjectDisplayer",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.camera.camera.BackgroundColoredVMobjectDisplayer.html",
  "tree_path": [
    "Reference Manual",
    "Cameras",
    "camera",
    "BackgroundColoredVMobjectDisplayer"
  ],
  "scraped_at": "2026-07-10T15:58:29"
}
---

# BackgroundColoredVMobjectDisplayer

Qualified name: `manim.camera.camera.BackgroundColoredVMobjectDisplayer`

class BackgroundColoredVMobjectDisplayer(*camera*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html)
:   Bases: `object`

    Auxiliary class that handles displaying vectorized mobjects with
    a set background image.

    Parameters:
    :   **camera** ([*Camera*](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html)) – Camera object to use.

    Methods

    |  |  |
    | --- | --- |
    | [`display`](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.display) | Displays the colored VMobjects. |
    | [`get_background_array`](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.get_background_array) | Gets the background array that has the passed file\_name. |
    | `reset_pixel_array` |  |
    | [`resize_background_array`](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array) | Resizes the pixel array representing the background. |
    | [`resize_background_array_to_match`](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array_to_match) | Resizes the background array to match the passed pixel array. |

    display(*\*cvmobjects*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html)
    :   Displays the colored VMobjects.

        Parameters:
        :   **\*cvmobjects** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)) – The VMobjects

        Returns:
        :   The pixel array with the cvmobjects displayed.

        Return type:
        :   np.array

    get\_background\_array(*image*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html)
    :   Gets the background array that has the passed file\_name.

        Parameters:
        :   **image** (*Image* *|* *Path* *|* *str*) – The background image or its file name.

        Returns:
        :   The pixel array of the image.

        Return type:
        :   np.ndarray

    resize\_background\_array(*background\_array*, *new\_width*, *new\_height*, *mode='RGBA'*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html)
    :   Resizes the pixel array representing the background.

        Parameters:
        :   - **background\_array** ([*PixelArray*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The pixel
            - **new\_width** (*float*) – The new width of the background
            - **new\_height** (*float*) – The new height of the background
            - **mode** (*str*) – The PIL image mode, by default “RGBA”

        Returns:
        :   The numpy pixel array of the resized background.

        Return type:
        :   np.array

    resize\_background\_array\_to\_match(*background\_array*, *pixel\_array*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html)
    :   Resizes the background array to match the passed pixel array.

        Parameters:
        :   - **background\_array** ([*PixelArray*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The prospective pixel array.
            - **pixel\_array** ([*PixelArray*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The pixel array whose width and height should be matched.

        Returns:
        :   The resized background array.

        Return type:
        :   np.array
