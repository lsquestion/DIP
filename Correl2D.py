import numpy as np

def correl2d(img,window):
    m=window.shape[0]
    n=window.shape[1]
    img1=np.zeros((img.shape[0]+m-1,img.shape[1]+n-1))
    img1[(m-1)//2:(img.shape[0]+(m-1)//2),(n-1)//2:(img.shape[1]+(n-1)//2)]=img
    img2=np.zeros(img.shape)
    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            temp=img1[i:i+m,j:j+n]
            img2[i,j]=np.sum(np.multiply(temp,window))

    return (img1,img2)
window=np.array([[1,0,0],[0,0,0],[0,0,2]])
img=np.array([[1,2,1,0,2,2],[0,1,1,2,0,1],[3,0,2,1,2,2],[0,1,1,0,0,1],[1,1,3,2,2,0],[0,0,1,0,1,0]])
img1,img2=correl2d(img,window)

print(img1)
print(img2)