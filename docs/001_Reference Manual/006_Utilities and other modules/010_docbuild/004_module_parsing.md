---
{
  "title": "module_parsing",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "docbuild",
    "module_parsing"
  ],
  "scraped_at": "2026-07-10T16:01:32"
}
---

# module\_parsing

Read and parse all the Manim modules and extract documentation from them.

Type Aliases

class AliasInfo
:   ```
    dict[str, str]
    ```

    Dictionary with a definition key containing the definition of
    a `TypeAlias` as a string, and optionally a doc key containing
    the documentation for that alias, if it exists.

class AliasCategoryDict
:   ```
    dict[str, AliasInfo]
    ```

    Dictionary which holds an [`AliasInfo`](#manim.utils.docbuild.module_parsing.AliasInfo) for every alias name in a same
    category.

class ModuleLevelAliasDict
:   ```
    dict[str, AliasCategoryDict]
    ```

    Dictionary containing every `TypeAlias` defined in a module,
    classified by category in different [`AliasCategoryDict`](#manim.utils.docbuild.module_parsing.AliasCategoryDict) objects.

class ModuleTypeVarDict
:   ```
    dict[str, str]
    ```

    Dictionary containing every `TypeVar` defined in a module.

class AliasDocsDict
:   ```
    dict[str, ModuleLevelAliasDict]
    ```

    Dictionary which, for every module in Manim, contains documentation
    about their module-level attributes which are explicitly defined as
    `TypeAlias`, separating them from the rest of attributes.

class DataDict
:   ```
    dict[str, list[str]]
    ```

    Type for a dictionary which, for every module, contains a list with
    the names of all their DOCUMENTED module-level attributes (identified
    by Sphinx via the `data` role, hence the name) which are NOT
    explicitly defined as `TypeAlias`.

class TypeVarDict
:   ```
    dict[str, ModuleTypeVarDict]
    ```

    A dictionary mapping module names to dictionaries of `TypeVar` objects.

Functions

parse\_module\_attributes()[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/docbuild/module_parsing.html)
:   Read all files, generate Abstract Syntax Trees from them, and
    extract useful information about the type aliases defined in the
    files: the category they belong to, their definition and their
    description, separating them from the “regular” module attributes.

    Returns:
    :   - **ALIAS\_DOCS\_DICT** ([`AliasDocsDict`](#manim.utils.docbuild.module_parsing.AliasDocsDict)) – A dictionary containing the information from all the type
          aliases in Manim. See [`AliasDocsDict`](#manim.utils.docbuild.module_parsing.AliasDocsDict) for more information.
        - **DATA\_DICT** ([`DataDict`](#manim.utils.docbuild.module_parsing.DataDict)) – A dictionary containing the names of all DOCUMENTED
          module-level attributes which are not a `TypeAlias`.
        - **TYPEVAR\_DICT** ([`TypeVarDict`](#manim.utils.docbuild.module_parsing.TypeVarDict)) – A dictionary containing the definitions of `TypeVar` objects,
          organized by modules.

    Return type:
    :   tuple[TypeAliasForwardRef(‘~manim.utils.docbuild.module\_parsing.AliasDocsDict’), TypeAliasForwardRef(‘~manim.utils.docbuild.module\_parsing.DataDict’), TypeAliasForwardRef(‘~manim.utils.docbuild.module\_parsing.TypeVarDict’)]
