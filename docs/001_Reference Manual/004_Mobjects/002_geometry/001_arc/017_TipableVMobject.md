---
{
  "title": "TipableVMobject",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.TipableVMobject.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "geometry",
    "arc",
    "TipableVMobject"
  ],
  "scraped_at": "2026-07-10T15:58:51"
}
---

# TipableVMobject

Qualified name: `manim.mobject.geometry.arc.TipableVMobject`

class TipableVMobject(*tip\_length=0.35*, *normal\_vector=array([0., 0., 1.])*, *tip\_style=None*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
:   Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    Meant for shared functionality between Arc and Line.
    Functionality can be classified broadly into these groups:

    > - Adding, Creating, Modifying tips
    >   :   - add\_tip calls create\_tip, before pushing the new tip
    >         :   into the TipableVMobject’s list of submobjects
    >       - stylistic and positional configuration
    > - Checking for tips
    >   :   - Boolean checks for whether the TipableVMobject has a tip
    >         :   and a starting tip
    > - Getters
    >   :   - Straightforward accessors, returning information pertaining
    >         :   to the TipableVMobject instance’s tip(s), its length etc

    Methods

    |  |  |
    | --- | --- |
    | [`add_tip`](#manim.mobject.geometry.arc.TipableVMobject.add_tip) | Adds a tip to the TipableVMobject instance, recognising that the endpoints might need to be switched if it's a 'starting tip' or not. |
    | `assign_tip_attr` |  |
    | [`create_tip`](#manim.mobject.geometry.arc.TipableVMobject.create_tip) | Stylises the tip, positions it spatially, and returns the newly instantiated tip to the caller. |
    | `get_default_tip_length` |  |
    | [`get_end`](#manim.mobject.geometry.arc.TipableVMobject.get_end) | Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) ends. |
    | `get_first_handle` |  |
    | `get_last_handle` |  |
    | `get_length` |  |
    | [`get_start`](#manim.mobject.geometry.arc.TipableVMobject.get_start) | Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) starts. |
    | [`get_tip`](#manim.mobject.geometry.arc.TipableVMobject.get_tip) | Returns the TipableVMobject instance's (first) tip, otherwise throws an exception. |
    | [`get_tips`](#manim.mobject.geometry.arc.TipableVMobject.get_tips) | Returns a VGroup (collection of VMobjects) containing the TipableVMObject instance's tips. |
    | [`get_unpositioned_tip`](#manim.mobject.geometry.arc.TipableVMobject.get_unpositioned_tip) | Returns a tip that has been stylistically configured, but has not yet been given a position in space. |
    | `has_start_tip` |  |
    | `has_tip` |  |
    | `pop_tips` |  |
    | `position_tip` |  |
    | `reset_endpoints_based_on_tip` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    Parameters:
    :   - **tip\_length** (*float*)
        - **normal\_vector** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **tip\_style** (*dict* *|* *None*)
        - **kwargs** (*Any*)

    \_original\_\_init\_\_(*tip\_length=0.35*, *normal\_vector=array([0., 0., 1.])*, *tip\_style=None*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **tip\_length** (*float*)
            - **normal\_vector** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **tip\_style** (*dict* *|* *None*)
            - **kwargs** (*Any*)

        Return type:
        :   None

    add\_tip(*tip=None*, *tip\_shape=None*, *tip\_length=None*, *tip\_width=None*, *at\_start=False*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
    :   Adds a tip to the TipableVMobject instance, recognising
        that the endpoints might need to be switched if it’s
        a ‘starting tip’ or not.

        Parameters:
        :   - **tip** ([*tips.ArrowTip*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowTip.html) *|* *None*)
            - **tip\_shape** (*type**[*[*tips.ArrowTip*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowTip.html)*]* *|* *None*)
            - **tip\_length** (*float* *|* *None*)
            - **tip\_width** (*float* *|* *None*)
            - **at\_start** (*bool*)

        Return type:
        :   Self

    create\_tip(*tip\_shape=None*, *tip\_length=None*, *tip\_width=None*, *at\_start=False*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
    :   Stylises the tip, positions it spatially, and returns
        the newly instantiated tip to the caller.

        Parameters:
        :   - **tip\_shape** (*type**[*[*tips.ArrowTip*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowTip.html)*]* *|* *None*)
            - **tip\_length** (*float* *|* *None*)
            - **tip\_width** (*float* *|* *None*)
            - **at\_start** (*bool*)

        Return type:
        :   [tips.ArrowTip](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowTip.html)

    get\_end()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
    :   Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) ends.

        Return type:
        :   [*Point3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)

    get\_start()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
    :   Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html) starts.

        Return type:
        :   [*Point3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)

    get\_tip()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
    :   Returns the TipableVMobject instance’s (first) tip,
        otherwise throws an exception.

        Return type:
        :   [*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)

    get\_tips()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
    :   Returns a VGroup (collection of VMobjects) containing
        the TipableVMObject instance’s tips.

        Return type:
        :   [*VGroup*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    get\_unpositioned\_tip(*tip\_shape=None*, *tip\_length=None*, *tip\_width=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html)
    :   Returns a tip that has been stylistically configured,
        but has not yet been given a position in space.

        Parameters:
        :   - **tip\_shape** (*type**[*[*tips.ArrowTip*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowTip.html)*]* *|* *None*)
            - **tip\_length** (*float* *|* *None*)
            - **tip\_width** (*float* *|* *None*)

        Return type:
        :   [tips.ArrowTip](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowTip.html) | [tips.ArrowTriangleFilledTip](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowTriangleFilledTip.html)
