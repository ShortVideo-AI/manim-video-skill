---
{
  "title": "utils",
  "source_url": "https://docs.manim.community/en/stable/reference/manim._config.utils.html",
  "tree_path": [
    "Reference Manual",
    "Configuration",
    "utils"
  ],
  "scraped_at": "2026-07-10T15:58:37"
}
---

# utils

Utilities to create and set the config.

The main class exported by this module is [`ManimConfig`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html). This class
contains all configuration options, including frame geometry (e.g. frame
height/width, frame rate), output (e.g. directories, logging), styling
(e.g. background color, transparency), and general behavior (e.g. writing a
movie vs writing a single frame).

See [Configuration](https://docs.manim.community/en/stable/guides/configuration.html) for an introduction to Manim’s configuration system.

Classes

| Name | Description |
| --- | --- |
| [`ManimConfig`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html) | Dict-like class storing all config options. |
| [`ManimFrame`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimFrame.html) |  |

Functions

config\_file\_paths()[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
:   The paths where `.cfg` files will be searched for.

    When manim is first imported, it processes any `.cfg` files it finds. This
    function returns the locations in which these files are searched for. In
    ascending order of precedence, these are: the library-wide config file, the
    user-wide config file, and the folder-wide config file.

    The library-wide config file determines manim’s default behavior. The
    user-wide config file is stored in the user’s home folder, and determines
    the behavior of manim whenever the user invokes it from anywhere in the
    system. The folder-wide config file only affects scenes that are in the
    same folder. The latter two files are optional.

    These files, if they exist, are meant to loaded into a single
    `configparser.ConfigParser` object, and then processed by
    [`ManimConfig`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html).

    Returns:
    :   List of paths which may contain `.cfg` files, in ascending order of
        precedence.

    Return type:
    :   List[`Path`]

    See also

    [`make_config_parser()`](#manim._config.utils.make_config_parser), [`ManimConfig.digest_file()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html), [`ManimConfig.digest_parser()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html)

    Notes

    The location of the user-wide config file is OS-specific.

make\_config\_parser(*custom\_file=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
:   Make a `ConfigParser` object and load any `.cfg` files.

    The user-wide file, if it exists, overrides the library-wide file. The
    folder-wide file, if it exists, overrides the other two.

    The folder-wide file can be ignored by passing `custom_file`. However,
    the user-wide and library-wide config files cannot be ignored.

    Parameters:
    :   **custom\_file** (*TypeAliasForwardRef**(**'~manim.typing.StrPath'**)* *|* *None*) – Path to a custom config file. If used, the folder-wide file in the
        relevant directory will be ignored, if it exists. If None, the
        folder-wide file will be used, if it exists.

    Returns:
    :   A parser containing the config options found in the .cfg files that
        were found. It is guaranteed to contain at least the config options
        found in the library-wide file.

    Return type:
    :   `ConfigParser`

    See also

    [`config_file_paths()`](#manim._config.utils.config_file_paths)
