---
{
  "title": "autoaliasattr_directive",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.docbuild.autoaliasattr_directive.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "docbuild",
    "autoaliasattr_directive"
  ],
  "scraped_at": "2026-07-10T16:01:26"
}
---

# autoaliasattr\_directive

A directive for documenting type aliases and other module-level attributes.

Classes

| Name | Description |
| --- | --- |
| [`AliasAttrDocumenter`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.autoaliasattr_directive.AliasAttrDocumenter.html) | Directive which replaces Sphinx's Autosummary for module-level attributes: instead, it manually crafts a new "Type Aliases" section, where all the module-level attributes which are explicitly annotated as `TypeAlias` are considered as such, for their use all around the Manim docs. |

Functions

setup(*app*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/docbuild/autoaliasattr_directive.html)
:   Parameters:
    :   **app** (*Sphinx*)

    Return type:
    :   None

smart\_replace(*base*, *alias*, *substitution*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/docbuild/autoaliasattr_directive.html)
:   Auxiliary function for substituting type aliases into a base
    string, when there are overlaps between the aliases themselves.

    Parameters:
    :   - **base** (*str*) – The string in which the type aliases will be located and
          replaced.
        - **alias** (*str*) – The substring to be substituted.
        - **substitution** (*str*) – The string which will replace every occurrence of `alias`.

    Returns:
    :   The new string after the alias substitution.

    Return type:
    :   str
