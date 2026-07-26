---
{
  "title": "commands",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.commands.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "commands"
  ],
  "scraped_at": "2026-07-10T16:01:16"
}
---

# commands

Classes

| Name | Description |
| --- | --- |
| [`VideoMetadata`](https://docs.manim.community/en/stable/reference/manim.utils.commands.VideoMetadata.html) |  |

Functions

capture(*command*, *cwd=None*, *command\_input=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/commands.html)
:   Parameters:
    :   - **command** (*str* *|* *list**[**str**]*)
        - **cwd** (*TypeAliasForwardRef**(**'~manim.typing.StrOrBytesPath'**)* *|* *None*)
        - **command\_input** (*str* *|* *None*)

    Return type:
    :   tuple[str, str, int]

get\_dir\_layout(*dirpath*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/commands.html)
:   Get list of paths relative to dirpath of all files in dir and subdirs recursively.

    Parameters:
    :   **dirpath** (*Path*)

    Return type:
    :   *Generator*[str, None, None]

get\_video\_metadata(*path\_to\_video*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/commands.html)
:   Parameters:
    :   **path\_to\_video** (*str* *|* *PathLike*)

    Return type:
    :   [*VideoMetadata*](https://docs.manim.community/en/stable/reference/manim.utils.commands.VideoMetadata.html)
