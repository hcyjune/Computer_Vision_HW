import numpy as np
from PIL import Image
import scipy.misc

img = Image.open('lena.bmp')
lena = np.array(img)[:, :] # 512*512 array

def low(x):
    tem = np.zeros(x.shape)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            tem[i][j] = x[i][j]/3.0
    return tem

def high(x):
    tem = np.zeros(x.shape)
    s_k=[]
    n_j=np.zeros([255+1])
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            n_j[int(x[i][j])]=n_j[int(x[i][j])]+1
    
    for k in range(255+1):
        sigma_k=0
        for m in range(k+1):
            sigma_k = sigma_k+n_j[m]
        s_k.append(255.0/(512.0*512.0)*sigma_k)    
    
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):     
                tem[i][j]=s_k[int(x[i][j])]
    return tem

def his(x):
    num = np.zeros([256])
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            num[int(x[i][j])] = num[int(x[i][j])]+1
    f = open('his_high.txt','w')
    for k in range(len(num)):
        f.write(str(k)+' '+str(num[k])+'\n')
    f.close()


ans = low(lena)			
#im = Image.fromarray(ans)
#im.save("lena_low.im")
scipy.misc.imsave('lena_low.png', ans)

#his(ans)

answer = high(ans)
#im = Image.fromarray(answer)
#im.save("lena_high.im")
scipy.misc.imsave('lena_high.png', answer)

his(answer)
