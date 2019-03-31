import numpy as np
from PIL import Image
import scipy.misc

img = Image.open('lena.bmp')
lena = np.array(img)[:, :] # 512*512 array

def up_down(x):
    tem = np.zeros(x.shape) # array full of zeros
    for i in range(x.shape[0]): # shape[0]: row
        for j in range(x.shape[1]): # shape[1]: column
            tem[i][j] = x[x.shape[0]-i-1][j]
    return tem
            
def right_left(x):
    tem = np.zeros(x.shape)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            tem[i][j] = x[i][x.shape[0]-j-1]
    return tem

def diag(x):
    tem = np.zeros(x.shape)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            tem[i][j] = x[j][i]
    return tem

def resize(x):
    width = int(x.size[1]*0.5)
    height = int(x.size[0]*0.5)
    nim = x.resize((width,height),Image.BILINEAR)
    return nim

def rotate(x):
    nim = x.rotate(-45) # counterclockwise
    return nim

def bi(x):
    tem = np.zeros(x.shape)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if x[i][j]<128: # threshold 128
                tem[i][j] = 0
            else:
                tem[i][j] = 1
    return tem


ans = up_down(lena)			
#im = Image.fromarray(ans)
#im.save("lena_up_down.im")
scipy.misc.imsave('lena_up_down.png', ans)

ans = right_left(lena)			
#im = Image.fromarray(ans)
#im.save("lena_right_left.im")
scipy.misc.imsave('lena_right_left.png', ans)

ans = diag(lena)			
#im = Image.fromarray(ans)
#im.save("lena_diag.im")
scipy.misc.imsave('lena_diag.png', ans)

im = resize(img)
#im.save("lena_resize.im")
im.save("lena_resize.png")

im = rotate(img)
#im.save("lena_rotate.im")
im.save("lena_rotate.png")

ans = bi(lena)			
#im = Image.fromarray(ans)
#im.save("lena_bi.im")
scipy.misc.imsave('lena_bi.png', ans)
