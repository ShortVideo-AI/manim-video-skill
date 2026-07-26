---
{
  "title": "ThreeDCamera",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.camera.three_d_camera.ThreeDCamera.html",
  "tree_path": [
    "Reference Manual",
    "Cameras",
    "three_d_camera",
    "ThreeDCamera"
  ],
  "scraped_at": "2026-07-10T15:58:35"
}
---

# ThreeDCamera

Qualified name: `manim.camera.three\_d\_camera.ThreeDCamera`

class ThreeDCamera(*focal\_distance=20.0*, *shading\_factor=0.2*, *default\_distance=5.0*, *light\_source\_start\_point=array([-7., -9., 10.])*, *should\_apply\_shading=True*, *exponential\_projection=False*, *phi=0*, *theta=-1.5707963267948966*, *gamma=0*, *zoom=1*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
:   Bases: [`Camera`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html)

    Initializes the ThreeDCamera

    Parameters:
    :   - **\*kwargs** (*Any*) – Any keyword argument of Camera.
        - **focal\_distance** (*float*)
        - **shading\_factor** (*float*)
        - **default\_distance** (*float*)
        - **light\_source\_start\_point** ([*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html))
        - **should\_apply\_shading** (*bool*)
        - **exponential\_projection** (*bool*)
        - **phi** (*float*)
        - **theta** (*float*)
        - **gamma** (*float*)
        - **zoom** (*float*)
        - **\*kwargs**

    Methods

    |  |  |
    | --- | --- |
    | [`add_fixed_in_frame_mobjects`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_in_frame_mobjects) | This method allows the mobject to have a fixed position, even when the camera moves around. |
    | [`add_fixed_orientation_mobjects`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_orientation_mobjects) | This method allows the mobject to have a fixed orientation, even when the camera moves around. |
    | [`capture_mobjects`](#manim.camera.three_d_camera.ThreeDCamera.capture_mobjects) | Capture mobjects by printing them on `pixel_array`. |
    | [`generate_rotation_matrix`](#manim.camera.three_d_camera.ThreeDCamera.generate_rotation_matrix) | Generates a rotation matrix based off the current position of the camera. |
    | [`get_fill_rgbas`](#manim.camera.three_d_camera.ThreeDCamera.get_fill_rgbas) | Returns the RGBA array of the fill of the passed VMobject |
    | [`get_focal_distance`](#manim.camera.three_d_camera.ThreeDCamera.get_focal_distance) | Returns focal\_distance of the Camera. |
    | [`get_gamma`](#manim.camera.three_d_camera.ThreeDCamera.get_gamma) | Returns the rotation of the camera about the vector from the ORIGIN to the Camera. |
    | [`get_mobjects_to_display`](#manim.camera.three_d_camera.ThreeDCamera.get_mobjects_to_display) | Used to get the list of mobjects to display with the camera. |
    | [`get_phi`](#manim.camera.three_d_camera.ThreeDCamera.get_phi) | Returns the Polar angle (the angle off Z\_AXIS) phi. |
    | [`get_rotation_matrix`](#manim.camera.three_d_camera.ThreeDCamera.get_rotation_matrix) | Returns the matrix corresponding to the current position of the camera. |
    | [`get_stroke_rgbas`](#manim.camera.three_d_camera.ThreeDCamera.get_stroke_rgbas) | Gets the RGBA array for the stroke of the passed VMobject. |
    | [`get_theta`](#manim.camera.three_d_camera.ThreeDCamera.get_theta) | Returns the Azimuthal i.e the angle that spins the camera around the Z\_AXIS. |
    | [`get_value_trackers`](#manim.camera.three_d_camera.ThreeDCamera.get_value_trackers) | A list of [`ValueTrackers`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html) of phi, theta, focal\_distance, gamma and zoom. |
    | [`get_zoom`](#manim.camera.three_d_camera.ThreeDCamera.get_zoom) | Returns the zoom amount of the camera. |
    | `modified_rgbas` |  |
    | [`project_point`](#manim.camera.three_d_camera.ThreeDCamera.project_point) | Applies the current rotation\_matrix as a projection matrix to the passed point. |
    | [`project_points`](#manim.camera.three_d_camera.ThreeDCamera.project_points) | Applies the current rotation\_matrix as a projection matrix to the passed array of points. |
    | [`remove_fixed_in_frame_mobjects`](#manim.camera.three_d_camera.ThreeDCamera.remove_fixed_in_frame_mobjects) | If a mobject was fixed in frame by passing it through [`add_fixed_in_frame_mobjects()`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_in_frame_mobjects), then this undoes that fixing. |
    | [`remove_fixed_orientation_mobjects`](#manim.camera.three_d_camera.ThreeDCamera.remove_fixed_orientation_mobjects) | If a mobject was fixed in its orientation by passing it through [`add_fixed_orientation_mobjects()`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_orientation_mobjects), then this undoes that fixing. |
    | [`reset_rotation_matrix`](#manim.camera.three_d_camera.ThreeDCamera.reset_rotation_matrix) | Sets the value of self.rotation\_matrix to the matrix corresponding to the current position of the camera |
    | [`set_focal_distance`](#manim.camera.three_d_camera.ThreeDCamera.set_focal_distance) | Sets the focal\_distance of the Camera. |
    | [`set_gamma`](#manim.camera.three_d_camera.ThreeDCamera.set_gamma) | Sets the angle of rotation of the camera about the vector from the ORIGIN to the Camera. |
    | [`set_phi`](#manim.camera.three_d_camera.ThreeDCamera.set_phi) | Sets the polar angle i.e the angle between Z\_AXIS and Camera through ORIGIN in radians. |
    | [`set_theta`](#manim.camera.three_d_camera.ThreeDCamera.set_theta) | Sets the azimuthal angle i.e the angle that spins the camera around Z\_AXIS in radians. |
    | [`set_zoom`](#manim.camera.three_d_camera.ThreeDCamera.set_zoom) | Sets the zoom amount of the camera. |
    | `transform_points_pre_display` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `background_color` |  |
    | `background_opacity` |  |
    | `frame_center` |  |

    add\_fixed\_in\_frame\_mobjects(*\*mobjects*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   This method allows the mobject to have a fixed position,
        even when the camera moves around.
        E.G If it was passed through this method, at the top of the frame, it
        will continue to be displayed at the top of the frame.

        Highly useful when displaying Titles or formulae or the like.

        Parameters:
        :   **\*\*mobjects** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobject to fix in frame.

        Return type:
        :   None

    add\_fixed\_orientation\_mobjects(*\*mobjects*, *use\_static\_center\_func=False*, *center\_func=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   This method allows the mobject to have a fixed orientation,
        even when the camera moves around.
        E.G If it was passed through this method, facing the camera, it
        will continue to face the camera even as the camera moves.
        Highly useful when adding labels to graphs and the like.

        Parameters:
        :   - **\*mobjects** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobject whose orientation must be fixed.
            - **use\_static\_center\_func** (*bool*) – Whether or not to use the function that takes the mobject’s
              center as centerpoint, by default False
            - **center\_func** (*Callable**[**[**]**,* *TypeAliasForwardRef**(**'~manim.typing.Point3D'**)**]* *|* *None*) – The function which returns the centerpoint
              with respect to which the mobject will be oriented, by default None

        Return type:
        :   None

    capture\_mobjects(*mobjects*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Capture mobjects by printing them on `pixel_array`.

        This is the essential function that converts the contents of a Scene
        into an array, which is then converted to an image or video.

        Parameters:
        :   - **mobjects** (*Iterable**[*[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]*) – Mobjects to capture.
            - **kwargs** (*Any*) – Keyword arguments to be passed to [`get_mobjects_to_display()`](#manim.camera.three_d_camera.ThreeDCamera.get_mobjects_to_display).

        Return type:
        :   None

        Notes

        For a list of classes that can currently be rendered, see `display_funcs()`.

    generate\_rotation\_matrix()[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Generates a rotation matrix based off the current position of the camera.

        Returns:
        :   The matrix corresponding to the current position of the camera.

        Return type:
        :   np.array

    get\_fill\_rgbas(*vmobject*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Returns the RGBA array of the fill of the passed VMobject

        Parameters:
        :   **vmobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)) – The VMobject

        Returns:
        :   The RGBA Array of the fill of the VMobject

        Return type:
        :   np.array

    get\_focal\_distance()[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Returns focal\_distance of the Camera.

        Returns:
        :   The focal\_distance of the Camera in MUnits.

        Return type:
        :   float

    get\_gamma()[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Returns the rotation of the camera about the vector from the ORIGIN to the Camera.

        Returns:
        :   The angle of rotation of the camera about the vector
            from the ORIGIN to the Camera in radians

        Return type:
        :   float

    get\_mobjects\_to\_display(*\*args*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Used to get the list of mobjects to display
        with the camera.

        Parameters:
        :   - **mobjects** – The Mobjects
            - **include\_submobjects** – Whether or not to include the submobjects of mobjects, by default True
            - **excluded\_mobjects** – Any mobjects to exclude, by default None
            - **args** (*Any*)
            - **kwargs** (*Any*)

        Returns:
        :   list of mobjects

        Return type:
        :   list

    get\_phi()[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Returns the Polar angle (the angle off Z\_AXIS) phi.

        Returns:
        :   The Polar angle in radians.

        Return type:
        :   float

    get\_rotation\_matrix()[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Returns the matrix corresponding to the current position of the camera.

        Returns:
        :   The matrix corresponding to the current position of the camera.

        Return type:
        :   np.array

    get\_stroke\_rgbas(*vmobject*, *background=False*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Gets the RGBA array for the stroke of the passed
        VMobject.

        Parameters:
        :   - **vmobject** ([*VMobject*](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html)) – The VMobject
            - **background** (*bool*) – Whether or not to consider the background when getting the stroke
              RGBAs, by default False

        Returns:
        :   The RGBA array of the stroke.

        Return type:
        :   np.ndarray

    get\_theta()[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Returns the Azimuthal i.e the angle that spins the camera around the Z\_AXIS.

        Returns:
        :   The Azimuthal angle in radians.

        Return type:
        :   float

    get\_value\_trackers()[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   A list of [`ValueTrackers`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html) of phi, theta, focal\_distance,
        gamma and zoom.

        Returns:
        :   list of ValueTracker objects

        Return type:
        :   list

    get\_zoom()[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Returns the zoom amount of the camera.

        Returns:
        :   The zoom amount of the camera.

        Return type:
        :   float

    project\_point(*point*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Applies the current rotation\_matrix as a projection
        matrix to the passed point.

        Parameters:
        :   **point** ([*Point3D*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The point to project.

        Returns:
        :   The point after projection.

        Return type:
        :   np.array

    project\_points(*points*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Applies the current rotation\_matrix as a projection
        matrix to the passed array of points.

        Parameters:
        :   **points** ([*Point3D\_Array*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The list of points to project.

        Returns:
        :   The points after projecting.

        Return type:
        :   np.array

    remove\_fixed\_in\_frame\_mobjects(*\*mobjects*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   If a mobject was fixed in frame by passing it through
        [`add_fixed_in_frame_mobjects()`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_in_frame_mobjects), then this undoes that fixing.
        The Mobject will no longer be fixed in frame.

        Parameters:
        :   **mobjects** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobjects which need not be fixed in frame any longer.

        Return type:
        :   None

    remove\_fixed\_orientation\_mobjects(*\*mobjects*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   If a mobject was fixed in its orientation by passing it through
        [`add_fixed_orientation_mobjects()`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_orientation_mobjects), then this undoes that fixing.
        The Mobject will no longer have a fixed orientation.

        Parameters:
        :   **mobjects** ([*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)) – The mobjects whose orientation need not be fixed any longer.

        Return type:
        :   None

    reset\_rotation\_matrix()[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Sets the value of self.rotation\_matrix to
        the matrix corresponding to the current position of the camera

        Return type:
        :   None

    set\_focal\_distance(*value*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Sets the focal\_distance of the Camera.

        Parameters:
        :   **value** (*float*) – The focal\_distance of the Camera.

        Return type:
        :   None

    set\_gamma(*value*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Sets the angle of rotation of the camera about the vector from the ORIGIN to the Camera.

        Parameters:
        :   **value** (*float*) – The new angle of rotation of the camera.

        Return type:
        :   None

    set\_phi(*value*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Sets the polar angle i.e the angle between Z\_AXIS and Camera through ORIGIN in radians.

        Parameters:
        :   **value** (*float*) – The new value of the polar angle in radians.

        Return type:
        :   None

    set\_theta(*value*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Sets the azimuthal angle i.e the angle that spins the camera around Z\_AXIS in radians.

        Parameters:
        :   **value** (*float*) – The new value of the azimuthal angle in radians.

        Return type:
        :   None

    set\_zoom(*value*)[[source]](https://docs.manim.community/en/stable/_modules/manim/camera/three_d_camera.html)
    :   Sets the zoom amount of the camera.

        Parameters:
        :   **value** (*float*) – The zoom amount of the camera.

        Return type:
        :   None
