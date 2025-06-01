#!/usr/bin/env python3

"""
Wrapper for video systems

It does not fit the iterator framework.
"""

from pathlib import Path
from PIL import Image
import numpy as np
import cv2

_supported_extensions = [".txt", ".lst"]

def is_supported(filename:str):
    """
    Check whether the file type is supported.

    Args:
        filename: The path to the file.

    Returns:
        True if the file type is supported, False otherwise.
    """
    return Path(filename).suffix.lower() in _supported_extensions

class VideoLoader(object):
    def __init__(self, filename):
        with open(filename, "r") as f:
            fl = f.readlines()
            self.file_list = [Path(filename).parent / i.rstrip() for i in fl]
        self.nframe = 0

    def next(self):
        if self.nframe >= len(self.file_list):
            return 0, None
        img = Image.open(self.file_list[self.nframe])
        frame = np.asarray(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        self.nframe += 1
        return self.nframe, frame

    def skip(self):
        if self.nframe >= len(self.file_list):
            return 0
        self.nframe += 1
        return self.nframe

if __name__ == "__main__":
    vl = VideoLoader("../examples/sample3_images.txt")

    while True:
        nframe, frame = vl.next()
        if nframe == 0:
            break
        print(frame.shape, nframe)
