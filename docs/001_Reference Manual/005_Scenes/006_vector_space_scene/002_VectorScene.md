---
{
  "title": "VectorScene",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.VectorScene.html",
  "tree_path": [
    "Reference Manual",
    "Scenes",
    "vector_space_scene",
    "VectorScene"
  ],
  "scraped_at": "2026-07-10T16:00:56"
}
---

# VectorScene

Qualified name: `manim.scene.vector\_space\_scene.VectorScene`

class VectorScene(*basis\_vector\_stroke\_width=6.0*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html)
:   Bases: [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html)

    Methods

    |  |  |
    | --- | --- |
    | [`add_axes`](#manim.scene.vector_space_scene.VectorScene.add_axes) | Adds a pair of Axes to the Scene. |
    | [`add_plane`](#manim.scene.vector_space_scene.VectorScene.add_plane) | Adds a NumberPlane object to the background. |
    | [`add_vector`](#manim.scene.vector_space_scene.VectorScene.add_vector) | Returns the Vector after adding it to the Plane. |
    | [`coords_to_vector`](#manim.scene.vector_space_scene.VectorScene.coords_to_vector) | This method writes the vector as a column matrix (henceforth called the label), takes the values in it one by one, and form the corresponding lines that make up the x and y components of the vector. |
    | [`get_basis_vector_labels`](#manim.scene.vector_space_scene.VectorScene.get_basis_vector_labels) | Returns naming labels for the basis vectors. |
    | [`get_basis_vectors`](#manim.scene.vector_space_scene.VectorScene.get_basis_vectors) | Returns a VGroup of the Basis Vectors (1,0) and (0,1) |
    | [`get_vector`](#manim.scene.vector_space_scene.VectorScene.get_vector) | Returns an arrow on the Plane given an input numerical vector. |
    | [`get_vector_label`](#manim.scene.vector_space_scene.VectorScene.get_vector_label) | Returns naming labels for the passed vector. |
    | [`label_vector`](#manim.scene.vector_space_scene.VectorScene.label_vector) | Shortcut method for creating, and animating the addition of a label for the vector. |
    | [`lock_in_faded_grid`](#manim.scene.vector_space_scene.VectorScene.lock_in_faded_grid) | This method freezes the NumberPlane and Axes that were already in the background, and adds new, manipulatable ones to the foreground. |
    | `position_x_coordinate` |  |
    | `position_y_coordinate` |  |
    | [`show_ghost_movement`](#manim.scene.vector_space_scene.VectorScene.show_ghost_movement) | This method plays an animation that partially shows the entire plane moving in the direction of a particular vector. |
    | [`vector_to_coords`](#manim.scene.vector_space_scene.VectorScene.vector_to_coords) | This method displays vector as a Vector() based vector, and then shows the corresponding lines that make up the x and y components of the vector. |
    | [`write_vector_coordinates`](#manim.scene.vector_space_scene.VectorScene.write_vector_coordinates) | Returns a column matrix indicating the vector coordinates, after writing them to the screen. |

    Attributes

    |  |  |
    | --- | --- |
    | `camera` |  |
    | `time` | The time since the start of the scene. |

    Parameters:
    :   - **basis\_vector\_stroke\_width** (*float*)
        - **kwargs** (*Any*)

    add\_axes(*animate=False*, *color=ManimColor('#FFFFFF')*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html)
    :   Adds a pair of Axes to the Scene.

        Parameters:
        :   - **animate** (*bool*) – Whether or not to animate the addition of the axes through Create.
            - **color** (*TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)* *|* *Iterable**[**TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)**]*) – The color of the axes. Defaults to WHITE.

        Return type:
        :   [*Axes*](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html)

    add\_plane(*animate=False*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html)
    :   Adds a NumberPlane object to the background.

        Parameters:
        :   - **animate** (*bool*) – Whether or not to animate the addition of the plane via Create.
            - **\*\*kwargs** (*Any*) – Any valid keyword arguments accepted by NumberPlane.

        Returns:
        :   The NumberPlane object.

        Return type:
        :   [NumberPlane](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html)

    add\_vector(*vector*, *color=ManimColor('#FFFF00')*, *animate=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html)
    :   Returns the Vector after adding it to the Plane.

        Parameters:
        :   - **vector** ([*Arrow*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html) *|* *TypeAliasForwardRef**(**'~manim.typing.Vector3DLike'**)*) – It can be a pre-made graphical vector, or the
              coordinates of one.
            - **color** (*TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)* *|* *Iterable**[**TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)**]*) – The string of the hex color of the vector.
              This is only taken into consideration if
              ‘vector’ is not an Arrow. Defaults to YELLOW.
            - **animate** (*bool*) – Whether or not to animate the addition of the vector
              by using GrowArrow
            - **\*\*kwargs** (*Any*) – Any valid keyword argument of Arrow.
              These are only considered if vector is not
              an Arrow.

        Returns:
        :   The arrow representing the vector.

        Return type:
        :   [Arrow](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html)

    coords\_to\_vector(*vector*, *coords\_start=array([2., 2., 0.])*, *clean\_up=True*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html)
    :   This method writes the vector as a column matrix (henceforth called the label),
        takes the values in it one by one, and form the corresponding
        lines that make up the x and y components of the vector. Then, an
        Vector() based vector is created between the lines on the Screen.

        Parameters:
        :   - **vector** ([*Vector2DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The vector to show.
            - **coords\_start** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The starting point of the location of
              the label of the vector that shows it
              numerically.
              Defaults to 2 \* RIGHT + 2 \* UP or (2,2)
            - **clean\_up** (*bool*) – Whether or not to remove whatever
              this method did after it’s done.

        Return type:
        :   None

    get\_basis\_vector\_labels(*\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html)
    :   Returns naming labels for the basis vectors.

        Parameters:
        :   **\*\*kwargs** (*Any*) –

            Any valid keyword arguments of get\_vector\_label:
            :   vector,
                label (str,MathTex)
                at\_tip (bool=False),
                direction (str=”left”),
                rotate (bool),
                color (str),
                label\_scale\_factor=VECTOR\_LABEL\_SCALE\_FACTOR (int, float),

        Return type:
        :   [*VGroup*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    get\_basis\_vectors(*i\_hat\_color=ManimColor('#83C167')*, *j\_hat\_color=ManimColor('#FC6255')*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html)
    :   Returns a VGroup of the Basis Vectors (1,0) and (0,1)

        Parameters:
        :   - **i\_hat\_color** (*TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)* *|* *Iterable**[**TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)**]*) – The hex colour to use for the basis vector in the x direction
            - **j\_hat\_color** (*TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)* *|* *Iterable**[**TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)**]*) – The hex colour to use for the basis vector in the y direction

        Returns:
        :   VGroup of the Vector Mobjects representing the basis vectors.

        Return type:
        :   [VGroup](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)

    get\_vector(*numerical\_vector*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html)
    :   Returns an arrow on the Plane given an input numerical vector.

        Parameters:
        :   - **numerical\_vector** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The Vector to plot.
            - **\*\*kwargs** (*Any*) – Any valid keyword argument of Arrow.

        Returns:
        :   The Arrow representing the Vector.

        Return type:
        :   [Arrow](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html)

    get\_vector\_label(*vector*, *label*, *at\_tip=False*, *direction='left'*, *rotate=False*, *color=None*, *label\_scale\_factor=0.8*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html)
    :   Returns naming labels for the passed vector.

        Parameters:
        :   - **vector** ([*Vector*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html)) – Vector Object for which to get the label.
            - **at\_tip** (*bool*) – Whether or not to place the label at the tip of the vector.
            - **direction** (*str*) – If the label should be on the “left” or right of the vector.
            - **rotate** (*bool*) – Whether or not to rotate it to align it with the vector.
            - **color** (*TypeAliasForwardRef**(**'~manim.utils.color.core.ParsableManimColor'**)* *|* *None*) – The color to give the label.
            - **label\_scale\_factor** (*float*) – How much to scale the label by.
            - **label** ([*MathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html) *|* *str*)

        Returns:
        :   The MathTex of the label.

        Return type:
        :   [MathTex](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html)

    label\_vector(*vector*, *label*, *animate=True*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html)
    :   Shortcut method for creating, and animating the addition of
        a label for the vector.

        Parameters:
        :   - **vector** ([*Vector*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html)) – The vector for which the label must be added.
            - **label** ([*MathTex*](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html) *|* *str*) – The MathTex/string of the label.
            - **animate** (*bool*) – Whether or not to animate the labelling w/ Write
            - **\*\*kwargs** (*Any*) – Any valid keyword argument of get\_vector\_label

        Returns:
        :   The MathTex of the label.

        Return type:
        :   [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html)

    lock\_in\_faded\_grid(*dimness=0.7*, *axes\_dimness=0.5*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html)
    :   This method freezes the NumberPlane and Axes that were already
        in the background, and adds new, manipulatable ones to the foreground.

        Parameters:
        :   - **dimness** (*float*) – The required dimness of the NumberPlane
            - **axes\_dimness** (*float*) – The required dimness of the Axes.

        Return type:
        :   None

    show\_ghost\_movement(*vector*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html)
    :   This method plays an animation that partially shows the entire plane moving
        in the direction of a particular vector. This is useful when you wish to
        convey the idea of mentally moving the entire plane in a direction, without
        actually moving the plane.

        Parameters:
        :   **vector** ([*Arrow*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html) *|* *TypeAliasForwardRef**(**'~manim.typing.Vector2DLike'**)* *|* *TypeAliasForwardRef**(**'~manim.typing.Vector3DLike'**)*) – The vector which indicates the direction of movement.

        Return type:
        :   None

    vector\_to\_coords(*vector*, *integer\_labels=True*, *clean\_up=True*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html)
    :   This method displays vector as a Vector() based vector, and then shows
        the corresponding lines that make up the x and y components of the vector.
        Then, a column matrix (henceforth called the label) is created near the
        head of the Vector.

        Parameters:
        :   - **vector** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The vector to show.
            - **integer\_labels** (*bool*) – Whether or not to round the value displayed.
              in the vector’s label to the nearest integer
            - **clean\_up** (*bool*) – Whether or not to remove whatever
              this method did after it’s done.

        Return type:
        :   tuple[[*Matrix*](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html), [*Line*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html), [*Line*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html)]

    write\_vector\_coordinates(*vector*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html)
    :   Returns a column matrix indicating the vector coordinates,
        after writing them to the screen.

        Parameters:
        :   - **vector** ([*Vector*](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html)) – The arrow representing the vector.
            - **\*\*kwargs** (*Any*) – Any valid keyword arguments of [`coordinate_label()`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html):

        Returns:
        :   The column matrix representing the vector.

        Return type:
        :   [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html)
