import imageio
from matplotlib import pyplot as plt
from skimage import data
import numpy as np
import math

image_color=imageio.imread('Sekuai.jpg')


r=image_color[:,:,0]
g=image_color[:,:,1]
b=image_color[:,:,2]

r1=r[128:255,85:196]
r1_u=np.mean(r1)
r1_d=0.0
for i in range(r1.shape[0]):
    for j in range(r1.shape[1]):
        r1_d=r1_d+(r1[i,j]-r1_u)*(r1[i,j]-r1_u)

r1_d=math.sqrt(r1_d/r1.shape[0]/r1.shape[1])
r2=np.zeros(r.shape,dtype='uint8')
for i in range(r1.shape[0]):
    for j in range(r1.shape[1]):
        if r[i,j]>=(r1_u-1.25*r1_d) and r[i,j]<=(r1_u+1.25*r1_d):
            r2[i,j]=1

image2=np.zeros(image_color.shape,dtype='uint8')

for i in range(r.shape[0]):
    for j in range(r.shape[1]):
        if r2[i,j]==1:
            image2[i,j,:]=image_color[i,j,:]


plt.figure(num=1)
plt.axis('off')
plt.imshow(image_color)

plt.figure(num=2)
plt.axis('off')
plt.imshow(r,cmap='gray')

plt.figure()
plt.axis('off')
plt.imshow(g,cmap='gray')

plt.figure()
plt.axis('off')
plt.imshow(b,cmap='gray')

plt.figure()
plt.axis('off')
plt.imshow(b,cmap='gray')

plt.figure()
plt.axis('off')
plt.imshow(r2,cmap='gray')

plt.figure()
plt.axis('off')
plt.imshow(image2)

plt.show()