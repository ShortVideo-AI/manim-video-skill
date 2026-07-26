---
{
  "title": "_config",
  "source_url": "https://docs.manim.community/en/stable/reference/manim._config.html",
  "tree_path": [
    "Reference Manual",
    "Configuration",
    "_config"
  ],
  "scraped_at": "2026-07-10T15:58:36"
}
---

# \_config

Set the global config and logger.

Functions

tempconfig(*temp*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config.html)
:   Temporarily modifies the global `config` object using a context manager.

    Inside the `with` statement, the modified config will be used. After
    context manager exits, the config will be restored to its original state.

    Parameters:
    :   **temp** ([*ManimConfig*](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html) *|* *dict**[**str**,* *Any**]*) – Object whose keys will be used to temporarily update the global
        `config`.

    Return type:
    :   *Generator*[None, None, None]

    Examples

    Use `with tempconfig({...})` to temporarily change the default values of
    certain config options.
