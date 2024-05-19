#!/usr/bin/env python3

##
#@file tiffmerger.@property
#@brief Merges two tiff images into one high contrast tiff image
#@author Gabriel Estima Correia Milanesi Castanheira de Souza
#
#@date 19/05/2024

from PIL import Image
import sys
import numpy as np

main = np.array(Image.open(sys.argv[1])).astype('int32')
back = np.array(Image.open(sys.argv[2])).astype('int32')

diff = np.clip((np.log(main+1) + 5000*np.log(back+1)), 0, 256)
diff = np.clip(256 - diff, 0, 256)

resname = sys.argv[3]
waterBlack = Image.fromarray(diff.astype(np.uint8)).convert("L")


imageRed = Image.open(sys.argv[1]).convert("L")
imageGreen = Image.open(sys.argv[2]).convert("L")
resultImg = Image.merge("RGB", (imageGreen, imageRed, waterBlack))
resultImg.save(resname)



