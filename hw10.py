import numpy as np
from PIL import Image
import scipy.misc
from math import sqrt
import math

img = Image.open('lena.bmp')
lena = np.array(img)[:, :] # 512*512 array

def laplacian(x):
    tem_1=np.ones(x.shape)
    tem_2=np.ones(x.shape)
    threshold = 15 #15
    mask_1=np.array([[0,1,0],[1,-4,1],[0,1,0]])
    mask_2=np.array([[1,1,1],[1,-8,1],[1,1,1]])/3.0
    for i in range(1,x.shape[0]-1):
        for j in range(1,x.shape[1]-1):
            y=x[i-1:i+2,j-1:j+2]
            gra_1 = np.sum(np.multiply(y,mask_1))
            gra_2 = np.sum(np.multiply(y,mask_2))
            if gra_1>threshold:
                tem_1[i][j]=0
            if gra_2>threshold:
                tem_2[i][j]=0
    return tem_1,tem_2   

def min_var_laplacian(x):
    tem=np.ones(x.shape)
    threshold = 20 #20
    mask=np.array([[2,-1,2],[-1,-4,-1],[2,-1,2]])/3.0
    for i in range(1,x.shape[0]-1):
        for j in range(1,x.shape[1]-1):
            y=x[i-1:i+2,j-1:j+2]
            gra = np.sum(np.multiply(y,mask))
            if gra>threshold:
                tem[i][j]=0
    return tem

def laplacian_guassian(x):
    tem=np.ones(x.shape)
    threshold = 3000 #3000
    mask=[[0,0,0,-1,-1,-2,-1,-1,0,0,0],
          [0,0,-2,-4,-8,-9,-8,-4,-2,0,0],
          [0,-2,-7,-15,-22,-23,-22,-15,-7,-2,0],
          [-1,-4,-15,-24,-14,-1,-14,-24,-15,-4,-1],
          [-1,-8,-22,-14,52,103,52,-14,-22,-8,-1],
          [-2,-9,-23,-1,103,178,103,-1,-23,-9,-2],
          [-1,-8,-22,-14,52,103,52,-14,-22,-8,-1],
          [-1,-4,-15,-24,-14,-1,-14,-24,-15,-4,-1],
          [0,-2,-7,-15,-22,-23,-22,-15,-7,-2,0],
          [0,0,-2,-4,-8,-9,-8,-4,-2,0,0],
          [0,0,0,-1,-1,-2,-1,-1,0,0,0]]
    for i in range(5,x.shape[0]-5):
        for j in range(5,x.shape[1]-5):
            y=x[i-5:i+6,j-5:j+6]
            gra = np.sum(np.multiply(y,mask))
            if gra>threshold:
                tem[i][j]=0
    return tem

def diff_guassian(x):
    tem=np.ones(x.shape)
    threshold = 5000 #1
    #mask = np.zeros([11,11])
    mask=[[-1,-3,-4,-6,-7,-8,-7,-6,-4,-3,-1],
          [-3,-5,-8,-11,-13,-13,-13,-11,-8,-5,-3],
          [-4,-8,-12,-16,-17,-17,-17,-16,-12,-8,-4],
          [-6,-11,-16,-16,0,15,0,-16,-16,-11,-6],
          [-7,-13,-17,0,85,160,85,0,-17,-13,-7],
          [-8,-13,-17,15,160,283,160,15,-17,-13,-8],
          [-7,-13,-17,0,85,160,85,0,-17,-13,-7],
          [-6,-11,-16,-16,0,15,0,-16,-16,-11,-6],
          [-4,-8,-12,-16,-17,-17,-17,-16,-12,-8,-4],
          [-3,-5,-8,-11,-13,-13,-13,-11,-8,-5,-3],
          [-1,-3,-4,-6,-7,-8,-7,-6,-4,-3,-1]]
    """
    sigma_1=1.0
    sigma_2=3.0
    for i in range(11):
        for j in range(11):
            value_1=math.exp(-((i-5)**2+(j-5)**2)/(2*sigma_1**2))/(2*math.pi*sigma_1**2)
            value_2=math.exp(-((i-5)**2+(j-5)**2)/(2*sigma_2**2))/(2*math.pi*sigma_2**2)
            value=value_1-value_2
            mask[i][j]=value
    """
    for i in range(5,x.shape[0]-5):
        for j in range(5,x.shape[1]-5):
            y=x[i-5:i+6,j-5:j+6]
            gra = np.sum(np.multiply(y,mask))
            if gra>threshold:
                tem[i][j]=0
                #print(gra)
    return tem

#ans_laplacian_1,ans_laplacian_2 = laplacian(lena)
#scipy.misc.imsave('lena_laplacian_1.jpg', ans_laplacian_1)
#scipy.misc.imsave('lena_laplacian_2.jpg', ans_laplacian_2)
#ans_min_var_laplacian = min_var_laplacian(lena)
#scipy.misc.imsave('lena_min_var_laplacian.jpg', ans_min_var_laplacian)
#ans_laplacian_guassian = laplacian_guassian(lena)
#scipy.misc.imsave('lena_laplacian_guassian.jpg', ans_laplacian_guassian)
ans_diff_guassian = diff_guassian(lena)
scipy.misc.imsave('lena_diff_guassian.jpg', ans_diff_guassian)

