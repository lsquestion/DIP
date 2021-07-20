# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import imageio
import IPF

from matplotlib import pyplot as plt
from skimage import data
import numpy as np
import math

#image_S=imageio.imread('Sekuai.jpg')
image_C=imageio.imread('Cup.jpeg')

#out_s_robert=IPF.robert(image_S)
#out_c_robert=IPF.robert_neg(image_C)
out_c_sobel=IPF.laplace(image_C)

#out_c_gray=IPF.RGB2MaxGray(image_C)

#plt.imshow(out_s_robert)
#plt.imshow(out_c_gray,cmap='gray')
plt.imshow(out_c_sobel,cmap='gray')

plt.show()


