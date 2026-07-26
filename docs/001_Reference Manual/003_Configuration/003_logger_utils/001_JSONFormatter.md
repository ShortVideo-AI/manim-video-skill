---
{
  "title": "JSONFormatter",
  "source_url": "https://docs.manim.community/en/stable/reference/manim._config.logger_utils.JSONFormatter.html",
  "tree_path": [
    "Reference Manual",
    "Configuration",
    "logger_utils",
    "JSONFormatter"
  ],
  "scraped_at": "2026-07-10T15:58:39"
}
---

# JSONFormatter

Qualified name: `manim.\_config.logger\_utils.JSONFormatter`

class JSONFormatter(*fmt=None*, *datefmt=None*, *style='%'*, *validate=True*, *\**, *defaults=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/logger_utils.html)
:   Bases: `Formatter`

    A formatter that outputs logs in a custom JSON format.

    This class is used internally for testing purposes.

    Initialize the formatter with specified format strings.

    Initialize the formatter either with the specified format string, or a
    default as described above. Allow for specialized date formatting with
    the optional datefmt argument. If datefmt is omitted, you get an
    ISO8601-like (or RFC 3339-like) format.

    Use a style parameter of ‘%’, ‘{’ or ‘$’ to specify that you want to
    use one of %-formatting, `str.format()` (`{}`) formatting or
    `string.Template` formatting in your format string.

    Changed in version 3.2: Added the `style` parameter.

    Methods

    |  |  |
    | --- | --- |
    | [`format`](#manim._config.logger_utils.JSONFormatter.format) | Format the record in a custom JSON format. |

    Attributes

    |  |  |
    | --- | --- |
    | `default_msec_format` |  |
    | `default_time_format` |  |

    format(*record*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/logger_utils.html)
    :   Format the record in a custom JSON format.

        Parameters:
        :   **record** (*LogRecord*)

        Return type:
        :   str
