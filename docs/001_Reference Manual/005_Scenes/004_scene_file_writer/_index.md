---
{
  "title": "scene_file_writer",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.html",
  "tree_path": [
    "Reference Manual",
    "Scenes",
    "scene_file_writer"
  ],
  "scraped_at": "2026-07-10T16:00:52"
}
---

# scene\_file\_writer

The interface between scenes and ffmpeg.

Classes

| Name | Description |
| --- | --- |
| [`SceneFileWriter`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html) | SceneFileWriter is the object that actually writes the animations played, into video files, using FFMPEG. |

Functions

convert\_audio(*input\_path*, *output\_path*, *codec\_name*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
:   Parameters:
    :   - **input\_path** (*Path*)
        - **output\_path** (*Path* *|* *\_TemporaryFileWrapper**[**bytes**]*)
        - **codec\_name** (*str*)

    Return type:
    :   None

to\_av\_frame\_rate(*fps*)[[source]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html)
:   Parameters:
    :   **fps** (*float*)

    Return type:
    :   *Fraction*
