# This is a sample Python script.
import skimage.feature
from skimage import data,io,exposure,color
from matplotlib import pyplot as plt
import numpy as np

image_color=io.imread('Sekuai.jpg')




for ii in range(image_color.shape[0]):
    for jj in range(image_color.shape[1]):
        r,g,b=image_color[ii,jj,:]
        max_gray[ii,jj]=max(r,g,b)
        ave_gray[ii,jj]=(r+g+b)/3
        weight_gray[ii,jj]=0.3*r+0.59*g+0.11*b

plt.figure()
plt.axis('off')
plt.imshow(image_color)

plt.figure()
plt.axis('off')
plt.imshow(max_gray,cmap='gray')

plt.figure()
plt.axis('off')
plt.imshow(ave_gray,cmap='gray')

plt.figure()
plt.axis('off')
plt.imshow(weight_gray,cmap='gray')

plt.show()
