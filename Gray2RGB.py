from matplotlib import pyplot as plt
from skimage import data,io,exposure,color
import numpy as np
L=255
def GetR(gry):
    if gry<L/2:
        return 0
    elif gry>L/4*3:
        return L
    else:
        return 4*gry-2*L

def GetG(gry):
    if gry<L/4:
        return 4*gry
    elif gry>L/4*3:
        return 4*L-4*gry
    else:
        return L

def GetB(gry):
    if gry < L / 4:
        return L
    elif gry > L/2:
        return 0
    else:
        return 2*L-4*gry
"""
x=[0,64,127,191,255]
plt.subplot(2,2,1)
R=[]
for i in x:
    R.append(GetR(i))
plt.plot(x,R,'r--',label='红色变换')

plt.subplot(2,2,2)
G=[]
for i in x:
    G.append(GetG(i))
plt.plot(x,G,'g--',label='绿色变换')

plt.subplot(2,2,3)
B=[]
for i in x:
    B.append(GetB(i))
plt.plot(x,B,'b--',label='黄色变换')
"""

file_name='Sekuai.jpg'
image=io.imread(fname=file_name)
grayimg=color.rgb2gray(image)*255
colorimag=np.zeros(image.shape,dtype='uint8')

for ii in range(image.shape[0]):
    for jj in range(image.shape[1]):
        r,g,b=GetR(grayimg[ii,jj]),GetG(grayimg[ii,jj]),GetB(grayimg[ii,jj])
        colorimag[ii,jj,:]=(r,g,b)

plt.subplot(2,1,1)
plt.imshow(grayimg)

plt.subplot(2,1,2)
plt.imshow(colorimag)

plt.show()