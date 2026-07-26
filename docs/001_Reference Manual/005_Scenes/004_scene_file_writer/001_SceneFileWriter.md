---
{
  "title": "SceneFileWriter",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html",
  "tree_path": [
    "Reference Manual",
    "Scenes",
    "scene_file_writer",
    "SceneFileWriter"
  ],
  "scraped_at": "2026-07-10T16:00:53"
}
---

# SceneFileWriter

Qualified name: `manim.scene.scene\_file\_writer.SceneFileWriter`

class SceneFileWriter(*renderer*, *scene\_name*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
:   Bases: `object`

    SceneFileWriter is the object that actually writes the animations
    played, into video files, using FFMPEG.
    This is mostly for Manim’s internal use. You will rarely, if ever,
    have to use the methods for this class, unless tinkering with the very
    fabric of Manim’s reality.

    Parameters:
    :   - **renderer** (*CairoRenderer* *|* *OpenGLRenderer*)
        - **scene\_name** (*str*)
        - **kwargs** (*Any*)

    sections
    :   used to segment scene

        Type:
        :   list of [`Section`](https://docs.manim.community/en/stable/reference/manim.scene.section.Section.html)

    sections\_output\_dir
    :   where are section videos stored

        Type:
        :   `pathlib.Path`

    output\_name
    :   name of movie without extension and basis for section video names

        Type:
        :   str

    Some useful attributes are:
    :   “write\_to\_movie” (bool=False)
        :   Whether or not to write the animations into a video file.

        “movie\_file\_extension” (str=”.mp4”)
        :   The file-type extension of the outputted video.

        “partial\_movie\_files”
        :   List of all the partial-movie files.

    Methods

    |  |  |
    | --- | --- |
    | [`add_audio_segment`](#manim.scene.scene_file_writer.SceneFileWriter.add_audio_segment) | This method adds an audio segment from an AudioSegment type object and suitable parameters. |
    | [`add_partial_movie_file`](#manim.scene.scene_file_writer.SceneFileWriter.add_partial_movie_file) | Adds a new partial movie file path to `scene.partial_movie_files` and current section from a hash. |
    | [`add_sound`](#manim.scene.scene_file_writer.SceneFileWriter.add_sound) | This method adds an audio segment from a sound file. |
    | [`begin_animation`](#manim.scene.scene_file_writer.SceneFileWriter.begin_animation) | Used internally by manim to stream the animation to FFMPEG for displaying or writing to a file. |
    | [`clean_cache`](#manim.scene.scene_file_writer.SceneFileWriter.clean_cache) | Will clean the cache by removing the oldest partial\_movie\_files. |
    | [`close_partial_movie_stream`](#manim.scene.scene_file_writer.SceneFileWriter.close_partial_movie_stream) | Close the currently opened video container. |
    | `combine_files` |  |
    | [`combine_to_movie`](#manim.scene.scene_file_writer.SceneFileWriter.combine_to_movie) | Used internally by Manim to combine the separate partial movie files that make up a Scene into a single video file for that Scene. |
    | [`combine_to_section_videos`](#manim.scene.scene_file_writer.SceneFileWriter.combine_to_section_videos) | Concatenate partial movie files for each section. |
    | [`create_audio_segment`](#manim.scene.scene_file_writer.SceneFileWriter.create_audio_segment) | Creates an empty, silent, Audio Segment. |
    | [`encode_and_write_frame`](#manim.scene.scene_file_writer.SceneFileWriter.encode_and_write_frame) | For internal use only: takes a given frame in `np.ndarray` format and writes it to the stream |
    | [`end_animation`](#manim.scene.scene_file_writer.SceneFileWriter.end_animation) | Internally used by Manim to stop streaming to FFMPEG gracefully. |
    | [`finish`](#manim.scene.scene_file_writer.SceneFileWriter.finish) | Finishes writing to the FFMPEG buffer or writing images to output directory. |
    | [`finish_last_section`](#manim.scene.scene_file_writer.SceneFileWriter.finish_last_section) | Delete current section if it is empty. |
    | [`flush_cache_directory`](#manim.scene.scene_file_writer.SceneFileWriter.flush_cache_directory) | Delete all the cached partial movie files |
    | [`get_resolution_directory`](#manim.scene.scene_file_writer.SceneFileWriter.get_resolution_directory) | Get the name of the resolution directory directly containing the video file. |
    | [`init_audio`](#manim.scene.scene_file_writer.SceneFileWriter.init_audio) | Preps the writer for adding audio to the movie. |
    | [`init_output_directories`](#manim.scene.scene_file_writer.SceneFileWriter.init_output_directories) | Initialise output directories. |
    | [`is_already_cached`](#manim.scene.scene_file_writer.SceneFileWriter.is_already_cached) | Will check if a file named with hash\_invocation exists. |
    | [`listen_and_write`](#manim.scene.scene_file_writer.SceneFileWriter.listen_and_write) | For internal use only: blocks until new frame is available on the queue. |
    | [`next_section`](#manim.scene.scene_file_writer.SceneFileWriter.next_section) | Create segmentation cut here. |
    | [`open_partial_movie_stream`](#manim.scene.scene_file_writer.SceneFileWriter.open_partial_movie_stream) | Open a container holding a video stream. |
    | `output_image` |  |
    | [`print_file_ready_message`](#manim.scene.scene_file_writer.SceneFileWriter.print_file_ready_message) | Prints the "File Ready" message to STDOUT. |
    | [`save_image`](#manim.scene.scene_file_writer.SceneFileWriter.save_image) | This method saves the image passed to it in the default image directory. |
    | [`write_frame`](#manim.scene.scene_file_writer.SceneFileWriter.write_frame) | Used internally by Manim to write a frame to the FFMPEG input buffer. |
    | [`write_subcaption_file`](#manim.scene.scene_file_writer.SceneFileWriter.write_subcaption_file) | Writes the subcaption file. |

    Attributes

    |  |  |
    | --- | --- |
    | `force_output_as_scene_name` |  |

    add\_audio\_segment(*new\_segment*, *time=None*, *gain\_to\_background=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   This method adds an audio segment from an AudioSegment type object
        and suitable parameters.

        Parameters:
        :   - **new\_segment** (*AudioSegment*) – The audio segment to add
            - **time** (*float* *|* *None*) – the timestamp at which the sound should be added.
            - **gain\_to\_background** (*float* *|* *None*) – The gain of the segment from the background.

        Return type:
        :   None

    add\_partial\_movie\_file(*hash\_animation*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Adds a new partial movie file path to `scene.partial_movie_files`
        and current section from a hash.

        This method will compute the path from the hash. In addition to that it
        adds the new animation to the current section.

        Parameters:
        :   **hash\_animation** (*str* *|* *None*) – Hash of the animation.

        Return type:
        :   None

    add\_sound(*sound\_file*, *time=None*, *gain=None*, *\*\*kwargs*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   This method adds an audio segment from a sound file.

        Parameters:
        :   - **sound\_file** ([*StrPath*](https://docs.manim.community/en/stable/reference/manim.typing.html)) – The path to the sound file.
            - **time** (*float* *|* *None*) – The timestamp at which the audio should be added.
            - **gain** (*float* *|* *None*) – The gain of the given audio segment.
            - **\*\*kwargs** (*Any*) – This method uses add\_audio\_segment, so any keyword arguments
              used there can be referenced here.

        Return type:
        :   None

    begin\_animation(*allow\_write=False*, *file\_path=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Used internally by manim to stream the animation to FFMPEG for
        displaying or writing to a file.

        Parameters:
        :   - **allow\_write** (*bool*) – Whether or not to write to a video file.
            - **file\_path** (*TypeAliasForwardRef**(**'~manim.typing.StrPath'**)* *|* *None*)

        Return type:
        :   None

    clean\_cache()[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Will clean the cache by removing the oldest partial\_movie\_files.

        Return type:
        :   None

    close\_partial\_movie\_stream()[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Close the currently opened video container.

        Used internally by Manim to first flush the remaining packages
        in the video stream holding a partial file, and then close
        the corresponding container.

        Return type:
        :   None

    combine\_to\_movie()[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Used internally by Manim to combine the separate
        partial movie files that make up a Scene into a single
        video file for that Scene.

        Return type:
        :   None

    combine\_to\_section\_videos()[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Concatenate partial movie files for each section.

        Return type:
        :   None

    create\_audio\_segment()[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Creates an empty, silent, Audio Segment.

        Return type:
        :   None

    encode\_and\_write\_frame(*frame*, *num\_frames*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   For internal use only: takes a given frame in `np.ndarray` format and
        writes it to the stream

        Parameters:
        :   - **frame** ([*PixelArray*](https://docs.manim.community/en/stable/reference/manim.typing.html))
            - **num\_frames** (*int*)

        Return type:
        :   None

    end\_animation(*allow\_write=False*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Internally used by Manim to stop streaming to FFMPEG gracefully.

        Parameters:
        :   **allow\_write** (*bool*) – Whether or not to write to a video file.

        Return type:
        :   None

    finish()[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Finishes writing to the FFMPEG buffer or writing images to output directory.
        Combines the partial movie files into the whole scene.
        If save\_last\_frame is True, saves the last frame in the default image directory.

        Return type:
        :   None

    finish\_last\_section()[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Delete current section if it is empty.

        Return type:
        :   None

    flush\_cache\_directory()[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Delete all the cached partial movie files

        Return type:
        :   None

    get\_resolution\_directory()[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Get the name of the resolution directory directly containing
        the video file.

        This method gets the name of the directory that immediately contains the
        video file. This name is `<height_in_pixels_of_video>p<frame_rate>`.
        For example, if you are rendering an 854x480 px animation at 15fps,
        the name of the directory that immediately contains the video, file
        will be `480p15`.

        The file structure should look something like:

        Returns:
        :   The name of the directory.

        Return type:
        :   `str`

    init\_audio()[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Preps the writer for adding audio to the movie.

        Return type:
        :   None

    init\_output\_directories(*scene\_name*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Initialise output directories.

        Notes

        The directories are read from `config`, for example
        `config['media_dir']`. If the target directories don’t already
        exist, they will be created.

        Parameters:
        :   **scene\_name** (*str*)

        Return type:
        :   None

    is\_already\_cached(*hash\_invocation*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Will check if a file named with hash\_invocation exists.

        Parameters:
        :   **hash\_invocation** (*str*) – The hash corresponding to an invocation to either scene.play or scene.wait.

        Returns:
        :   Whether the file exists.

        Return type:
        :   `bool`

    listen\_and\_write()[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   For internal use only: blocks until new frame is available on the queue.

        Return type:
        :   None

    next\_section(*name*, *type\_*, *skip\_animations*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Create segmentation cut here.

        Parameters:
        :   - **name** (*str*)
            - **type\_** (*str*)
            - **skip\_animations** (*bool*)

        Return type:
        :   None

    open\_partial\_movie\_stream(*file\_path=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Open a container holding a video stream.

        This is used internally by Manim initialize the container holding
        the video stream of a partial movie file.

        Parameters:
        :   **file\_path** (*TypeAliasForwardRef**(**'~manim.typing.StrPath'**)* *|* *None*)

        Return type:
        :   None

    print\_file\_ready\_message(*file\_path*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Prints the “File Ready” message to STDOUT.

        Parameters:
        :   **file\_path** ([*StrPath*](https://docs.manim.community/en/stable/reference/manim.typing.html))

        Return type:
        :   None

    save\_image(*image*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   This method saves the image passed to it in the default image directory.

        Parameters:
        :   **image** (*Image*) – The pixel array of the image to save.

        Return type:
        :   None

    write\_frame(*frame\_or\_renderer*, *num\_frames=1*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Used internally by Manim to write a frame to the FFMPEG input buffer.

        Parameters:
        :   - **frame\_or\_renderer** ([*PixelArray*](https://docs.manim.community/en/stable/reference/manim.typing.html) *|* *OpenGLRenderer*) – Pixel array of the frame.
            - **num\_frames** (*int*) – The number of times to write frame.

        Return type:
        :   None

    write\_subcaption\_file()[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
    :   Writes the subcaption file.

        Return type:
        :   None
