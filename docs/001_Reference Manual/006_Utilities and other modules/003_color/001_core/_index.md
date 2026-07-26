---
{
  "title": "core",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.color.core.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "color",
    "core"
  ],
  "scraped_at": "2026-07-10T16:01:04"
}
---

# core

Manim’s (internal) color data structure and some utilities for color conversion.

This module contains the implementation of [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html), the data structure
internally used to represent colors.

The preferred way of using these colors is by importing their constants from Manim:

```
>>> from manim import RED, GREEN, BLUE
>>> print(RED)
#FC6255
```

Note that this way uses the name of the colors in UPPERCASE.

Note

The colors with a `_C` suffix have an alias equal to the colorname without a
letter. For example, `GREEN = GREEN_C`.

## Custom Color Spaces

Hello, dear visitor. You seem to be interested in implementing a custom color class for
a color space we don’t currently support.

The current system is using a few indirections for ensuring a consistent behavior with
all other color types in Manim.

To implement a custom color space, you must subclass [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) and implement
three important methods:

- [`_internal_value`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html): a `@property` implemented on
  [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) with the goal of keeping a consistent internal representation
  which can be referenced by other functions in [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html). This property acts
  as a proxy to whatever representation you need in your class.

  - The getter should always return a NumPy array in the format `[r,g,b,a]`, in
    accordance with the type `ManimColorInternal`.
  - The setter should always accept a value in the format `[r,g,b,a]` which can be
    converted to whatever attributes you need.
- [`_internal_space`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html): a read-only `@property` implemented on
  [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) with the goal of providing a useful representation which can be
  used by operators, interpolation and color transform functions.

  The only constraints on this value are:

  - It must be a NumPy array.
  - The last value must be the opacity in a range `0.0` to `1.0`.

  Additionally, your `__init__` must support this format as an initialization value
  without additional parameters to ensure correct functionality of all other methods in
  [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).
- [`_from_internal()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html): a `@classmethod` which converts an
  `[r,g,b,a]` value into suitable parameters for your `__init__` method and calls
  the `cls` parameter.

Type Aliases

class ParsableManimColor
:   ```
    ManimColor | int | str | IntRGBLike | FloatRGBLike | IntRGBALike | FloatRGBALike
    ```

    [`ParsableManimColor`](#manim.utils.color.core.ParsableManimColor) represents all the types which can be parsed
    to a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) in Manim.

TypeVar’s

class ManimColorT
:   ```
    TypeVar('ManimColorT', bound=ManimColor)
    ```

Classes

| Name | Description |
| --- | --- |
| [`HSV`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html) | HSV Color Space |
| [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) | Internal representation of a color. |
| [`RGBA`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.RGBA.html) | RGBA Color Space |
| [`RandomColorGenerator`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.RandomColorGenerator.html) | A generator for producing random colors from a given list of Manim colors, optionally in a reproducible sequence using a seed value. |

Functions

average\_color(*\*colors*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Determine the average color between the given parameters.

    Note

    This operation does not consider the alphas (opacities) of the colors. The
    generated color has an alpha or opacity of 1.0.

    Returns:
    :   The average color of the input.

    Return type:
    :   [ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)

    Parameters:
    :   **colors** ([*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor))

color\_gradient(*reference\_colors*, *length\_of\_output*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Create a list of colors interpolated between the input array of colors with a
    specific number of colors.

    Parameters:
    :   - **reference\_colors** (*Iterable**[**TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)**]*) – The colors to be interpolated between or spread apart.
        - **length\_of\_output** (*int*) – The number of colors that the output should have, ideally more than the input.

    Returns:
    :   A list of interpolated [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)’s.

    Return type:
    :   list[[ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)]

color\_to\_int\_rgb(*color*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.to_int_rgb()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).

    Parameters:
    :   **color** ([*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor)) – A color to convert to an RGB integer array.

    Returns:
    :   The corresponding RGB integer array.

    Return type:
    :   RGB\_Array\_Int

color\_to\_int\_rgba(*color*, *alpha=1.0*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.to_int_rgba_with_alpha()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).

    Parameters:
    :   - **color** ([*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor)) – A color to convert to an RGBA integer array.
        - **alpha** (*float*) – An alpha value between 0.0 and 1.0 to be used as opacity in the color. Default is
          1.0.

    Returns:
    :   The corresponding RGBA integer array.

    Return type:
    :   RGBA\_Array\_Int

color\_to\_rgb(*color*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Helper function for use in functional style programming.
    Refer to [`ManimColor.to_rgb()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).

    Parameters:
    :   **color** ([*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor)) – A color to convert to an RGB float array.

    Returns:
    :   The corresponding RGB float array.

    Return type:
    :   RGB\_Array\_Float

