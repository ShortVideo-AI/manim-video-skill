---
{
  "title": "manim_directive",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "docbuild",
    "manim_directive"
  ],
  "scraped_at": "2026-07-10T16:01:29"
}
---

# manim\_directive

## A directive for including Manim videos in a Sphinx document

When rendering the HTML documentation, the `.. manim::` directive
implemented here allows to include rendered videos.

Its basic usage that allows processing **inline content**
looks as follows:

```
.. manim:: MyScene

    class MyScene(Scene):
        def construct(self):
            ...
```

It is required to pass the name of the class representing the
scene to be rendered to the directive.

As a second application, the directive can also be used to
render scenes that are defined within doctests, for example:

### Options

Options can be passed as follows:

```
.. manim:: <Class name>
    :<option name>: <value>
```

The following configuration options are supported by the
directive:

> hide\_source
> :   If this flag is present without argument,
>     the source code is not displayed above the rendered video.
>
> no\_autoplay
> :   If this flag is present without argument,
>     the video will not autoplay.
>
> quality{‘low’, ‘medium’, ‘high’, ‘fourk’}
> :   Controls render quality of the video, in analogy to
>     the corresponding command line flags.
>
> save\_as\_gif
> :   If this flag is present without argument,
>     the scene is rendered as a gif.
>
> save\_last\_frame
> :   If this flag is present without argument,
>     an image representing the last frame of the scene will
>     be rendered and displayed, instead of a video.
>
> ref\_classes
> :   A list of classes, separated by spaces, that is
>     rendered in a reference block after the source code.
>
> ref\_functions
> :   A list of functions, separated by spaces,
>     that is rendered in a reference block after the source code.
>
> ref\_methods
> :   A list of methods, separated by spaces,
>     that is rendered in a reference block after the source code.

Classes

| Name | Description |
| --- | --- |
| [`ManimDirective`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html) | The manim directive, rendering videos while building the documentation. |
| [`SetupMetadata`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.SetupMetadata.html) |  |
| [`SkipManimNode`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.SkipManimNode.html) | Auxiliary node class that is used when the `skip-manim` tag is present or `.pot` files are being built. |

Functions

depart(*self*, *node*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/docbuild/manim_directive.html)
:   Parameters:
    :   - **self** ([*SkipManimNode*](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.SkipManimNode.html))
        - **node** (*Element*)

    Return type:
    :   None

process\_name\_list(*option\_input*, *reference\_type*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/docbuild/manim_directive.html)
:   Reformats a string of space separated class names
    as a list of strings containing valid Sphinx references.

    Tests

    Parameters:
    :   - **option\_input** (*str*)
        - **reference\_type** (*str*)

    Return type:
    :   list[str]

setup(*app*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/docbuild/manim_directive.html)
:   Parameters:
    :   **app** (*Sphinx*)

    Return type:
    :   [SetupMetadata](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.SetupMetadata.html)

visit(*self*, *node*, *name=''*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/docbuild/manim_directive.html)
:   Parameters:
    :   - **self** ([*SkipManimNode*](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.SkipManimNode.html))
        - **node** (*Element*)
        - **name** (*str*)

    Return type:
    :   None
