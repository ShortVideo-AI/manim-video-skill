---
{
  "title": "logger_utils",
  "source_url": "https://docs.manim.community/en/stable/reference/manim._config.logger_utils.html",
  "tree_path": [
    "Reference Manual",
    "Configuration",
    "logger_utils"
  ],
  "scraped_at": "2026-07-10T15:58:39"
}
---

# logger\_utils

Utilities to create and set the logger.

Manim’s logger can be accessed as `manim.logger`, or as
`logging.getLogger("manim")`, once the library has been imported. Manim also
exports a second object, `console`, which should be used to print on screen
messages that need not be logged.

Both `logger` and `console` use the `rich` library to produce rich text
format.

Classes

| Name | Description |
| --- | --- |
| [`JSONFormatter`](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.JSONFormatter.html) | A formatter that outputs logs in a custom JSON format. |

Functions

make\_logger(*parser*, *verbosity*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/logger_utils.html)
:   Make the manim logger and console.

    Parameters:
    :   - **parser** (*SectionProxy*) – A parser containing any .cfg files in use.
        - **verbosity** (*str*) – The verbosity level of the logger.

    Returns:
    :   The manim logger and consoles. The first console outputs
        to stdout, the second to stderr. All use the theme returned by
        [`parse_theme()`](#manim._config.logger_utils.parse_theme).

    Return type:
    :   `logging.Logger`, `rich.Console`, `rich.Console`

    See also

    [`make_config_parser()`](https://docs.manim.community/en/stable/reference/manim._config.utils.html), [`parse_theme()`](#manim._config.logger_utils.parse_theme)

    Notes

    The `parser` is assumed to contain only the options related to
    configuring the logger at the top level.

parse\_theme(*parser*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/logger_utils.html)
:   Configure the rich style of logger and console output.

    Parameters:
    :   **parser** (*SectionProxy*) – A parser containing any .cfg files in use.

    Returns:
    :   The rich theme to be used by the manim logger.

    Return type:
    :   `rich.Theme`

    See also

    [`make_logger()`](#manim._config.logger_utils.make_logger)

set\_file\_logger(*scene\_name*, *module\_name*, *log\_dir*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/logger_utils.html)
:   Add a file handler to manim logger.

    The path to the file is built using `config.log_dir`.

    Parameters:
    :   - **scene\_name** (*str*) – The name of the scene, used in the name of the log file.
        - **module\_name** (*str*) – The name of the module, used in the name of the log file.
        - **log\_dir** (*Path*) – Path to the folder where log files are stored.

    Return type:
    :   None
