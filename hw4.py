import numpy as np
from PIL import Image
import scipy.misc
img = Image.open('lena.bmp')
lena = np.array(img)[:, :] # 512*512 array

def bi(x):
    tem = np.zeros(x.shape)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if x[i][j]<128:
                tem[i][j] = 0
            else:
                tem[i][j] = 1
    return tem

def com(x):
    tem = np.zeros(x.shape)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if x[i][j]==0:
                tem[i][j]=1
    return tem

kernel = []
for k in range(-2,3,1):
    for m in range(-2,3,1):
        if (k!=-2 or m!=-2) and (k!=-2 or m!=2) and (k!=2 or m!=-2) and (k!=2 or m!=2):
            kernel.append([k,m])

def dil(x):
    tem = np.zeros(x.shape)
    for i in range(2,x.shape[0]-2,1):
        for j in range(2,x.shape[1]-2,1):
            if x[i][j]==1:
                for k in range(len(kernel)):
                    tem[i+kernel[k][0]][j+kernel[k][1]] = 1
    return tem

J = [(0,-1),(0,0),(1,0)]
K = [(-1,0),(-1,1),(0,1)]
def hit(x):
    y = com(x)
    tem_1 = np.zeros(x.shape)
    tem_2 = np.zeros(y.shape)
    tem = np.zeros(x.shape)
    for i in range(0,x.shape[0]-1,1):
        for j in range(1,x.shape[1],1):
            flag = 1
	    for k in range(len(J)):
		    if x[i+J[k][0]][j+J[k][1]] == 0:
			    flag = 0
			    break
	    if flag != 0:
		    tem_1[i][j] = 1
                    
    for i in range(1,y.shape[0],1):
        for j in range(0,y.shape[1]-1,1):                
            flag = 1
	    for k in range(len(K)):
		    if y[i+K[k][0]][j+K[k][1]] == 0:
			    flag = 0
			    break
	    if flag != 0:
		    tem_2[i][j] = 1
                    
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if tem_1[i][j]==1 and tem_2[i][j]==1:
                tem[i][j]=1
    return tem

ans = bi(lena)
scipy.misc.imsave('lena_bi.jpg', ans)

ans_dil = dil(ans)
scipy.misc.imsave('lena_dil.jpg', ans_dil)

ans_ero = com(dil(com(ans)))
scipy.misc.imsave('lena_ero.jpg', ans_ero)

ans_opn = dil(ans_ero)
scipy.misc.imsave('lena_opn.jpg', ans_opn)

ans_clo = com(dil(com(ans_dil)))
scipy.misc.imsave('lena_clo.jpg', ans_clo)

ans_hit = hit(ans)
scipy.misc.imsave('lena_hit.jpg', ans_hit)

