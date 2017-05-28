#!/usr/bin/env python

from gimpfu import *

def vr_blur(image, layer):
    upper = layer.copy()
    lower = layer.copy()
    image.add_layer(upper)
    image.add_layer(lower)
    upper.resize(layer.width, 1, 0, 0)
    lower.resize(layer.width, 1, 0, -layer.height+1)
    overlap = 42
    gap = (image.height - layer.height) / 2
    pdb.gimp_layer_scale(upper, layer.width, gap + overlap, 1)
    pdb.gimp_layer_scale(lower, layer.width, gap + overlap, 1)
    image.raise_layer(layer)
    image.raise_layer(layer)
    upper.translate(0, (upper.height - overlap) / -2)
    lower.translate(0, (lower.height - overlap) / 2)
    pdb.plug_in_gauss_rle(image, upper, 8, 1, 0)
    pdb.plug_in_gauss_rle(image, lower, 8, 1, 0)

register(
    "python_fu_vr_blur",
    "VR Blur",
    "Blurs top and bottom gaps",
    "Alexander Pavlenko",
    "MIT",
    "2017",
    "<Image>/Filters/Blur/VR",
    "*",
    [],
    [],
    vr_blur)

main()
