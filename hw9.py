import numpy as np
from PIL import Image
import scipy.misc
from math import sqrt

img = Image.open('lena.bmp')
lena = np.array(img)[:, :] # 512*512 array

def roberts(x):
    tem=np.ones(x.shape)
    threshold = 30 #12
    mask_1=[[-1,0],[0,1]]
    mask_2=[[0,-1],[1,0]]
    for i in range(x.shape[0]-1):
        for j in range(x.shape[1]-1):
            y=x[i:i+2,j:j+2]
            gra = sqrt(np.sum(np.multiply(y,mask_1))**2+np.sum(np.multiply(y,mask_2))**2)
            if gra>threshold:
                tem[i][j]=0
    return tem

def prewitt(x):
    tem=np.ones(x.shape)
    threshold = 90 #24
    mask_1=[[-1,-1,-1],[0,0,0],[1,1,1]]
    mask_2=[[-1,0,1],[-1,0,1],[-1,0,1]]
    for i in range(1,x.shape[0]-1):
        for j in range(1,x.shape[1]-1):
            y=x[i-1:i+2,j-1:j+2]
            gra = sqrt(np.sum(np.multiply(y,mask_1))**2+np.sum(np.multiply(y,mask_2))**2)
            if gra>threshold:
                tem[i][j]=0
    return tem

def sobel(x):
    tem=np.ones(x.shape)
    threshold = 120 #38
    mask_1=[[-1,-2,-1],[0,0,0],[1,2,1]]
    mask_2=[[-1,0,1],[-2,0,2],[-1,0,1]]
    for i in range(1,x.shape[0]-1):
        for j in range(1,x.shape[1]-1):
            y=x[i-1:i+2,j-1:j+2]
            gra = sqrt(np.sum(np.multiply(y,mask_1))**2+np.sum(np.multiply(y,mask_2))**2)
            if gra>threshold:
                tem[i][j]=0
    return tem

def frei_and_chen(x):
    tem=np.ones(x.shape)
    threshold = 100 #30
    mask_1=[[-1,-sqrt(2),-1],[0,0,0],[1,sqrt(2),1]]
    mask_2=[[-1,0,1],[-sqrt(2),0,sqrt(2)],[-1,0,1]]
    for i in range(1,x.shape[0]-1):
        for j in range(1,x.shape[1]-1):
            y=x[i-1:i+2,j-1:j+2]
            gra = sqrt(np.sum(np.multiply(y,mask_1))**2+np.sum(np.multiply(y,mask_2))**2)
            if gra>threshold:
                tem[i][j]=0
    return tem

def kirsch(x):
    tem=np.ones(x.shape)
    threshold = 430 #135
    mask=[]#list
    mask.append(np.array([[-3,-3,5],[-3,0,5],[-3,-3,5]]))#k0
    mask.append(np.array([[-3,5,5],[-3,0,5],[-3,-3,-3]]))#k1
    mask.append(np.array([[5,5,5],[-3,0,-3],[-3,-3,-3]]))#k2
    mask.append(np.array([[5,5,-3],[5,0,-3],[-3,-3,-3]]))#k3
    mask.append(np.array([[5,-3,-3],[5,0,-3],[5,-3,-3]]))#k4
    mask.append(np.array([[-3,-3,-3],[5,0,-3],[5,5,-3]]))#k5
    mask.append(np.array([[-3,-3,-3],[-3,0,-3],[5,5,5]]))#k6
    mask.append(np.array([[-3,-3,-3],[-3,0,5],[-3,5,5]]))#k7
    for i in range(1,x.shape[0]-1):
        for j in range(1,x.shape[1]-1):
            gra_max=0
            for k in range(len(mask)):
                y=x[i-1:i+2,j-1:j+2]
                gra=np.sum(np.multiply(y,mask[k]))
                if gra>gra_max:
                    gra_max=gra
            if gra_max>threshold:
                tem[i][j]=0
    return tem

def robinson(x):
    tem=np.ones(x.shape)
    threshold = 120 #43
    mask=[]#list
    mask.append(np.array([[-1,0,1],[-2,0,2],[-1,0,1]]))#k0
    mask.append(np.array([[0,1,2],[-1,0,1],[-2,-1,0]]))#k1
    mask.append(np.array([[1,2,1],[0,0,0],[-1,-2,-1]]))#k2
    mask.append(np.array([[2,1,0],[1,0,-1],[0,-1,-2]]))#k3
    for k in range(len(mask)):
        mask.append(-mask[k])
    for i in range(1,x.shape[0]-1):
        for j in range(1,x.shape[1]-1):
            gra_max=0
            for k in range(len(mask)):
                y=x[i-1:i+2,j-1:j+2]
                gra = np.sum(np.multiply(y,mask[k]))
                if gra>gra_max:
                    gra_max=gra
            if gra_max>threshold:
                tem[i][j]=0
    return tem

def nevatia_babu(x):
    tem=np.ones(x.shape)
    threshold = 37000 #12500
    mask=[]#list
    mask.append(np.array([[100,100,100,100,100],[100,100,100,100,100],[0,0,0,0,0],[-100,-100,-100,-100,-100],[-100,-100,-100,-100,-100]]))#k0
    mask.append(np.array([[100,100,100,100,100],[100,100,100,78,-32],[100,92,0,-92,-100],[32,-78,-100,-100,-100],[-100,-100,-100,-100,-100]]))#k1
    mask.append(np.array([[100,100,100,32,-100],[100,100,92,-78,-100],[100,100,0,-100,-100],[100,78,-92,-100,-100],[100,-32,-100,-100,-100]]))#k2
    mask.append(np.array([[-100,-100,0,100,100],[-100,-100,0,100,100],[-100,-100,0,100,100],[-100,-100,0,100,100],[-100,-100,0,100,100]]))#k3
    mask.append(np.array([[-100,32,100,100,100],[-100,-78,92,100,100],[-100,-100,0,100,100],[-100,-100,-92,78,100],[-100,-100,-100,-32,100]]))#k4
    mask.append(np.array([[100,100,100,100,100],[-32,78,100,100,100],[-100,-92,0,92,100],[-100,-100,-100,-78,32],[-100,-100,-100,-100,-100]]))#k5
    for k in range(len(mask)):
        mask.append(-mask[k])
    for i in range(2,x.shape[0]-2):
        for j in range(2,x.shape[1]-2):
            gra_max=0
            for k in range(len(mask)):
                y=x[i-2:i+3,j-2:j+3]
                gra = np.sum(np.multiply(y,mask[k]))
                if gra>gra_max:
                    gra_max=gra
            if gra_max>threshold:
                tem[i][j]=0
    return tem

#ans_roberts = roberts(lena)
#scipy.misc.imsave('lena_roberts.jpg', ans_roberts)
#ans_prewitt = prewitt(lena)
#scipy.misc.imsave('lena_prewitt.jpg', ans_prewitt)
#ans_sobel = sobel(lena)
#scipy.misc.imsave('lena_sobel.jpg', ans_sobel)
#ans_frei_and_chen = frei_and_chen(lena)
#scipy.misc.imsave('lena_frei_and_chen.jpg', ans_frei_and_chen)
#ans_kirsch = kirsch(lena)
#scipy.misc.imsave('lena_kirsch.jpg', ans_kirsch)
#ans_robinson = robinson(lena)
#scipy.misc.imsave('lena_robinson.jpg', ans_robinson)
ans_nevatia_babu = nevatia_babu(lena)
scipy.misc.imsave('lena_nevatia_babu.jpg', ans_nevatia_babu)
