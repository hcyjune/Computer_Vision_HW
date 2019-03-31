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

I = 2
b = 3
def bor(x):
    tem = np.zeros(x.shape)
    for i in range(1,x.shape[0]-1):
        for j in range(1,x.shape[1]-1):
            if x[i][j]==1:
                tem[i][j]=x[i][j]
                if tem[i][j]!=x[i-1][j]:
                    tem[i][j] = b #
                if tem[i][j]!=x[i][j-1]:
                    tem[i][j] = b #
                if tem[i][j]!=x[i+1][j]:
                    tem[i][j] = b #
                if tem[i][j]!=x[i][j+1]:
                    tem[i][j] = b #
                if tem[i][j]!=b:
                    tem[i][j] = I #
    return tem

p = 4
q = 5
def pair(x):
    tem = np.zeros(x.shape)
    for i in range(1,x.shape[0]-1):
        for j in range(1,x.shape[1]-1):
            if x[i][j]==b:
                if x[i-1][j]==I or x[i][j-1]==I or x[i+1][j]==I or x[i][j+1]==I:
                    tem[i][j] = p #
                else:
                   tem[i][j] = q #
            elif x[i][j]==I: #
                tem[i][j] = q #
    return tem

def thin(x):            
    y = pair(bor(x)) #marked by pair    
    for i in range(1,x.shape[0]-1):
        for j in range(1,x.shape[1]-1):
            if x[i][j]==1:
                a=[]
                if x[i][j]==x[i][j+1]:
                    if x[i][j]!=x[i-1][j+1] or x[i][j]!=x[i-1][j]:
                        a.append(1)
                if x[i][j]==x[i-1][j]:
                    if x[i][j]!=x[i-1][j-1] or x[i][j]!=x[i][j-1]:
                        a.append(1)
                if x[i][j]==x[i][j-1]:
                    if x[i][j]!=x[i+1][j-1] or x[i][j]!=x[i+1][j]:
                        a.append(1)
                if x[i][j]==x[i+1][j]:
                    if x[i][j]!=x[i+1][j+1] or x[i][j]!=x[i][j+1]:
                        a.append(1)
                if a.count(1)==1 and y[i][j]==p:
                    x[i][j]=0                
    return x

def chk(x):
    count=0
    while(True):
        count +=1
        x1=np.copy(x)
        x2=thin(x)
        if np.array_equal(x1, x2) == True: break     

    print(count)       
    return x2

def out(x):
    f = open('thin.txt','w')
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if x[i][j]==1:
                f.write('*')
            else:
                f.write(' ')
        f.write('\n')
    f.close

    
ans = bi(lena)
answer = unit(ans)
out(chk(answer))

