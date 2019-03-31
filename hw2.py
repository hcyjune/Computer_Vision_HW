import numpy as np
from PIL import Image
import scipy.misc
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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

def his(x):
    num = np.zeros([256])
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            num[int(x[i][j])] = num[int(x[i][j])]+1
    f = open('his.txt','w')
    for k in range(len(num)):
        f.write(str(k)+' '+str(num[k])+'\n')
    f.close()

    
img_bi = Image.open('lena_bi.png')
lena_bi = np.array(img_bi)[:, :]

def con(x):
    tem = np.zeros(x.shape)
    label = 0
    corner = []
    right = []
    wrong = []
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if x[i][j]==1: # white area -> object
                if label!=0: # not first label
                    if i!=0 and j==0: # not first row but first column
                        if x[i-1][j] ==1: # connected
                            tem[i][j] = tem[i-1][j]
                        else: # isolated
                            label = label+1
                            tem[i][j] = label
                            
                    if j!=0 and i==0: # not first column but first row
                        if x[i][j-1] ==1: # connected
                            tem[i][j] = tem[i][j-1]
                        else: # isolated
                            label = label+1
                            tem[i][j] = label
                            
                    if i!=0 and j!=0: # neither first row nor first column
                        if x[i-1][j] !=1 and x[i][j-1] ==1: # only horizontally-connected
                            tem[i][j] = tem[i][j-1]
                        elif x[i-1][j] ==1 and x[i][j-1] !=1: # only vertically-connected
                            tem[i][j] = tem[i-1][j]
                        elif x[i-1][j] ==1 and x[i][j-1] ==1: # horizontally-connected and vertically-connected
                            small = min(tem[i-1][j],tem[i][j-1])
                            large = max(tem[i-1][j],tem[i][j-1])
                            tem[i][j] = small
                            if small!=large:
                                for y in range(j):
                                    if tem[i][y]==large:
                                        tem[i][y]=small
                                if  ([small,large] in corner)==False:
                                    corner.append([small,large])
                                    right.append(small)
                                    wrong.append(large)
                        
                        else: # isolated
                            label = label+1
                            tem[i][j] = label
                            
                else: # first label
                    label = label+1
                    tem[i][j] = label

    # substitute label in corner
    for k in range(len(right)):
        for m in range(len(right)):
            if wrong[k]==right[m]:
                right[m]=right[k]
                    
    # substitute label in tem
    for i in range(x.shape[0]-1,-1,-1):
        for j in range(x.shape[1]-1,-1,-1):
            if (tem[i][j]in wrong)==True:
                tem[i][j]=right[wrong.index(tem[i][j])]    

    # count pixels of each label
    value = np.zeros([label+1])
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
           value[int(tem[i][j])]=value[int(tem[i][j])]+1
           
    # only save areas with more than 500 pixels
    leftvalue = []
    for k in range(len(value)):
        if value[k]>=500 and k!=0:
            leftvalue.append(k)
            print(value[k])

    # relabel with consecutive integers   
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if (tem[i][j] in leftvalue)==True:
                tem[i][j] = leftvalue.index(tem[i][j])+1
            elif tem[i][j]!=0:
                tem[i][j] = 0
                
    # centroid & boundary
    xpos = np.zeros(len(leftvalue))
    ypos = np.zeros(len(leftvalue))
    xnum = np.zeros(len(leftvalue))
    ynum = np.zeros(len(leftvalue))
    xcen = np.zeros(len(leftvalue))
    ycen = np.zeros(len(leftvalue))
    xmax = []
    xmin = []
    ymax = []
    ymin = []
    for k in range(len(leftvalue)):
        xmax.append('n')
        xmin.append('n')
        ymax.append('n')
        ymin.append('n')
    for k in range(len(leftvalue)):
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                if tem[i][j]==k+1:
                    xpos[k] = xpos[k]+j
                    ypos[k] = ypos[k]+i
                    xnum[k] = xnum[k]+1
                    ynum[k] = ynum[k]+1
                    if xmax[k]=='n':
                        xmax[k] = j
                    elif j>xmax[k]:
                        xmax[k] = j    
                    if xmin[k]=='n':
                        xmin[k] = j
                    elif j<xmin[k]:
                        xmin[k] = j    
                    if ymax[k]=='n':
                        ymax[k] = i
                    elif i>ymax[k]:
                        ymax[k] = i    
                    if ymin[k]=='n':
                        ymin[k] = i
                    elif i<ymin[k]:
                        ymin[k] = i
    fig,ax = plt.subplots(1)
    ax.imshow(lena_bi,cmap='gray')          
    for k in range(len(leftvalue)):
        xcen[k] = xpos[k]/xnum[k]
        ycen[k] = ypos[k]/ynum[k]  
        rect = patches.Rectangle((xmin[k],ymin[k]),(xmax[k]-xmin[k]),(ymax[k]-ymin[k]),linewidth=1,edgecolor='r',facecolor='none')
        ax.add_patch(rect)
    plt.show()
    print(xcen)
    print(ycen)
    print(xmin)
    print(ymin)
    print(xmax)
    print(ymax)
    
           
ans = bi(lena)			
#im = Image.fromarray(ans)
#im.save("lena_bi.im")
#scipy.misc.imsave('lena_bi.jpg', ans)

#his(lena)

answer = con(ans)
