---
{
  "title": "ManimConfig",
  "source_url": "https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html",
  "tree_path": [
    "Reference Manual",
    "Configuration",
    "utils",
    "ManimConfig"
  ],
  "scraped_at": "2026-07-10T15:58:38"
}
---

# ManimConfig

Qualified name: `manim.\_config.utils.ManimConfig`

class ManimConfig[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
:   Bases: `MutableMapping`

    Dict-like class storing all config options.

    The global `config` object is an instance of this class, and acts as a
    single source of truth for all of the library’s customizable behavior.

    The global `config` object is capable of digesting different types of
    sources and converting them into a uniform interface. These sources are
    (in ascending order of precedence): configuration files, command line
    arguments, and programmatic changes. Regardless of how the user chooses to
    set a config option, she can access its current value using
    [`ManimConfig`](#manim._config.utils.ManimConfig)’s attributes and properties.

    Notes

    Each config option is implemented as a property of this class.

    Each config option can be set via a config file, using the full name of the
    property. If a config option has an associated CLI flag, then the flag is
    equal to the full name of the property. Those that admit an alternative
    flag or no flag at all are documented in the individual property’s
    docstring.

    Examples

    We use a copy of the global configuration object in the following
    examples for the sake of demonstration; you can skip these lines
    and just import `config` directly if you actually want to modify
    the configuration:

    Each config option allows for dict syntax and attribute syntax. For
    example, the following two lines are equivalent,

    The former is preferred; the latter is provided mostly for backwards
    compatibility.

    The config options are designed to keep internal consistency. For example,
    setting `frame_y_radius` will affect `frame_height`:

    There are many ways of interacting with config options. Take for example
    the config option `background_color`. There are three ways to change it:
    via a config file, via CLI flags, or programmatically.

    To set the background color via a config file, save the following
    `manim.cfg` file with the following contents.

    ```
    [CLI]
    background_color = WHITE
    ```

    In order to have this `.cfg` file apply to a manim scene, it needs to be
    placed in the same directory as the script,

    ```
    project/
    ├─scene.py
    └─manim.cfg
    ```

    Now, when the user executes

    ```
    manim scene.py
    ```

    the background of the scene will be set to `WHITE`. This applies regardless
    of where the manim command is invoked from.

    Command line arguments override `.cfg` files. In the previous example,
    executing

    ```
    manim scene.py -c BLUE
    ```

    will set the background color to BLUE, regardless of the contents of
    `manim.cfg`.

    Finally, any programmatic changes made within the scene script itself will
    override the command line arguments. For example, if `scene.py` contains
    the following

    the background color will be set to RED, regardless of the contents of
    `manim.cfg` or the CLI arguments used when invoking manim.

    Methods

    |  |  |
    | --- | --- |
    | [`copy`](#manim._config.utils.ManimConfig.copy) | Deepcopy the contents of this ManimConfig. |
    | [`digest_args`](#manim._config.utils.ManimConfig.digest_args) | Process the config options present in CLI arguments. |
    | [`digest_file`](#manim._config.utils.ManimConfig.digest_file) | Process the config options present in a `.cfg` file. |
    | [`digest_parser`](#manim._config.utils.ManimConfig.digest_parser) | Process the config options present in a `ConfigParser` object. |
    | [`get_dir`](#manim._config.utils.ManimConfig.get_dir) | Resolve a config option that stores a directory. |
    | `resolve_movie_file_extension` |  |
    | [`update`](#manim._config.utils.ManimConfig.update) | Digest the options found in another [`ManimConfig`](#manim._config.utils.ManimConfig) or in a dict. |

    Attributes

    |  |  |
    | --- | --- |
    | [`aspect_ratio`](#manim._config.utils.ManimConfig.aspect_ratio) | Aspect ratio (width / height) in pixels (--resolution, -r). |
    | [`assets_dir`](#manim._config.utils.ManimConfig.assets_dir) | Directory to locate video assets (no flag). |
    | [`background_color`](#manim._config.utils.ManimConfig.background_color) | Background color of the scene (-c). |
    | [`background_opacity`](#manim._config.utils.ManimConfig.background_opacity) | A number between 0.0 (fully transparent) and 1.0 (fully opaque). |
    | [`bottom`](#manim._config.utils.ManimConfig.bottom) | Coordinate at the center bottom of the frame. |
    | [`custom_folders`](#manim._config.utils.ManimConfig.custom_folders) | Whether to use custom folder output. |
    | [`disable_caching`](#manim._config.utils.ManimConfig.disable_caching) | Whether to use scene caching. |
    | [`disable_caching_warning`](#manim._config.utils.ManimConfig.disable_caching_warning) | Whether a warning is raised if there are too much submobjects to hash. |
    | [`dry_run`](#manim._config.utils.ManimConfig.dry_run) | Whether dry run is enabled. |
    | [`enable_gui`](#manim._config.utils.ManimConfig.enable_gui) | Enable GUI interaction. |
    | [`enable_wireframe`](#manim._config.utils.ManimConfig.enable_wireframe) | Whether to enable wireframe debugging mode in opengl. |
    | [`ffmpeg_loglevel`](#manim._config.utils.ManimConfig.ffmpeg_loglevel) | Verbosity level of ffmpeg (no flag). |
    | [`flush_cache`](#manim._config.utils.ManimConfig.flush_cache) | Whether to delete all the cached partial movie files. |
    | [`force_window`](#manim._config.utils.ManimConfig.force_window) | Whether to force window when using the opengl renderer. |
    | [`format`](#manim._config.utils.ManimConfig.format) | File format; "png", "gif", "mp4", "webm" or "mov". |
    | [`frame_height`](#manim._config.utils.ManimConfig.frame_height) | Frame height in logical units (no flag). |
    | [`frame_rate`](#manim._config.utils.ManimConfig.frame_rate) | Frame rate in frames per second. |
    | [`frame_size`](#manim._config.utils.ManimConfig.frame_size) | Tuple with (pixel width, pixel height) (no flag). |
    | [`frame_width`](#manim._config.utils.ManimConfig.frame_width) | Frame width in logical units (no flag). |
    | [`frame_x_radius`](#manim._config.utils.ManimConfig.frame_x_radius) | Half the frame width (no flag). |
    | [`frame_y_radius`](#manim._config.utils.ManimConfig.frame_y_radius) | Half the frame height (no flag). |
    | [`from_animation_number`](#manim._config.utils.ManimConfig.from_animation_number) | Start rendering animations at this number (-n). |
    | [`fullscreen`](#manim._config.utils.ManimConfig.fullscreen) | Expand the window to its maximum possible size. |
    | [`gui_location`](#manim._config.utils.ManimConfig.gui_location) | Location parameters for the GUI window (e.g., screen coordinates or layout settings). |
    | [`images_dir`](#manim._config.utils.ManimConfig.images_dir) | Directory to place images (no flag). |
    | [`input_file`](#manim._config.utils.ManimConfig.input_file) | Input file name. |
    | [`left_side`](#manim._config.utils.ManimConfig.left_side) | Coordinate at the middle left of the frame. |
    | [`log_dir`](#manim._config.utils.ManimConfig.log_dir) | Directory to place logs. |
    | [`log_to_file`](#manim._config.utils.ManimConfig.log_to_file) | Whether to save logs to a file. |
    | [`max_files_cached`](#manim._config.utils.ManimConfig.max_files_cached) | Maximum number of files cached. |
    | [`media_dir`](#manim._config.utils.ManimConfig.media_dir) | Main output directory. |
    | [`media_embed`](#manim._config.utils.ManimConfig.media_embed) | Whether to embed videos in Jupyter notebook. |
    | [`media_width`](#manim._config.utils.ManimConfig.media_width) | Media width in Jupyter notebook. |
    | [`movie_file_extension`](#manim._config.utils.ManimConfig.movie_file_extension) | Either .mp4, .webm or .mov. |
    | [`no_latex_cleanup`](#manim._config.utils.ManimConfig.no_latex_cleanup) | Prevents deletion of .aux, .dvi, and .log files produced by Tex and MathTex. |
    | [`notify_outdated_version`](#manim._config.utils.ManimConfig.notify_outdated_version) | Whether to notify if there is a version update available. |
    | [`output_file`](#manim._config.utils.ManimConfig.output_file) | Output file name (-o). |
    | [`partial_movie_dir`](#manim._config.utils.ManimConfig.partial_movie_dir) | Directory to place partial movie files (no flag). |
    | [`pixel_height`](#manim._config.utils.ManimConfig.pixel_height) | Frame height in pixels (--resolution, -r). |
    | [`pixel_width`](#manim._config.utils.ManimConfig.pixel_width) | Frame width in pixels (--resolution, -r). |
    | [`plugins`](#manim._config.utils.ManimConfig.plugins) | List of plugins to enable. |
    | [`preview`](#manim._config.utils.ManimConfig.preview) | Whether to play the rendered movie (-p). |
    | `preview_command` |  |
    | [`progress_bar`](#manim._config.utils.ManimConfig.progress_bar) | Whether to show progress bars while rendering animations. |
    | [`quality`](#manim._config.utils.ManimConfig.quality) | Video quality (-q). |
    | [`renderer`](#manim._config.utils.ManimConfig.renderer) | The currently active renderer. |
    | [`right_side`](#manim._config.utils.ManimConfig.right_side) | Coordinate at the middle right of the frame. |
    | [`save_as_gif`](#manim._config.utils.ManimConfig.save_as_gif) | Whether to save the rendered scene in .gif format (-i). |
    | [`save_last_frame`](#manim._config.utils.ManimConfig.save_last_frame) | Whether to save the last frame of the scene as an image file (-s). |
    | [`save_pngs`](#manim._config.utils.ManimConfig.save_pngs) | Whether to save all frames in the scene as images files (-g). |
    | [`save_sections`](#manim._config.utils.ManimConfig.save_sections) | Whether to save single videos for each section in addition to the movie file. |
    | [`scene_names`](#manim._config.utils.ManimConfig.scene_names) | Scenes to play from file. |
    | [`sections_dir`](#manim._config.utils.ManimConfig.sections_dir) | Directory to place section videos (no flag). |
    | [`seed`](#manim._config.utils.ManimConfig.seed) | Random seed for reproducibility. |
    | [`show_in_file_browser`](#manim._config.utils.ManimConfig.show_in_file_browser) | Whether to show the output file in the file browser (-f). |
    | [`tex_dir`](#manim._config.utils.ManimConfig.tex_dir) | Directory to place tex (no flag). |
    | [`tex_template`](#manim._config.utils.ManimConfig.tex_template) | Template used when rendering Tex. |
    | [`tex_template_file`](#manim._config.utils.ManimConfig.tex_template_file) | File to read Tex template from (no flag). |
    | [`text_dir`](#manim._config.utils.ManimConfig.text_dir) | Directory to place text (no flag). |
    | [`top`](#manim._config.utils.ManimConfig.top) | Coordinate at the center top of the frame. |
    | [`transparent`](#manim._config.utils.ManimConfig.transparent) | Whether the background opacity is less than 1.0 (-t). |
    | [`upto_animation_number`](#manim._config.utils.ManimConfig.upto_animation_number) | Stop rendering animations at this number. |
    | [`use_projection_fill_shaders`](#manim._config.utils.ManimConfig.use_projection_fill_shaders) | Use shaders for OpenGLVMobject fill which are compatible with transformation matrices. |
    | [`use_projection_stroke_shaders`](#manim._config.utils.ManimConfig.use_projection_stroke_shaders) | Use shaders for OpenGLVMobject stroke which are compatible with transformation matrices. |
    | [`verbosity`](#manim._config.utils.ManimConfig.verbosity) | Logger verbosity; "DEBUG", "INFO", "WARNING", "ERROR", or "CRITICAL" (-v). |
    | [`video_dir`](#manim._config.utils.ManimConfig.video_dir) | Directory to place videos (no flag). |
    | [`window_monitor`](#manim._config.utils.ManimConfig.window_monitor) | The monitor on which the scene will be rendered. |
    | [`window_position`](#manim._config.utils.ManimConfig.window_position) | Set the position of preview window. |
    | [`window_size`](#manim._config.utils.ManimConfig.window_size) | The size of the opengl window. |
    | [`write_all`](#manim._config.utils.ManimConfig.write_all) | Whether to render all scenes in the input file (-a). |
    | [`write_to_movie`](#manim._config.utils.ManimConfig.write_to_movie) | Whether to render the scene to a movie file (-w). |
    | [`zero_pad`](#manim._config.utils.ManimConfig.zero_pad) | PNG zero padding. |

    \_set\_between(*key*, *val*, *lo*, *hi*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
    :   Set `key` to `val` if lo <= val <= hi.

        Parameters:
        :   - **key** (*str*)
            - **val** (*float*)
            - **lo** (*float*)
            - **hi** (*float*)

        Return type:
        :   None

    \_set\_boolean(*key*, *val*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
    :   Set `key` to `val` if `val` is Boolean.

        Parameters:
        :   - **key** (*str*)
            - **val** (*Any*)

        Return type:
        :   None

    \_set\_from\_enum(*key*, *enum\_value*, *enum\_class*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
    :   Set `key` to the enum object with value `enum_value` in the given
        `enum_class`.

        Tests:

        Parameters:
        :   - **key** (*str*)
            - **enum\_value** (*Any*)
            - **enum\_class** (*EnumMeta*)

        Return type:
        :   None

    \_set\_from\_list(*key*, *val*, *values*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
    :   Set `key` to `val` if `val` is contained in `values`.

        Parameters:
        :   - **key** (*str*)
            - **val** (*Any*)
            - **values** (*list**[**Any**]*)

        Return type:
        :   None

    \_set\_int\_between(*key*, *val*, *lo*, *hi*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
    :   Set `key` to `val` if lo <= val <= hi.

        Parameters:
        :   - **key** (*str*)
            - **val** (*int*)
            - **lo** (*int*)
            - **hi** (*int*)

        Return type:
        :   None

    \_set\_pos\_number(*key*, *val*, *allow\_inf*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
    :   Set `key` to `val` if `val` is a positive integer.

        Parameters:
        :   - **key** (*str*)
            - **val** (*int*)
            - **allow\_inf** (*bool*)

        Return type:
        :   None

    \_set\_str(*key*, *val*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
    :   Set `key` to `val` if `val` is a string.

        Parameters:
        :   - **key** (*str*)
            - **val** (*Any*)

        Return type:
        :   None

    property aspect\_ratio: float
    :   Aspect ratio (width / height) in pixels (–resolution, -r).

    property assets\_dir: str
    :   Directory to locate video assets (no flag).

    property background\_color: [ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html)
    :   Background color of the scene (-c).

    property background\_opacity: float
    :   A number between 0.0 (fully transparent) and 1.0 (fully opaque).

    property bottom: [Vector3D](https://docs.manim.community/en/stable/reference/manim.typing.html)
    :   Coordinate at the center bottom of the frame.

    copy()[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
    :   Deepcopy the contents of this ManimConfig.

        Returns:
        :   A copy of this object containing no shared references.

        Return type:
        :   [`ManimConfig`](#manim._config.utils.ManimConfig)

        See also

        `tempconfig()`

        Notes

        This is the main mechanism behind `tempconfig()`.

    property custom\_folders: str
    :   Whether to use custom folder output.

    digest\_args(*args*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
    :   Process the config options present in CLI arguments.

        Parameters:
        :   **args** (*argparse.Namespace*) – An object returned by `main_utils.parse_args()`.

        Returns:
        :   **self** – This object, after processing the contents of `parser`.

        Return type:
        :   [`ManimConfig`](#manim._config.utils.ManimConfig)

        See also

        `main_utils.parse_args()`, [`digest_parser()`](#manim._config.utils.ManimConfig.digest_parser),
        [`digest_file()`](#manim._config.utils.ManimConfig.digest_file)

        Notes

        If `args.config_file` is a non-empty string, `ManimConfig` tries to digest the
        contents of said file with [`digest_file()`](#manim._config.utils.ManimConfig.digest_file) before
        digesting any other CLI arguments.

    digest\_file(*filename*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
    :   Process the config options present in a `.cfg` file.

        This method processes a single `.cfg` file, whereas
        [`digest_parser()`](#manim._config.utils.ManimConfig.digest_parser) can process arbitrary parsers, built
        perhaps from multiple `.cfg` files.

        Parameters:
        :   **filename** ([*StrPath*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – Path to the `.cfg` file.

        Returns:
        :   **self** – This object, after processing the contents of `filename`.

        Return type:
        :   [`ManimConfig`](#manim._config.utils.ManimConfig)

        See also

        [`digest_file()`](#manim._config.utils.ManimConfig.digest_file), [`digest_args()`](#manim._config.utils.ManimConfig.digest_args), [`make_config_parser()`](https://docs.manim.community/en/stable/reference/manim._config.utils.html)

        Notes

        If there are multiple `.cfg` files to process, it is always more
        efficient to parse them into a single `ConfigParser` object
        first and digesting them with one call to
        [`digest_parser()`](#manim._config.utils.ManimConfig.digest_parser), instead of calling this method
        multiple times.

    digest\_parser(*parser*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
    :   Process the config options present in a `ConfigParser` object.

        This method processes arbitrary parsers, not only those read from a
        single file, whereas [`digest_file()`](#manim._config.utils.ManimConfig.digest_file) can only process one
        file at a time.

        Parameters:
        :   **parser** (*configparser.ConfigParser*) – An object reflecting the contents of one or many `.cfg` files. In
            particular, it may reflect the contents of multiple files that have
            been parsed in a cascading fashion.

        Returns:
        :   **self** – This object, after processing the contents of `parser`.

        Return type:
        :   [`ManimConfig`](#manim._config.utils.ManimConfig)

        See also

        [`make_config_parser()`](https://docs.manim.community/en/stable/reference/manim._config.utils.html), [`digest_file()`](#manim._config.utils.ManimConfig.digest_file), [`digest_args()`](#manim._config.utils.ManimConfig.digest_args)

        Notes

        If there are multiple `.cfg` files to process, it is always more
        efficient to parse them into a single `ConfigParser` object
        first, and then call this function once (instead of calling
        [`digest_file()`](#manim._config.utils.ManimConfig.digest_file) multiple times).

        Examples

        To digest the config options set in two files, first create a
        ConfigParser and parse both files and then digest the parser:

        In fact, the global `config` object is initialized like so:

    property disable\_caching: bool
    :   Whether to use scene caching.

    property disable\_caching\_warning: bool
    :   Whether a warning is raised if there are too much submobjects to hash.

    property dry\_run: bool
    :   Whether dry run is enabled.

    property enable\_gui: bool
    :   Enable GUI interaction.

    property enable\_wireframe: bool
    :   Whether to enable wireframe debugging mode in opengl.

    property ffmpeg\_loglevel: str
    :   Verbosity level of ffmpeg (no flag).

    property flush\_cache: bool
    :   Whether to delete all the cached partial movie files.

    property force\_window: bool
    :   Whether to force window when using the opengl renderer.

    property format: str | None
    :   File format; “png”, “gif”, “mp4”, “webm” or “mov”.

    property frame\_height: float
    :   Frame height in logical units (no flag).

    property frame\_rate: float
    :   Frame rate in frames per second.

    property frame\_size: tuple[int, int]
    :   Tuple with (pixel width, pixel height) (no flag).

    property frame\_width: float
    :   Frame width in logical units (no flag).

    property frame\_x\_radius: float
    :   Half the frame width (no flag).

    property frame\_y\_radius: float
    :   Half the frame height (no flag).

    property from\_animation\_number: int
    :   Start rendering animations at this number (-n).

    property fullscreen: bool
    :   Expand the window to its maximum possible size.

    get\_dir(*key*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
    :   Resolve a config option that stores a directory.

        Config options that store directories may depend on one another. This
        method is used to provide the actual directory to the end user.

        Parameters:
        :   - **key** (*str*) – The config option to be resolved. Must be an option ending in
              `'_dir'`, for example `'media_dir'` or `'video_dir'`.
            - **kwargs** (*Any*) – Any strings to be used when resolving the directory.

        Returns:
        :   Path to the requested directory. If the path resolves to the empty
            string, return `None` instead.

        Return type:
        :   `pathlib.Path`

        Raises:
        :   **KeyError** – When `key` is not a config option that stores a directory and
            thus [`get_dir()`](#manim._config.utils.ManimConfig.get_dir) is not appropriate; or when
            `key` is appropriate but there is not enough information to
            resolve the directory.

        Notes

        Standard `str.format()` syntax is used to resolve the paths so the
        paths may contain arbitrary placeholders using f-string notation.
        However, these will require `kwargs` to contain the required values.

        Examples

        The value of `config.tex_dir` is `'{media_dir}/Tex'` by default,
        i.e. it is a subfolder of wherever `config.media_dir` is located. In
        order to get the *actual* directory, use [`get_dir()`](#manim._config.utils.ManimConfig.get_dir).

        Resolving directories is done in a lazy way, at the last possible
        moment, to reflect any changes in other config options:

        Some directories depend on information that is not available to
        [`ManimConfig`](#manim._config.utils.ManimConfig). For example, the default value of video\_dir
        includes the name of the input file and the video quality
        (e.g. 480p15). This informamtion has to be supplied via `kwargs`:

        Note the quality does not need to be passed as keyword argument since
        [`ManimConfig`](#manim._config.utils.ManimConfig) does store information about quality.

        Directories may be recursively defined. For example, the config option
        `partial_movie_dir` depends on `video_dir`, which in turn depends
        on `media_dir`:

        Standard f-string syntax is used. Arbitrary names can be used when
        defining directories, as long as the corresponding values are passed to
        [`ManimConfig.get_dir()`](#manim._config.utils.ManimConfig.get_dir) via `kwargs`.

    property gui\_location: tuple[int, ...]
    :   Location parameters for the GUI window (e.g., screen coordinates or layout settings).

    property images\_dir: str
    :   Directory to place images (no flag). See [`ManimConfig.get_dir()`](#manim._config.utils.ManimConfig.get_dir).

    property input\_file: str | Path
    :   Input file name.

    property left\_side: [Vector3D](https://docs.manim.community/en/stable/reference/manim.typing.html)
    :   Coordinate at the middle left of the frame.

    property log\_dir: str
    :   Directory to place logs. See [`ManimConfig.get_dir()`](#manim._config.utils.ManimConfig.get_dir).

    property log\_to\_file: bool
    :   Whether to save logs to a file.

    property max\_files\_cached: int
    :   Maximum number of files cached. Use -1 for infinity (no flag).

    property media\_dir: str
    :   Main output directory. See [`ManimConfig.get_dir()`](#manim._config.utils.ManimConfig.get_dir).

    property media\_embed: bool | None
    :   Whether to embed videos in Jupyter notebook.

    property media\_width: str
    :   Media width in Jupyter notebook.

    property movie\_file\_extension: str
    :   Either .mp4, .webm or .mov.

    property no\_latex\_cleanup: bool
    :   Prevents deletion of .aux, .dvi, and .log files produced by Tex and MathTex.

    property notify\_outdated\_version: bool
    :   Whether to notify if there is a version update available.

    property output\_file: str
    :   Output file name (-o).

    property partial\_movie\_dir: str
    :   Directory to place partial movie files (no flag). See [`ManimConfig.get_dir()`](#manim._config.utils.ManimConfig.get_dir).

    property pixel\_height: int
    :   Frame height in pixels (–resolution, -r).

    property pixel\_width: int
    :   Frame width in pixels (–resolution, -r).

    property plugins: list[str]
    :   List of plugins to enable.

    property preview: bool
    :   Whether to play the rendered movie (-p).

    property progress\_bar: str
    :   Whether to show progress bars while rendering animations.

    property quality: str | None
    :   Video quality (-q).

    property renderer: [RendererType](https://docs.manim.community/en/stable/reference/manim.constants.RendererType.html)
    :   The currently active renderer.

        Populated with one of the available renderers in [`RendererType`](https://docs.manim.community/en/stable/reference/manim.constants.RendererType.html).

        Tests:

        Check that capitalization of renderer types is irrelevant:

        ```
        >>> test_config.renderer = 'OpenGL'
        >>> test_config.renderer = 'cAirO'
        ```

    property right\_side: [Vector3D](https://docs.manim.community/en/stable/reference/manim.typing.html)
    :   Coordinate at the middle right of the frame.

    property save\_as\_gif: bool
    :   Whether to save the rendered scene in .gif format (-i).

    property save\_last\_frame: bool
    :   Whether to save the last frame of the scene as an image file (-s).

    property save\_pngs: bool
    :   Whether to save all frames in the scene as images files (-g).

    property save\_sections: bool
    :   Whether to save single videos for each section in addition to the movie file.

    property scene\_names: list[str]
    :   Scenes to play from file.

    property sections\_dir: str
    :   Directory to place section videos (no flag). See [`ManimConfig.get_dir()`](#manim._config.utils.ManimConfig.get_dir).

    property seed: int | None
    :   Random seed for reproducibility. None means no seed is set.

    property show\_in\_file\_browser: bool
    :   Whether to show the output file in the file browser (-f).

    property tex\_dir: str
    :   Directory to place tex (no flag). See [`ManimConfig.get_dir()`](#manim._config.utils.ManimConfig.get_dir).

    property tex\_template: [TexTemplate](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html)
    :   Template used when rendering Tex. See [`TexTemplate`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html).

    property tex\_template\_file: Path
    :   File to read Tex template from (no flag). See [`TexTemplate`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html).

    property text\_dir: str
    :   Directory to place text (no flag). See [`ManimConfig.get_dir()`](#manim._config.utils.ManimConfig.get_dir).

    property top: [Vector3D](https://docs.manim.community/en/stable/reference/manim.typing.html)
    :   Coordinate at the center top of the frame.

    property transparent: bool
    :   Whether the background opacity is less than 1.0 (-t).

    update(*obj*)[[source]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html)
    :   Digest the options found in another [`ManimConfig`](#manim._config.utils.ManimConfig) or in a dict.

        Similar to `dict.update()`, replaces the values of this object with
        those of `obj`.

        Parameters:
        :   **obj** ([*ManimConfig*](#manim._config.utils.ManimConfig) *|* *dict**[**str**,* *Any**]*) – The object to copy values from.

        Return type:
        :   None

        Raises:
        :   **AttributeError** – If `obj` is a dict but contains keys that do not belong to any
            config options.

        See also

        [`digest_file()`](#manim._config.utils.ManimConfig.digest_file), [`digest_args()`](#manim._config.utils.ManimConfig.digest_args), [`digest_parser()`](#manim._config.utils.ManimConfig.digest_parser)

    property upto\_animation\_number: int
    :   Stop rendering animations at this number. Use -1 to avoid skipping (-n).

    property use\_projection\_fill\_shaders: bool
    :   Use shaders for OpenGLVMobject fill which are compatible with transformation matrices.

    property use\_projection\_stroke\_shaders: bool
    :   Use shaders for OpenGLVMobject stroke which are compatible with transformation matrices.

    property verbosity: str
    :   Logger verbosity; “DEBUG”, “INFO”, “WARNING”, “ERROR”, or “CRITICAL” (-v).

    property video\_dir: str
    :   Directory to place videos (no flag). See [`ManimConfig.get_dir()`](#manim._config.utils.ManimConfig.get_dir).

    property window\_monitor: int
    :   The monitor on which the scene will be rendered.

    property window\_position: str
    :   Set the position of preview window. You can use directions, e.g. UL/DR/ORIGIN/LEFT…or the position(pixel) of the upper left corner of the window, e.g. ‘960,540’.

    property window\_size: str | tuple[int, ...]
    :   The size of the opengl window. ‘default’ to automatically scale the window based on the display monitor.

    property write\_all: bool
    :   Whether to render all scenes in the input file (-a).

    property write\_to\_movie: bool
    :   Whether to render the scene to a movie file (-w).

    property zero\_pad: int
    :   PNG zero padding. A number between 0 (no zero padding) and 9 (9 columns minimum).
