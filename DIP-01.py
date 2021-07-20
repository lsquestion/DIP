# This is a sample Python script.
from skimage import data,io,exposure,color
from matplotlib import pyplot as plt
import numpy as np
from change_alpha import  change_alpha
array=np.array([2,3,4,5,6])
file_name='Sekuai.jpg'
image=io.imread(fname=file_name)
"""
image_change=change_alpha(image,1.5)
image_r=image[:,:,0]
image_g=image[:,:,1]
image_b=image[:,:,2]
plt.subplot(2,2,1)
plt.imshow(image_r)
plt.subplot(2,2,2)
plt.imshow(image_g)
plt.subplot(2,2,3)
plt.imshow(image_b)
"""
"""
image_1=exposure.adjust_gamma(image,0.2)
image_2=exposure.adjust_gamma(image,0.67)
image_3=exposure.adjust_gamma(image,25)

plt.subplot(2,3,1)
plt.title('gamma=1')
io.imshow(image)

plt.subplot(2,3,2)
plt.title('gamma=0.2')
io.imshow(image_1)

plt.subplot(2,3,3)
plt.title('gamma=0.67')
io.imshow(image_1)

plt.subplot(2,3,4)
plt.title('gamma=25')
io.imshow(image_3)

"""
"""
plt.subplot(2,2,1)
plt.title("image")
io.imshow(image)

plt.subplot(2,2,2)
plt.title("hist_r")
img_r=image[:,:,0]
plt.hist(img_r,bins=30)

print(hist_b)
"""
"""
imag_gray=color.rgb2gray(image)
plt.subplot(2,1,1)
#plt.axis('off')
plt.imshow(imag_gray,cmap='gray')
rows,cols=imag_gray.shape
labels=np.zeros([rows,cols])
for i in range(rows):
    for j in range(cols):
        if(imag_gray[i,j]<0.4):
            labels[i,j]=0
        elif(imag_gray[i,j]<0.8):
            labels[i,j]=1
        else:
            labels[i,j]=2
psdimag=color.label2rgb(labels)
#plt.figure()
plt.axis('off')
plt.subplot(2,1,2)
plt.imshow(psdimag)
"""



plt.show()