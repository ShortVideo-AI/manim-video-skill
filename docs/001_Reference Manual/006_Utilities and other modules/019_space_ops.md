---
{
  "title": "space_ops",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html",
  "tree_path": [
    "Reference Manual",
    "Utilities and other modules",
    "space_ops"
  ],
  "scraped_at": "2026-07-10T16:01:42"
}
---

# space\_ops

Utility functions for two- and three-dimensional vectors.

Functions

R3\_to\_complex(*point*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Parameters:
    :   **point** (*Sequence**[**float**]*)

    Return type:
    :   *ndarray*

angle\_axis\_from\_quaternion(*quaternion*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Gets angle and axis from a quaternion.

    Parameters:
    :   **quaternion** (*Sequence**[**float**]*) – The quaternion from which we get the angle and axis.

    Returns:
    :   Gives the angle and axis

    Return type:
    :   Sequence[float]

angle\_between\_vectors(*v1*, *v2*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Returns the angle between two vectors.
    This angle will always be between 0 and pi

    Parameters:
    :   - **v1** (*ndarray*) – The first vector.
        - **v2** (*ndarray*) – The second vector.

    Returns:
    :   The angle between the vectors.

    Return type:
    :   float

angle\_of\_vector(*vector*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Returns polar coordinate theta when vector is projected on xy plane.

    Parameters:
    :   **vector** (*Sequence**[**float**]* *|* *ndarray*) – The vector to find the angle for.

    Returns:
    :   The angle of the vector projected.

    Return type:
    :   float

cartesian\_to\_spherical(*vec*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Returns an array of numbers corresponding to each
    polar coordinate value (distance, phi, theta).

    Parameters:
    :   **vec** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – A numpy array or a sequence of floats `[x, y, z]`.

    Return type:
    :   *ndarray*

center\_of\_mass(*points*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Gets the center of mass of the points in space.

    Parameters:
    :   **points** ([*PointNDLike\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The points to find the center of mass from.

    Returns:
    :   The center of mass of the points.

    Return type:
    :   np.ndarray

compass\_directions(*n=4*, *start\_vect=array([1., 0., 0.])*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Finds the cardinal directions using tau.

    Parameters:
    :   - **n** (*int*) – The amount to be rotated, by default 4
        - **start\_vect** (*ndarray*) – The direction for the angle to start with, by default RIGHT

    Returns:
    :   The angle which has been rotated.

    Return type:
    :   np.ndarray

complex\_func\_to\_R3\_func(*complex\_func*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Parameters:
    :   **complex\_func** (*Callable**[**[**complex**]**,* *complex**]*)

    Return type:
    :   *Callable*[[TypeAliasForwardRef(‘~manim.typing.Point3DLike’)], TypeAliasForwardRef(‘~manim.typing.Point3D’)]

complex\_to\_R3(*complex\_num*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Parameters:
    :   **complex\_num** (*complex*)

    Return type:
    :   *ndarray*

cross(*v1*, *v2*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Parameters:
    :   - **v1** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **v2** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))

    Return type:
    :   [*Vector3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)

cross2d(*a*, *b*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Compute the determinant(s) of the passed
    vector (sequences).

    Parameters:
    :   - **a** ([*Vector2D*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* [*Vector2D\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – A vector or a sequence of vectors.
        - **b** ([*Vector2D*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* [*Vector2D\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – A vector or a sequence of vectors.

    Returns:
    :   The determinant or sequence of determinants
        of the first two components of the specified
        vectors.

    Return type:
    :   Sequence[float] | float

    Examples

earclip\_triangulation(*verts*, *ring\_ends*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Returns a list of indices giving a triangulation
    of a polygon, potentially with holes.

    Parameters:
    :   - **verts** (*ndarray*) – verts is a numpy array of points.
        - **ring\_ends** (*list*) – ring\_ends is a list of indices indicating where
          the ends of new paths are.

    Returns:
    :   A list of indices giving a triangulation of a polygon.

    Return type:
    :   list

find\_intersection(*p0s*, *v0s*, *p1s*, *v1s*, *threshold=1e-05*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Return the intersection of a line passing through p0 in direction v0
    with one passing through p1 in direction v1 (or array of intersections
    from arrays of such points/directions).
    For 3d values, it returns the point on the ray p0 + v0 \* t closest to the
    ray p1 + v1 \* t

    Parameters:
    :   - **p0s** ([*Point3DLike\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **v0s** ([*Vector3DLike\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **p1s** ([*Point3DLike\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **v1s** ([*Vector3DLike\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **threshold** (*float*)

    Return type:
    :   list[TypeAliasForwardRef(‘~manim.typing.Point3D’)]

get\_unit\_normal(*v1*, *v2*, *tol=1e-06*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Gets the unit normal of the vectors.

    Parameters:
    :   - **v1** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The first vector.
        - **v2** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The second vector
        - **tol** (*float*) – [description], by default 1e-6

    Returns:
    :   The normal of the two vectors.

    Return type:
    :   np.ndarray

get\_winding\_number(*points*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Determine the number of times a polygon winds around the origin.

    The orientation is measured mathematically positively, i.e.,
    counterclockwise.

    Parameters:
    :   **points** (*Sequence**[**ndarray**]*) – The vertices of the polygon being queried.

    Return type:
    :   float

    Examples

line\_intersection(*line1*, *line2*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Returns the intersection point of two lines, each defined by
    a pair of distinct points lying on the line.

    Parameters:
    :   - **line1** (*Sequence**[**ndarray**]*) – A list of two points that determine the first line.
        - **line2** (*Sequence**[**ndarray**]*) – A list of two points that determine the second line.

    Returns:
    :   The intersection points of the two lines which are intersecting.

    Return type:
    :   np.ndarray

    Raises:
    :   **ValueError** – Error is produced if the two lines don’t intersect with each other
        or if the coordinates don’t lie on the xy-plane.

midpoint(*point1*, *point2*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Gets the midpoint of two points.

    Parameters:
    :   - **point1** (*Sequence**[**float**]*) – The first point.
        - **point2** (*Sequence**[**float**]*) – The second point.

    Returns:
    :   The midpoint of the points

    Return type:
    :   [Union](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Union.html)[float, np.ndarray]

norm\_squared(*v*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Parameters:
    :   **v** (*float*)

    Return type:
    :   float

normalize(*vect*, *fall\_back=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Parameters:
    :   - **vect** (*ndarray* *|* *tuple**[**float**]*)
        - **fall\_back** (*ndarray* *|* *None*)

    Return type:
    :   *ndarray*

normalize\_along\_axis(*array*, *axis*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Normalizes an array with the provided axis.

    Parameters:
    :   - **array** (*ndarray*) – The array which has to be normalized.
        - **axis** (*ndarray*) – The axis to be normalized to.

    Returns:
    :   Array which has been normalized according to the axis.

    Return type:
    :   np.ndarray

perpendicular\_bisector(*line*, *norm\_vector=array([0., 0., 1.])*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Returns a list of two points that correspond
    to the ends of the perpendicular bisector of the
    two points given.

    Parameters:
    :   - **line** (*Sequence**[**ndarray**]*) – a list of two numpy array points (corresponding
          to the ends of a line).
        - **norm\_vector** ([*Vector3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – the vector perpendicular to both the line given
          and the perpendicular bisector.

    Returns:
    :   A list of two numpy array points that correspond
        to the ends of the perpendicular bisector

    Return type:
    :   list

quaternion\_conjugate(*quaternion*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Used for finding the conjugate of the quaternion

    Parameters:
    :   **quaternion** (*Sequence**[**float**]*) – The quaternion for which you want to find the conjugate for.

    Returns:
    :   The conjugate of the quaternion.

    Return type:
    :   np.ndarray

quaternion\_from\_angle\_axis(*angle*, *axis*, *axis\_normalized=False*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Gets a quaternion from an angle and an axis.
    For more information, check [this Wikipedia page](https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles).

    Parameters:
    :   - **angle** (*float*) – The angle for the quaternion.
        - **axis** (*ndarray*) – The axis for the quaternion
        - **axis\_normalized** (*bool*) – Checks whether the axis is normalized, by default False

    Returns:
    :   Gives back a quaternion from the angle and axis

    Return type:
    :   list[float]

quaternion\_mult(*\*quats*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Gets the Hamilton product of the quaternions provided.
    For more information, check [this Wikipedia page](https://en.wikipedia.org/wiki/Quaternion).

    Returns:
    :   Returns a list of product of two quaternions.

    Return type:
    :   [Union](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Union.html)[np.ndarray, List[[Union](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Union.html)[float, np.ndarray]]]

    Parameters:
    :   **quats** (*Sequence**[**float**]*)

regular\_vertices(*n*, *\**, *radius=1*, *start\_angle=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Generates regularly spaced vertices around a circle centered at the origin.

    Parameters:
    :   - **n** (*int*) – The number of vertices
        - **radius** (*float*) – The radius of the circle that the vertices are placed on.
        - **start\_angle** (*float* *|* *None*) –

          The angle the vertices start at.

          If unspecified, for even `n` values, `0` will be used.
          For odd `n` values, 90 degrees is used.

    Returns:
    :   - **vertices** (`numpy.ndarray`) – The regularly spaced vertices.
        - **start\_angle** (`float`) – The angle the vertices start at.

    Return type:
    :   tuple[*ndarray*, float]

rotate\_vector(*vector*, *angle*, *axis=array([0., 0., 1.])*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Function for rotating a vector.

    Parameters:
    :   - **vector** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The vector to be rotated.
        - **angle** (*float*) – The angle to be rotated by.
        - **axis** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The axis to be rotated, by default OUT

    Returns:
    :   The rotated vector with provided angle and axis.

    Return type:
    :   np.ndarray

    Raises:
    :   **ValueError** – If vector is not of dimension 2 or 3.

rotation\_about\_z(*angle*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Returns a rotation matrix for a given angle.

    Parameters:
    :   **angle** (*float*) – Angle for the rotation matrix.

    Returns:
    :   Gives back the rotated matrix.

    Return type:
    :   np.ndarray

rotation\_matrix(*angle*, *axis*, *homogeneous=False*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Rotation in R^3 about a specified axis of rotation.

    Parameters:
    :   - **angle** (*float*)
        - **axis** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **homogeneous** (*bool*)

    Return type:
    :   *ndarray*

rotation\_matrix\_from\_quaternion(*quat*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Parameters:
    :   **quat** (*ndarray*)

    Return type:
    :   *ndarray*

rotation\_matrix\_transpose(*angle*, *axis*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Parameters:
    :   - **angle** (*float*)
        - **axis** ([*Vector3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))

    Return type:
    :   *ndarray*

rotation\_matrix\_transpose\_from\_quaternion(*quat*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Converts the quaternion, quat, to an equivalent rotation matrix representation.
    For more information, check [this page](https://in.mathworks.com/help/driving/ref/quaternion.rotmat.html).

    Parameters:
    :   **quat** (*ndarray*) – The quaternion which is to be converted.

    Returns:
    :   Gives back the Rotation matrix representation, returned as a 3-by-3
        matrix or 3-by-3-by-N multidimensional array.

    Return type:
    :   List[np.ndarray]

shoelace(*x\_y*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   2D implementation of the shoelace formula.

    Returns:
    :   Returns signed area.

    Return type:
    :   `float`

    Parameters:
    :   **x\_y** ([*Point2D\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html))

shoelace\_direction(*x\_y*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Uses the area determined by the shoelace method to determine whether
    the input set of points is directed clockwise or counterclockwise.

    Returns:
    :   Either `"CW"` or `"CCW"`.

    Return type:
    :   `str`

    Parameters:
    :   **x\_y** ([*Point2D\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html))

spherical\_to\_cartesian(*spherical*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Returns a numpy array `[x, y, z]` based on the spherical
    coordinates given.

    Parameters:
    :   **spherical** (*Sequence**[**float**]*) –

        A list of three floats that correspond to the following:

        r - The distance between the point and the origin.

        theta - The azimuthal angle of the point to the positive x-axis.

        phi - The vertical angle of the point to the positive z-axis.

    Return type:
    :   *ndarray*

thick\_diagonal(*dim*, *thickness=2*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Parameters:
    :   - **dim** (*int*)
        - **thickness** (*int*)

    Return type:
    :   [*MatrixMN*](https://docs.manim.community/en/stable/reference/manim.typing.html)

z\_to\_vector(*vector*)[[source]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html)
:   Returns some matrix in SO(3) which takes the z-axis to the
    (normalized) vector provided as an argument

    Parameters:
    :   **vector** (*ndarray*)

    Return type:
    :   *ndarray*
