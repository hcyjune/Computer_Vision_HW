import numpy as np
from PIL import Image
import scipy.misc
img = Image.open('lena.bmp')
lena = np.array(img)[:, :] # 512*512 array

def bdry(x):
    tem_blk = np.zeros([516,516])
    tem_wht = np.full([516,516],255)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            tem_blk[i+2][j+2] = x[i][j]
            tem_wht[i+2][j+2] = x[i][j]
    return tem_blk, tem_wht


kernel = []
for k in range(-2,3,1):
    for m in range(-2,3,1):
        if (k!=-2 or m!=-2) and (k!=-2 or m!=2) and (k!=2 or m!=-2) and (k!=2 or m!=2):
            kernel.append([k,m])

def dil(x):
    tem = np.zeros([512,512])
    for i in range(2,x.shape[0]-2,1):
        for j in range(2,x.shape[1]-2,1):
            maxi = 0
            for k in range(len(kernel)):
                if x[i+kernel[k][0]][j+kernel[k][1]]> maxi:                        
                    maxi = x[i+kernel[k][0]][j+kernel[k][1]]
            tem[i-2][j-2] = maxi
    print(tem.shape)
    return tem

def ero(x):
    tem = np.zeros([512,512])
    for i in range(2,x.shape[0]-2,1):
        for j in range(2,x.shape[1]-2,1):
            mini = 255
            for k in range(len(kernel)):
                if x[i+kernel[k][0]][j+kernel[k][1]]< mini:                        
                    mini = x[i+kernel[k][0]][j+kernel[k][1]]
            tem[i-2][j-2] = mini
    return tem

ans_blk, ans_wht = bdry(lena)

ans_dil = dil(ans_blk)
scipy.misc.imsave('lena_grey_dil.jpg', ans_dil)

ans_ero = ero(ans_wht)
scipy.misc.imsave('lena_grey_ero.jpg', ans_ero)

ans_blk, ans_wht = bdry(ans_ero)
ans_opn = dil(ans_blk)
scipy.misc.imsave('lena_grey_opn.jpg', ans_opn)

ans_blk, ans_wht = bdry(ans_dil)
ans_clo = ero(ans_wht)
scipy.misc.imsave('lena_grey_clo.jpg', ans_clo)


