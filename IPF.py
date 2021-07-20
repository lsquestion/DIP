import numpy as np

def change_alpha(im,a):
    im_changed=np.zeros(shape=im.shape,dtype='uint8')
    for i in range(im.shape[0],):
        for j in range(im.shape[1]):
            for k in range(im.shape[2]):
                if im[i,j,k]*a>255:
                    im_changed[i,j,k]=255
                elif im[i,j,k]*a<0:
                    im_changed[i,j,k]=0
                else:
                    im_changed[i,j,k]=im[i,j,k]*a
    return im_changed

def RGB2MaxGray(img):
    max_gray = np.zeros(img.shape[0:2], dtype='uint8')
    for ii in range(img.shape[0]):
        for jj in range(img.shape[1]):
            r, g, b = img[ii, jj, :]
            max_gray[ii, jj] = max(r, g, b)
    return max_gray

def RGB2AveGray(img):
    ave_gray = np.zeros(img.shape[0:2], dtype='uint8')
    for ii in range(img.shape[0]):
        for jj in range(img.shape[1]):
            r, g, b = img[ii, jj, :]
            ave_gray[ii, jj] = (r + g + b) / 3
    return  ave_gray

def RGB2WeightGray(img):
    weight_gray = np.zeros(img.shape[0:2], dtype='uint8')
    for ii in range(img.shape[0]):
        for jj in range(img.shape[1]):
            r, g, b = img[ii, jj, :]
            weight_gray[ii, jj] = 0.3 * r + 0.59 * g + 0.11 * b
    return weight_gray

def robert(img):
    img=RGB2MaxGray(img)
    m=img.shape[0]
    n=img.shape[1]
    robert_operator=[[-1,-1],[1,1]]
    for i in range(m):
        for j in range(n):
            if (j+2<=n) and(i+2<=m):
                imgChild=img[i:i+2,j:j+2]
                list_robert=robert_operator*imgChild
                img[i,j]=abs(list_robert.sum())
    return img

def robert_pos(img):
    img=RGB2MaxGray(img)
    m=img.shape[0]
    n=img.shape[1]
    robert_operator=[[-1,0],[0,1]]
    for i in range(m):
        for j in range(n):
            if (j+2<=n) and(i+2<=m):
                imgChild=img[i:i+2,j:j+2]
                list_robert=robert_operator*imgChild
                img[i,j]=abs(list_robert.sum())
    return img

def robert_neg(img):
    img=RGB2MaxGray(img)
    m=img.shape[0]
    n=img.shape[1]
    robert_operator=[[-1,-1],[1,1]]
    for i in range(m):
        for j in range(n):
            if (j+2<=n) and(i+2<=m):
                imgChild=img[i:i+2,j:j+2]
                list_robert=robert_operator*imgChild
                img[i,j]=abs(list_robert.sum())
    return img

def sobel_h(img):
    m = img.shape[0]
    n = img.shape[1]
    new_imgH=np.zeros((m,n))
    sobel_operator_h = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    for i in range(m-2):
        for j in range(n-2):
            new_imgH[i+1,j+1]=abs(np.sum(img[i:i+3,j:j+3]*sobel_operator_h))
    return np.uint8(new_imgH)

def sobel_v(img):
    m = img.shape[0]
    n = img.shape[1]
    new_imgV=np.zeros((m,n))
    sobel_operator_v = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    for i in range(m-2):
        for j in range(n-2):
            new_imgV[i+1,j+1]=abs(np.sum(img[i:i+3,j:j+3]*sobel_operator_v))
    return np.uint8(new_imgV)

def sobel(img):
    m = img.shape[0]
    n = img.shape[1]
    new_img = np.zeros((m, n))
    new_imgH= np.zeros((m, n))
    new_imgV= np.zeros((m, n))
    sobel_operator_h = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_operator_v = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    for i in range(m-2):
        for j in range(n-2):
            new_imgH[i + 1, j + 1] = abs(np.sum(img[i:i + 3, j:j + 3] * sobel_operator_h))
            new_imgV[i + 1, j + 1] = abs(np.sum(img[i:i + 3, j:j + 3] * sobel_operator_v))
            new_img[i+1,j+1]=(new_imgH[i+1,j+1]*new_imgH[i+1,j+1]+new_imgV[i+1,j+1]*new_imgV[i+1,j+1])
    return np.uint8(new_img)

def laplace(img):
    m = img.shape[0]
    n = img.shape[1]
    new_img=np.zeros((m,n))
    laplace_operator=np.array([[0,1,0],[1,-4,1],[0,1,0]])
    #laplace_operator_Exp = np.array([[1, 1, 1], [1, 8, 1], [1, 1, 1]])
    #laplace_operator_MidNeg = np.array([[0, -1, 0], [1, 4, 1], [0, -1, 0]])
    #laplace_operator_ExpMidNeg= np.array([[-1, 1, 1], [1, 8, -1], [1, 1, 1]])
    for i in range(m-2):
        for j in range(n-2):
            new_img[i+1,j+1]=abs(np.sum(img[i:i+3,j:j+3]*laplace_operator))
    return np.uint(new_img)

