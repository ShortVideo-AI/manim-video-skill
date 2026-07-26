---
{
  "title": "TexTemplate",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "tex",
    "TexTemplate"
  ],
  "scraped_at": "2026-07-10T16:01:48"
}
---

# TexTemplate

Qualified name: `manim.utils.tex.TexTemplate`

class TexTemplate(*tex\_compiler='latex'*, *description=''*, *output\_format='.dvi'*, *documentclass='\\documentclass[preview]{standalone}'*, *preamble='\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}'*, *placeholder\_text='YourTextHere'*, *post\_doc\_commands=''*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/tex.html)
:   Bases: `object`

    TeX templates are used to create `Tex` and `MathTex` objects.

    Methods

    |  |  |
    | --- | --- |
    | [`add_to_document`](#manim.utils.tex.TexTemplate.add_to_document) | Adds text to the TeX template just after begin{document}, e.g. `\boldmath`. |
    | [`add_to_preamble`](#manim.utils.tex.TexTemplate.add_to_preamble) | Adds text to the TeX template's preamble (e.g. definitions, packages). |
    | [`copy`](#manim.utils.tex.TexTemplate.copy) | Create a deep copy of the TeX template instance. |
    | [`from_file`](#manim.utils.tex.TexTemplate.from_file) | Create an instance by reading the content of a file. |
    | [`get_texcode_for_expression`](#manim.utils.tex.TexTemplate.get_texcode_for_expression) | Inserts expression verbatim into TeX template. |
    | [`get_texcode_for_expression_in_env`](#manim.utils.tex.TexTemplate.get_texcode_for_expression_in_env) | Inserts expression into TeX template wrapped in `\begin{environment}` and `\end{environment}`. |

    Attributes

    |  |  |
    | --- | --- |
    | [`body`](#manim.utils.tex.TexTemplate.body) | The entire TeX template. |
    | [`description`](#manim.utils.tex.TexTemplate.description) | A description of the template |
    | [`documentclass`](#manim.utils.tex.TexTemplate.documentclass) | The command defining the documentclass, e.g. `\documentclass[preview]{standalone}`. |
    | [`output_format`](#manim.utils.tex.TexTemplate.output_format) | The output format resulting from compilation, e.g. `.dvi` or `.pdf`. |
    | [`placeholder_text`](#manim.utils.tex.TexTemplate.placeholder_text) | Text in the document that will be replaced by the expression to be rendered. |
    | [`post_doc_commands`](#manim.utils.tex.TexTemplate.post_doc_commands) | Text (definitions, commands) to be inserted at right after `\begin{document}`, e.g. `\boldmath`. |
    | [`preamble`](#manim.utils.tex.TexTemplate.preamble) | The document's preamble, i.e. the part between `\documentclass` and `\begin{document}`. |
    | [`tex_compiler`](#manim.utils.tex.TexTemplate.tex_compiler) | The TeX compiler to be used, e.g. `latex`, `pdflatex` or `lualatex`. |

    Parameters:
    :   - **tex\_compiler** (*str*)
        - **description** (*str*)
        - **output\_format** (*str*)
        - **documentclass** (*str*)
        - **preamble** (*str*)
        - **placeholder\_text** (*str*)
        - **post\_doc\_commands** (*str*)

    \_body: str = ''
    :   A custom body, can be set from a file.

    add\_to\_document(*txt*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/tex.html)
    :   Adds text to the TeX template just after begin{document}, e.g. `\boldmath`.

        Parameters:
        :   **txt** (*str*) – String containing the text to be added.

        Return type:
        :   Self

    add\_to\_preamble(*txt*, *prepend=False*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/tex.html)
    :   Adds text to the TeX template’s preamble (e.g. definitions, packages). Text can be inserted at the beginning or at the end of the preamble.

        Parameters:
        :   - **txt** (*str*) – String containing the text to be added, e.g. `\usepackage{hyperref}`.
            - **prepend** (*bool*) – Whether the text should be added at the beginning of the preamble, i.e. right after `\documentclass`.
              Default is to add it at the end of the preamble, i.e. right before `\begin{document}`.

        Return type:
        :   Self

    property body: str
    :   The entire TeX template.

    copy()[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/tex.html)
    :   Create a deep copy of the TeX template instance.

        Return type:
        :   Self

    description: str = ''
    :   A description of the template

    documentclass: str = '\\documentclass[preview]{standalone}'
    :   The command defining the documentclass, e.g. `\documentclass[preview]{standalone}`.

    classmethod from\_file(*file='tex\_template.tex'*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/tex.html)
    :   Create an instance by reading the content of a file.

        Using the `add_to_preamble` and `add_to_document` methods on this instance
        will have no effect, as the body is read from the file.

        Parameters:
        :   - **file** ([*StrPath*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **kwargs** (*Any*)

        Return type:
        :   Self

    get\_texcode\_for\_expression(*expression*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/tex.html)
    :   Inserts expression verbatim into TeX template.

        Parameters:
        :   **expression** (*str*) – The string containing the expression to be typeset, e.g. `$\sqrt{2}$`

        Returns:
        :   LaTeX code based on current template, containing the given `expression` and ready for typesetting

        Return type:
        :   `str`

    get\_texcode\_for\_expression\_in\_env(*expression*, *environment*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/tex.html)
    :   Inserts expression into TeX template wrapped in `\begin{environment}` and `\end{environment}`.

        Parameters:
        :   - **expression** (*str*) – The string containing the expression to be typeset, e.g. `$\sqrt{2}$`.
            - **environment** (*str*) – The string containing the environment in which the expression should be typeset, e.g. `align*`.

        Returns:
        :   LaTeX code based on template, containing the given expression inside its environment, ready for typesetting

        Return type:
        :   `str`

    output\_format: str = '.dvi'
    :   The output format resulting from compilation, e.g. `.dvi` or `.pdf`.

    placeholder\_text: str = 'YourTextHere'
    :   Text in the document that will be replaced by the expression to be rendered.

    post\_doc\_commands: str = ''
    :   Text (definitions, commands) to be inserted at right after `\begin{document}`, e.g. `\boldmath`.

    preamble: str = '\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}'
    :   The document’s preamble, i.e. the part between `\documentclass` and `\begin{document}`.

    tex\_compiler: str = 'latex'
    :   The TeX compiler to be used, e.g. `latex`, `pdflatex` or `lualatex`.
