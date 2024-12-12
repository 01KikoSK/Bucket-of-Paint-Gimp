#!/usr/bin/env python

from gimpfu import *

def bucket_of_paint(image, drawable, color):
    pdb.gimp_context_set_foreground(color)
    pdb.gimp_edit_bucket_fill(drawable, FG_BUCKET_FILL, NORMAL_MODE, 100, 255, FALSE, 0, 0)

register(
    "python_fu_bucket_of_paint",
    "Bucket of Paint",
    "Simulate a bucket fill tool",
    "Your Name",
    "Your Name",
    "2024",
    "<Image>/Filters/Custom/Bucket of Paint",
    "RGB*, GRAY*",
    [
        (PF_COLOR, "color", "Fill color", (255, 0, 0))
    ],
    [],
    bucket_of_paint)

main()
