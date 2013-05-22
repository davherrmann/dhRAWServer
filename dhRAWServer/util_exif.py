# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:20:38 2013

@author: dherrmann
"""

import exif
import glob
import os

EXIF_TAGS_SHOWN = ("EXIF ShutterSpeedValue",
                   "EXIF ISOSpeedRatings",
                   "EXIF ExposureTime",
                   "EXIF ExposureMode",
                   "EXIF WhiteBalance",
                   "EXIF FNumber",
                   "EXIF ApertureValue",
                   "EXIF ColorSpace",
                   "EXIF LensModel",
                   "Image Model",
                   "Image DateTime")
                   
def extract_exif_from_jpg(path, tags=EXIF_TAGS_SHOWN):
    try:
        #open image in binary reading mode
        with open(path, 'rb') as image:
            tags_all = exif.process_file(image)
            tags_shown = {tag.split(" ")[-1:][0]: str(tags_all[tag]) for tag in tags}
        return tags_shown
    except IOError:
        return {}

#
def extract_exifs_from_folder(path, tags=EXIF_TAGS_SHOWN):
    exifs = {}
    for image in glob.glob(os.path.join(path, "*.JPG")):
        exifs[image] = extract_exif_from_jpg(image, tags)
        exifs[image]["path"] = os.path.basename(image)
    return exifs