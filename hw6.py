import numpy as np
from PIL import Image

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

def unit(x):
    tem = np.zeros([64+2,64+2])
    for i in range(64+2):# (64+2)*(64+2) array
        for j in range(64+2):
            if i==0 or j==0 or i==65 or j==65:
                tem[i][j]=0
            else:
                tem[i][j]=x[(i-1)*8][(j-1)*8]
    return tem

def yokoi(x):
    f = open('yokoi.txt','w')
    tem = np.zeros(x.shape)
    for i in range(1,x.shape[0]-1):
        for j in range(1,x.shape[1]-1):
            if x[i][j]==1:
                a = []                
                if x[i][j]==x[i][j+1]:
                    if x[i][j]==x[i-1][j+1] and x[i][j]==x[i-1][j]:
                        a.append('r')
                    else:
                        a.append('q')
                else:
                    a.append('s')
              
                if x[i][j]==x[i-1][j]:
                    if x[i][j]==x[i-1][j-1] and x[i][j]==x[i][j-1]:
                        a.append('r')
                    else:
                        a.append('q')
                else:
                    a.append('s')
            
                if x[i][j]==x[i][j-1]:
                    if x[i][j]==x[i+1][j-1] and x[i][j]==x[i+1][j]:
                        a.append('r')
                    else:
                        a.append('q')
                else:
                    a.append('s')
            
                if x[i][j]==x[i+1][j]:
                    if x[i][j]==x[i+1][j+1] and x[i][j]==x[i][j+1]:
                        a.append('r')
                    else:
                        a.append('q')
                else:
                    a.append('s')

                if a.count('r')==4:
                    tem[i][j]=5
                else:
                    tem[i][j]=a.count('q')
                
                f.write(str(int(tem[i][j])))
            else:
                f.write(' ')
        f.write('\n')
    f.close()         
    return tem
                    
    
ans = bi(lena)

answer = unit(ans)

yokoi(answer)
