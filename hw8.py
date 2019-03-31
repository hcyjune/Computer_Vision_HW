import numpy as np
from PIL import Image
import scipy.misc

img = Image.open('lena.bmp')
lena = np.array(img)[:, :] # 512*512 array

def gua(x):
    tem_1=np.zeros(x.shape)
    tem_2=np.zeros(x.shape)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            tem_1[i][j]=x[i][j]+10*np.random.normal(0,1)
            tem_2[i][j]=x[i][j]+30*np.random.normal(0,1)
    return tem_1,tem_2

def salt(x):
    tem_1=np.copy(x)
    tem_2=np.copy(x)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if np.random.uniform(0,1)<0.05:
                tem_1[i][j]=0
            elif np.random.uniform(0,1)>(1-0.05):
                tem_1[i][j]=255            
            if np.random.uniform(0,1)<0.1:
                tem_2[i][j]=0
            elif np.random.uniform(0,1)>(1-0.1):
                tem_2[i][j]=255
    return tem_1,tem_2

def box(x1,x2,x3,x4):
    tem_1,temp_1=np.copy(x1),np.copy(x1)
    tem_2,temp_2=np.copy(x2),np.copy(x2)
    tem_3,temp_3=np.copy(x3),np.copy(x3)
    tem_4,temp_4=np.copy(x4),np.copy(x4)
    for i in range(1,x1.shape[0]-1):
        for j in range(1,x1.shape[1]-1):
            sum_1,sum_2,sum_3,sum_4=0,0,0,0
            for k in range(i-1,i+2):
                for m in range(j-1,j+2):
                    sum_1+=x1[k][m]
                    sum_2+=x2[k][m]
                    sum_3+=x3[k][m]
                    sum_4+=x4[k][m]
            tem_1[i][j]=sum_1/9
            tem_2[i][j]=sum_2/9
            tem_3[i][j]=sum_3/9
            tem_4[i][j]=sum_4/9
    for i in range(2,x1.shape[0]-2):
        for j in range(2,x1.shape[1]-2):
            sum_1,sum_2,sum_3,sum_4=0,0,0,0
            for k in range(i-2,i+3):
                for m in range(j-2,j+3):
                    sum_1+=x1[k][m]
                    sum_2+=x2[k][m]
                    sum_3+=x3[k][m]
                    sum_4+=x4[k][m]
            temp_1[i][j]=sum_1/25
            temp_2[i][j]=sum_2/25
            temp_3[i][j]=sum_3/25
            temp_4[i][j]=sum_4/25
    return tem_1,tem_2,tem_3,tem_4,temp_1,temp_2,temp_3,temp_4

def med(x1,x2,x3,x4):
    tem_1,temp_1=np.copy(x1),np.copy(x1)
    tem_2,temp_2=np.copy(x2),np.copy(x2)
    tem_3,temp_3=np.copy(x3),np.copy(x3)
    tem_4,temp_4=np.copy(x4),np.copy(x4)
    for i in range(1,x1.shape[0]-1):
        for j in range(1,x1.shape[1]-1):
            list_1,list_2,list_3,list_4=[],[],[],[]
            for k in range(i-1,i+2):
                for m in range(j-1,j+2):
                    list_1.append(x1[k][m])
                    list_2.append(x2[k][m])
                    list_3.append(x3[k][m])
                    list_4.append(x4[k][m])
            list_1.sort()
            list_2.sort()
            list_3.sort()
            list_4.sort()
            tem_1[i][j]=list_1[4]
            tem_2[i][j]=list_2[4]
            tem_3[i][j]=list_3[4]
            tem_4[i][j]=list_4[4]
    for i in range(2,x1.shape[0]-2):
        for j in range(2,x1.shape[1]-2):
            list_1,list_2,list_3,list_4=[],[],[],[]
            for k in range(i-2,i+3):
                for m in range(j-2,j+3):
                    list_1.append(x1[k][m])
                    list_2.append(x2[k][m])
                    list_3.append(x3[k][m])
                    list_4.append(x4[k][m])
            list_1.sort()
            list_2.sort()
            list_3.sort()
            list_4.sort()
            temp_1[i][j]=list_1[12]
            temp_2[i][j]=list_2[12]
            temp_3[i][j]=list_3[12]
            temp_4[i][j]=list_4[12]
    return tem_1,tem_2,tem_3,tem_4,temp_1,temp_2,temp_3,temp_4


kernel = []
for k in range(-2,3):
    for m in range(-2,3):
        if (k!=-2 or m!=-2) and (k!=-2 or m!=2) and (k!=2 or m!=-2) and (k!=2 or m!=2):
            kernel.append([k,m])

