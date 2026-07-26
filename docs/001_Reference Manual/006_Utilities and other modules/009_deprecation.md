---
{
  "title": "deprecation",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.deprecation.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "deprecation"
  ],
  "scraped_at": "2026-07-10T16:01:25"
}
---

# deprecation

Decorators for deprecating classes, functions and function parameters.

TypeVar’s

class T
:   ```
    TypeVar('T')
    ```

Functions

deprecated(*func: Callable[[...], [T](#manim.utils.deprecation.T)]*, *since: str | None = None*, *until: str | None = None*, *replacement: str | None = None*, *message: str | None = ''*) → Callable[[...], [T](#manim.utils.deprecation.T)][[source]](https://docs.manim.community/en/stable/_modules/manim/utils/deprecation.html)

deprecated(*func: None = None*, *since: str | None = None*, *until: str | None = None*, *replacement: str | None = None*, *message: str | None = ''*) → Callable[[Callable[[...], [T](#manim.utils.deprecation.T)]], Callable[[...], [T](#manim.utils.deprecation.T)]]
:   Decorator to mark a callable as deprecated.

    The decorated callable will cause a warning when used. The docstring of the
    deprecated callable is adjusted to indicate that this callable is deprecated.

    Parameters:
    :   - **func** (*Callable**[**[**...**]**,* [*T*](#manim.utils.deprecation.T)*]* *|* *None*) – The function to be decorated. Should not be set by the user.
        - **since** (*str* *|* *None*) – The version or date since deprecation.
        - **until** (*str* *|* *None*) – The version or date until removal of the deprecated callable.
        - **replacement** (*str* *|* *None*) – The identifier of the callable replacing the deprecated one.
        - **message** (*str* *|* *None*) – The reason for why the callable has been deprecated.

    Returns:
    :   The decorated callable.

    Return type:
    :   Callable

    Examples

    Basic usage:

    You can specify additional information for a more precise warning:

    You may also use dates instead of versions:

deprecated\_params(*params=None*, *since=None*, *until=None*, *message=''*, *redirections=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/deprecation.html)
:   Decorator to mark parameters of a callable as deprecated.

    It can also be used to automatically redirect deprecated parameter values to their
    replacements.

    Parameters:
    :   - **params** (*str* *|* *Iterable**[**str**]* *|* *None*) –

          The parameters to be deprecated. Can consist of:

          - An iterable of strings, with each element representing a parameter to deprecate
          - A single string, with parameter names separated by commas or spaces.
        - **since** (*str* *|* *None*) – The version or date since deprecation.
        - **until** (*str* *|* *None*) – The version or date until removal of the deprecated callable.
        - **message** (*str*) – The reason for why the callable has been deprecated.
        - **redirections** (*None* *|* *Iterable**[**tuple**[**str**,* *str**]* *|* *Callable**[**[**...**]**,* *dict**[**str**,* *Any**]**]**]*) –

          A list of parameter redirections. Each redirection can be one of the following:

          - A tuple of two strings. The first string defines the name of the deprecated
            parameter; the second string defines the name of the parameter to redirect to,
            when attempting to use the first string.
          - A function performing the mapping operation. The parameter names of the
            function determine which parameters are used as input. The function must
            return a dictionary which contains the redirected arguments.

          Redirected parameters are also implicitly deprecated.

    Returns:
    :   The decorated callable.

    Return type:
    :   Callable

    Raises:
    :   - **ValueError** – If no parameters are defined (neither explicitly nor implicitly).
        - **ValueError** – If defined parameters are invalid python identifiers.

    Examples

    Basic usage:

    You can also specify additional information for a more precise warning:

    Basic parameter redirection:

    Redirecting using a calculated value:

    Redirecting multiple parameter values to one:

    Redirect one parameter to multiple:
