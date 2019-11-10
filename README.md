# Gif Creator

This short code snippet will **create GIFs** by concatenating images using Python's Pillow library.

## Procedure
1. Add the wanted images in a (new) sub-folder inside the `img` folder found under the root directory. Make sure that 
the images have names in alphabetical order since this will determine the order during the creation of the GIF. All 
images within the same folder are included in the GIF.
2. Update the `# --> CONTROL <-- #` section in the `main.py` file under root. These are the following:
    * `file_format` The format of the input images (e.g. png, jpg, ...)
    * `gif_speed` The duration between each picture (i.e. frame-rate)
    * `image_path` The relative path to the folder in which the images are saved that are used to create the GIF
    * `name` The name of the saved GIF, which is automatically saved in the root-folder
    * `slow_end` The number of (additional) repetitions of the last image in the GIF
    * `slow_start` The number of (additional) repetitions of the first image in the GIF
3. Run `main.py`. The GIF can now be found under the root-directory.

## Q&A
* **The GIF was created successfully, however, it is not playing in my editor.**<br>
Some editors (e.g. PyCharm) don't support GIFs natively. The GIF will play when opened in the PC's file explorer.
* **I get a `IndexError: list index out of range` error at line 33.**<br>
Most likely, you've entered the path wrong. Note the `image_path` **always** should end with a `/`.