color\_to\_rgba(*color*, *alpha=1.0*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.to_rgba_with_alpha()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).

    Parameters:
    :   - **color** ([*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor)) – A color to convert to an RGBA float array.
        - **alpha** (*float*) – An alpha value between 0.0 and 1.0 to be used as opacity in the color. Default is
          1.0.

    Returns:
    :   The corresponding RGBA float array.

    Return type:
    :   RGBA\_Array\_Float

get\_shaded\_rgb(*rgb*, *point*, *unit\_normal\_vect*, *light\_source*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Add light or shadow to the `rgb` color of some surface which is located at a
    given `point` in space and facing in the direction of `unit_normal_vect`,
    depending on whether the surface is facing a `light_source` or away from it.

    Parameters:
    :   - **rgb** ([*FloatRGB*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – An RGB array of floats.
        - **point** ([*Point3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The location of the colored surface.
        - **unit\_normal\_vect** ([*Vector3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The direction in which the colored surface is facing.
        - **light\_source** ([*Point3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The location of a light source which might illuminate the surface.

    Returns:
    :   The color with added light or shadow, depending on the direction of the colored
        surface.

    Return type:
    :   RGB\_Array\_Float

hex\_to\_rgb(*hex\_code*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.to_rgb()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).

    Parameters:
    :   **hex\_code** (*str*) – A hex string representing a color.

    Returns:
    :   An RGB array representing the color.

    Return type:
    :   RGB\_Array\_Float

interpolate\_color(*color1*, *color2*, *alpha*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Standalone function to interpolate two ManimColors and get the result. Refer to
    [`ManimColor.interpolate()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).

    Parameters:
    :   - **color1** ([*ManimColorT*](#manim.utils.color.core.ManimColorT)) – The first [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).
        - **color2** ([*ManimColorT*](#manim.utils.color.core.ManimColorT)) – The second [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).
        - **alpha** (*float*) – The alpha value determining the point of interpolation between the colors.

    Returns:
    :   The interpolated ManimColor.

    Return type:
    :   [ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)

invert\_color(*color*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.invert()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)

    Parameters:
    :   **color** ([*ManimColorT*](#manim.utils.color.core.ManimColorT)) – The [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) to invert.

    Returns:
    :   The linearly inverted [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).

    Return type:
    :   [ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)

random\_bright\_color()[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Return a random bright color: a random color averaged with `WHITE`.

    Warning

    This operation is very expensive. Please keep in mind the performance loss.

    Returns:
    :   A random bright [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).

    Return type:
    :   [ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)

random\_color()[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Return a random [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).

    Returns:
    :   A random [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).

    Return type:
    :   [ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)

rgb\_to\_color(*rgb*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.from_rgb()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).

    Parameters:
    :   **rgb** (*TypeAliasForwardRef**(**'~manim.typing.FloatRGBLike'**)* *|* *TypeAliasForwardRef**(**'~manim.typing.IntRGBLike'**)*) – A 3 element iterable.

    Returns:
    :   A ManimColor with the corresponding value.

    Return type:
    :   [ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)

rgb\_to\_hex(*rgb*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.from_rgb()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html) and [`ManimColor.to_hex()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).

    Parameters:
    :   **rgb** (*TypeAliasForwardRef**(**'~manim.typing.FloatRGBLike'**)* *|* *TypeAliasForwardRef**(**'~manim.typing.IntRGBLike'**)*) – A 3 element iterable.

    Returns:
    :   A hex representation of the color.

    Return type:
    :   str

rgba\_to\_color(*rgba*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html)
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.from_rgba()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html).

    Parameters:
    :   **rgba** (*TypeAliasForwardRef**(**'~manim.typing.FloatRGBALike'**)* *|* *TypeAliasForwardRef**(**'~manim.typing.IntRGBALike'**)*) – A 4 element iterable.

    Returns:
    :   A ManimColor with the corresponding value

    Return type:
    :   [ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)
