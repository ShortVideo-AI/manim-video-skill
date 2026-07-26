---
{
  "title": "iterables",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.iterables.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "iterables"
  ],
  "scraped_at": "2026-07-10T16:01:36"
}
---

# iterables

Operations on iterables.

TypeVar’s

class T
:   ```
    TypeVar('T')
    ```

class U
:   ```
    TypeVar('U')
    ```

class F
:   ```
    TypeVar('F', np.float64, np.int_)
    ```

class H
:   ```
    TypeVar('H', bound=Hashable)
    ```

Functions

adjacent\_n\_tuples(*objects*, *n*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Returns the Sequence objects cyclically split into n length tuples.

    See also

    [`adjacent_pairs`](#manim.utils.iterables.adjacent_pairs)
    :   alias with n=2

    Examples

    Parameters:
    :   - **objects** (*Sequence**[*[*T*](#manim.utils.iterables.T)*]*)
        - **n** (*int*)

    Return type:
    :   zip[tuple[[T](#manim.utils.iterables.T), …]]

adjacent\_pairs(*objects*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Alias for `adjacent_n_tuples(objects, 2)`.

    See also

    [`adjacent_n_tuples`](#manim.utils.iterables.adjacent_n_tuples)

    Examples

    ```
    >>> list(adjacent_pairs([1, 2, 3, 4]))
    [(1, 2), (2, 3), (3, 4), (4, 1)]
    ```

    Parameters:
    :   **objects** (*Sequence**[*[*T*](#manim.utils.iterables.T)*]*)

    Return type:
    :   zip[tuple[[T](#manim.utils.iterables.T), …]]

all\_elements\_are\_instances(*iterable*, *Class*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Returns `True` if all elements of iterable are instances of Class.
    False otherwise.

    Parameters:
    :   - **iterable** (*Iterable**[**object**]*)
        - **Class** (*type**[**object**]*)

    Return type:
    :   bool

batch\_by\_property(*items*, *property\_func*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Takes in a Sequence, and returns a list of tuples, (batch, prop)
    such that all items in a batch have the same output when
    put into the Callable property\_func, and such that chaining all these
    batches together would give the original Sequence (i.e. order is
    preserved).

    Examples

    Parameters:
    :   - **items** (*Iterable**[*[*T*](#manim.utils.iterables.T)*]*)
        - **property\_func** (*Callable**[**[*[*T*](#manim.utils.iterables.T)*]**,* [*U*](#manim.utils.iterables.U)*]*)

    Return type:
    :   list[tuple[list[[*T*](#manim.utils.iterables.T)], [*U*](#manim.utils.iterables.U) | None]]

concatenate\_lists(*\*list\_of\_lists*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Combines the Iterables provided as arguments into one list.

    Examples

    ```
    >>> concatenate_lists([1, 2], [3, 4], [5])
    [1, 2, 3, 4, 5]
    ```

    Parameters:
    :   **list\_of\_lists** (*Iterable**[*[*T*](#manim.utils.iterables.T)*]*)

    Return type:
    :   list[[*T*](#manim.utils.iterables.T)]

hash\_obj(*obj*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Determines a hash, even of potentially mutable objects.

    Parameters:
    :   **obj** (*object*)

    Return type:
    :   int

list\_difference\_update(*l1*, *l2*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Returns a list containing all the elements of l1 not in l2.

    Examples

    ```
    >>> list_difference_update([1, 2, 3, 4], [2, 4])
    [1, 3]
    ```

    Parameters:
    :   - **l1** (*Iterable**[*[*T*](#manim.utils.iterables.T)*]*)
        - **l2** (*Iterable**[*[*T*](#manim.utils.iterables.T)*]*)

    Return type:
    :   list[[*T*](#manim.utils.iterables.T)]

list\_update(*l1*, *l2*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Used instead of `set.update()` to maintain order,
    :   making sure duplicates are removed from l1, not l2.
        Removes overlap of l1 and l2 and then concatenates l2 unchanged.

    Examples

    ```
    >>> list_update([1, 2, 3], [2, 4, 4])
    [1, 3, 2, 4, 4]
    ```

    Parameters:
    :   - **l1** (*Iterable**[*[*T*](#manim.utils.iterables.T)*]*)
        - **l2** (*Iterable**[*[*T*](#manim.utils.iterables.T)*]*)

    Return type:
    :   list[[*T*](#manim.utils.iterables.T)]

listify(*obj: str*) → list[str][[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)

listify(*obj: Iterable[[T](#manim.utils.iterables.T)]*) → list[[T](#manim.utils.iterables.T)]

listify(*obj: [T](#manim.utils.iterables.T)*) → list[[T](#manim.utils.iterables.T)]
:   Converts obj to a list intelligently.

    Examples

    Parameters:
    :   **obj** (*str* *|* *Iterable**[*[*T*](#manim.utils.iterables.T)*]* *|* [*T*](#manim.utils.iterables.T))

    Return type:
    :   list[str] | list[[*T*](#manim.utils.iterables.T)]

make\_even(*iterable\_1*, *iterable\_2*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Extends the shorter of the two iterables with duplicate values until its
    :   length is equal to the longer iterable (favours earlier elements).

    See also

    [`make_even_by_cycling`](#manim.utils.iterables.make_even_by_cycling)
    :   cycles elements instead of favouring earlier ones

    Examples

    Parameters:
    :   - **iterable\_1** (*Iterable**[*[*T*](#manim.utils.iterables.T)*]*)
        - **iterable\_2** (*Iterable**[*[*U*](#manim.utils.iterables.U)*]*)

    Return type:
    :   tuple[list[[*T*](#manim.utils.iterables.T)], list[[*U*](#manim.utils.iterables.U)]]

make\_even\_by\_cycling(*iterable\_1*, *iterable\_2*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Extends the shorter of the two iterables with duplicate values until its
    :   length is equal to the longer iterable (cycles over shorter iterable).

    See also

    [`make_even`](#manim.utils.iterables.make_even)
    :   favours earlier elements instead of cycling them

    Examples

    Parameters:
    :   - **iterable\_1** (*Collection**[*[*T*](#manim.utils.iterables.T)*]*)
        - **iterable\_2** (*Collection**[*[*U*](#manim.utils.iterables.U)*]*)

    Return type:
    :   tuple[list[[*T*](#manim.utils.iterables.T)], list[[*U*](#manim.utils.iterables.U)]]

remove\_list\_redundancies(*lst*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Used instead of `list(set(l))` to maintain order.
    Keeps the last occurrence of each element.

    Parameters:
    :   **lst** (*Reversible**[*[*H*](#manim.utils.iterables.H)*]*)

    Return type:
    :   list[[*H*](#manim.utils.iterables.H)]

remove\_nones(*sequence*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Removes elements where bool(x) evaluates to False.

    Examples

    Parameters:
    :   **sequence** (*Iterable**[*[*T*](#manim.utils.iterables.T) *|* *None**]*)

    Return type:
    :   list[[*T*](#manim.utils.iterables.T)]

resize\_array(*nparray*, *length*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Extends/truncates nparray so that `len(result) == length`.
    :   The elements of nparray are cycled to achieve the desired length.

    See also

    [`resize_preserving_order`](#manim.utils.iterables.resize_preserving_order)
    :   favours earlier elements instead of cycling them

    [`make_even_by_cycling`](#manim.utils.iterables.make_even_by_cycling)
    :   similar cycling behaviour for balancing 2 iterables

    Examples

    Parameters:
    :   - **nparray** (*npt.NDArray**[*[*F*](#manim.utils.iterables.F)*]*)
        - **length** (*int*)

    Return type:
    :   npt.NDArray[[F](#manim.utils.iterables.F)]

resize\_preserving\_order(*nparray*, *length*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Extends/truncates nparray so that `len(result) == length`.
    :   The elements of nparray are duplicated to achieve the desired length
        (favours earlier elements).

        Constructs a zeroes array of length if nparray is empty.

    See also

    [`resize_array`](#manim.utils.iterables.resize_array)
    :   cycles elements instead of favouring earlier ones

    [`make_even`](#manim.utils.iterables.make_even)
    :   similar earlier-favouring behaviour for balancing 2 iterables

    Examples

    Parameters:
    :   - **nparray** (*npt.NDArray**[**np.float64**]*)
        - **length** (*int*)

    Return type:
    :   npt.NDArray[np.float64]

resize\_with\_interpolation(*nparray*, *length*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Extends/truncates nparray so that `len(result) == length`.
    :   New elements are interpolated to achieve the desired length.

        Note that if nparray’s length changes, its dtype may too
        (e.g. int -> float: see Examples)

    See also

    [`resize_array`](#manim.utils.iterables.resize_array)
    :   cycles elements instead of interpolating

    [`resize_preserving_order`](#manim.utils.iterables.resize_preserving_order)
    :   favours earlier elements instead of interpolating

    Examples

    Parameters:
    :   - **nparray** (*npt.NDArray**[*[*F*](#manim.utils.iterables.F)*]*)
        - **length** (*int*)

    Return type:
    :   npt.NDArray[[F](#manim.utils.iterables.F)]

stretch\_array\_to\_length(*nparray*, *length*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Parameters:
    :   - **nparray** (*npt.NDArray**[*[*F*](#manim.utils.iterables.F)*]*)
        - **length** (*int*)

    Return type:
    :   npt.NDArray[[F](#manim.utils.iterables.F)]

tuplify(*obj: str*) → tuple[str][[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)

tuplify(*obj: Iterable[[T](#manim.utils.iterables.T)]*) → tuple[[T](#manim.utils.iterables.T)]

tuplify(*obj: [T](#manim.utils.iterables.T)*) → tuple[[T](#manim.utils.iterables.T)]
:   Converts obj to a tuple intelligently.

    Examples

    Parameters:
    :   **obj** (*str* *|* *Iterable**[*[*T*](#manim.utils.iterables.T)*]* *|* [*T*](#manim.utils.iterables.T))

    Return type:
    :   tuple[str] | tuple[[*T*](#manim.utils.iterables.T)]

uniq\_chain(*\*args*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html)
:   Returns a generator that yields all unique elements of the Iterables
    :   provided via args in the order provided.

    Examples

    Parameters:
    :   **args** (*Iterable**[*[*T*](#manim.utils.iterables.T)*]*)

    Return type:
    :   *Generator*[[*T*](#manim.utils.iterables.T), None, None]
