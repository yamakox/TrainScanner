#!/usr/bin/env python3

"""
Wrapper for video systems

It does not fit the iterator framework.
"""

from pathlib import Path
import numpy as np
import cv2
from logging import getLogger

logger = getLogger()
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
        self.nframe = 0
        self.file_list = []
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
                self.file_list = [Path(filename).parent / i.rstrip() for i in lines]
        except Exception as e:
            logger.error(f"Error loading the image catalog file: {filename}: {e}")

    def next(self):
        if self.nframe >= len(self.file_list):
            return 0, None
        try:
            frame = cv2.imread(str(self.file_list[self.nframe]))
            self.nframe += 1
            return self.nframe, frame
        except Exception as e:
            logger.error(f"Error loading the image file: {self.file_list[self.nframe]}: {e}")
            return 0, None

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
