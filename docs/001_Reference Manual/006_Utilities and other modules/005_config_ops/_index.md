---
{
  "title": "config_ops",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.config_ops.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "config_ops"
  ],
  "scraped_at": "2026-07-10T16:01:18"
}
---

# config\_ops

Utilities that might be useful for configuration dictionaries.

TypeVar’s

class \_Data\_T
:   ```
    TypeVar('_Data_T', bound='npt.NDArray[Any]', default='npt.NDArray[Any]')
    ```

class \_Uniforms\_T
:   ```
    TypeVar('_Uniforms_T', bound='float | tuple[float, ...]', default=float)
    ```

Classes

| Name | Description |
| --- | --- |
| [`DictAsObject`](https://docs.manim.community/en/stable/reference/manim.utils.config_ops.DictAsObject.html) |  |

Functions

merge\_dicts\_recursively(*\*dicts*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/config_ops.html)
:   Creates a dict whose keyset is the union of all the
    input dictionaries. The value for each key is based
    on the first dict in the list with that key.

    dicts later in the list have higher priority

    When values are dictionaries, it is applied recursively

    Parameters:
    :   **dicts** (*dict**[**Any**,* *Any**]*)

    Return type:
    :   dict[*Any*, *Any*]

update\_dict\_recursively(*current\_dict*, *\*others*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/config_ops.html)
:   Parameters:
    :   - **current\_dict** (*dict**[**Any**,* *Any**]*)
        - **others** (*dict**[**Any**,* *Any**]*)

    Return type:
    :   None