def dil(x):
    tem = np.copy(x)
    for i in range(2,x.shape[0]-2):
        for j in range(2,x.shape[1]-2):
            maxi = 0
            for k in range(len(kernel)):
                if x[i+kernel[k][0]][j+kernel[k][1]]> maxi:                        
                    maxi = x[i+kernel[k][0]][j+kernel[k][1]]                
            tem[i][j] = maxi            
    return tem

def ero(x):
    tem = np.copy(x)   
    for i in range(2,x.shape[0]-2):
        for j in range(2,x.shape[1]-2):
            mini = 255
            for k in range(len(kernel)):
                if x[i+kernel[k][0]][j+kernel[k][1]]< mini:                        
                    mini = x[i+kernel[k][0]][j+kernel[k][1]]                
            tem[i][j] = mini            
    return tem

def opn(x):
    tem = np.copy(dil(ero(x)))    
    return tem

def clo(x):
    tem = np.copy(ero(dil(x)))
    return tem

def co(x1,x2,x3,x4):
    tem_1 = np.copy(opn(clo(x1)))
    tem_2 = np.copy(opn(clo(x2)))
    tem_3 = np.copy(opn(clo(x3)))
    tem_4 = np.copy(opn(clo(x4)))
    return tem_1,tem_2,tem_3,tem_4

def oc(x1,x2,x3,x4):
    tem_1 = np.copy(clo(opn(x1)))
    tem_2 = np.copy(clo(opn(x2)))
    tem_3 = np.copy(clo(opn(x3)))
    tem_4 = np.copy(clo(opn(x4)))
    return tem_1,tem_2,tem_3,tem_4

ans_gua_1, ans_gua_2 = gua(lena)
#scipy.misc.imsave('lena_gua_10.jpg', ans_gua_1)
#scipy.misc.imsave('lena_gua_30.jpg', ans_gua_2)

ans_salt_1, ans_salt_2 = salt(lena)
#scipy.misc.imsave('lena_salt_05.jpg', ans_salt_1)
#scipy.misc.imsave('lena_salt_10.jpg', ans_salt_2)

#ans_box_1, ans_box_2, ans_box_3, ans_box_4, ans_box_5, ans_box_6, ans_box_7, ans_box_8 = box(ans_gua_1, ans_gua_2, ans_salt_1, ans_salt_2)
#scipy.misc.imsave('lena_gua_10_box3.jpg', ans_box_1)
#scipy.misc.imsave('lena_gua_30_box3.jpg', ans_box_2)
#scipy.misc.imsave('lena_salt_05_box3.jpg', ans_box_3)
#scipy.misc.imsave('lena_salt_10_box3.jpg', ans_box_4)
#scipy.misc.imsave('lena_gua_10_box5.jpg', ans_box_5)
#scipy.misc.imsave('lena_gua_30_box5.jpg', ans_box_6)
#scipy.misc.imsave('lena_salt_05_box5.jpg', ans_box_7)
#scipy.misc.imsave('lena_salt_10_box5.jpg', ans_box_8)

#ans_med_1, ans_med_2, ans_med_3, ans_med_4, ans_med_5, ans_med_6, ans_med_7, ans_med_8 = med(ans_gua_1, ans_gua_2, ans_salt_1, ans_salt_2)
#scipy.misc.imsave('lena_gua_10_med3.jpg', ans_med_1)
#scipy.misc.imsave('lena_gua_30_med3.jpg', ans_med_2)
#scipy.misc.imsave('lena_salt_05_med3.jpg', ans_med_3)
#scipy.misc.imsave('lena_salt_10_med3.jpg', ans_med_4)
#scipy.misc.imsave('lena_gua_10_med5.jpg', ans_med_5)
#scipy.misc.imsave('lena_gua_30_med5.jpg', ans_med_6)
#scipy.misc.imsave('lena_salt_05_med5.jpg', ans_med_7)
#scipy.misc.imsave('lena_salt_10_med5.jpg', ans_med_8)

ans_co_1, ans_co_2, ans_co_3, ans_co_4 = co(ans_gua_1, ans_gua_2, ans_salt_1, ans_salt_2)
#ans_oc_1, ans_oc_2, ans_oc_3, ans_oc_4 = oc(ans_gua_1, ans_gua_2, ans_salt_1, ans_salt_2)
scipy.misc.imsave('lena_gua_10_co.jpg', ans_co_1)
scipy.misc.imsave('lena_gua_30_co.jpg', ans_co_2)
scipy.misc.imsave('lena_salt_05_co.jpg', ans_co_3)
scipy.misc.imsave('lena_salt_10_co.jpg', ans_co_4)
#scipy.misc.imsave('lena_gua_10_oc.jpg', ans_oc_1)
#scipy.misc.imsave('lena_gua_30_oc.jpg', ans_oc_2)
#scipy.misc.imsave('lena_salt_05_oc.jpg', ans_oc_3)
#scipy.misc.imsave('lena_salt_10_oc.jpg', ans_oc_4)
