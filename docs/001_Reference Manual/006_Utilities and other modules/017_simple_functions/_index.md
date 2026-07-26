---
{
  "title": "simple_functions",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "simple_functions"
  ],
  "scraped_at": "2026-07-10T16:01:40"
}
---

# simple\_functions

A collection of simple functions.

TypeVar’s

class ComparableT
:   ```
    TypeVar('ComparableT', bound=Comparable)
    ```

Classes

| Name | Description |
| --- | --- |
| [`Comparable`](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.Comparable.html) |  |

Functions

binary\_search(*function*, *target*, *lower\_bound*, *upper\_bound*, *tolerance=0.0001*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/simple_functions.html)
:   Searches for a value in a range by repeatedly dividing the range in half.

    To be more precise, performs numerical binary search to determine the
    input to `function`, between the bounds given, that outputs `target`
    to within `tolerance` (default of 0.0001).
    Returns `None` if no input can be found within the bounds.

    Examples

    Consider the polynomial \(x^2 + 3x + 1\) where we search for
    a target value of \(11\). An exact solution is \(x = 2\).

    Searching in the interval \([0, 5]\) for a target value of \(71\)
    does not yield a solution:

    ```
    >>> binary_search(lambda x: x**2 + 3*x + 1, 71, 0, 5) is None
    True
    ```

    Parameters:
    :   - **function** (*Callable**[**[**float**]**,* *float**]*)
        - **target** (*float*)
        - **lower\_bound** (*float*)
        - **upper\_bound** (*float*)
        - **tolerance** (*float*)

    Return type:
    :   float | None

choose(*n*, *k*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/simple_functions.html)
:   The binomial coefficient n choose k.

    \(\binom{n}{k}\) describes the number of possible choices of
    \(k\) elements from a set of \(n\) elements.

    References

    - <https://en.wikipedia.org/wiki/Combination>
    - [https://docs.python.org/3/library/math.html#math.comb](https://docs.python.org/3/library/math.html)

    Parameters:
    :   - **n** (*int*)
        - **k** (*int*)

    Return type:
    :   int

clip(*a*, *min\_a*, *max\_a*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/simple_functions.html)
:   Clips `a` to the interval [`min_a`, `max_a`].

    Accepts any comparable objects (i.e. those that support <, >).
    Returns `a` if it is between `min_a` and `max_a`.
    Otherwise, whichever of `min_a` and `max_a` is closest.

    Examples

    ```
    >>> clip(15, 11, 20)
    15
    >>> clip('a', 'h', 'k')
    'h'
    ```

    Parameters:
    :   - **a** ([*ComparableT*](#manim.utils.simple_functions.ComparableT))
        - **min\_a** ([*ComparableT*](#manim.utils.simple_functions.ComparableT))
        - **max\_a** ([*ComparableT*](#manim.utils.simple_functions.ComparableT))

    Return type:
    :   [*ComparableT*](#manim.utils.simple_functions.ComparableT)

sigmoid(*x*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/simple_functions.html)
:   Returns the output of the logistic function.

    The logistic function, a common example of a sigmoid function, is defined
    as \(\frac{1}{1 + e^{-x}}\).

    References

    - <https://en.wikipedia.org/wiki/Sigmoid_function>
    - <https://en.wikipedia.org/wiki/Logistic_function>

    Parameters:
    :   **x** (*float*)

    Return type:
    :   float
