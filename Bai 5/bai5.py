import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def colorFader(c1,c2,mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return (1-mix)*c1 + mix*c2

def chessboard():
    M = np.zeros((8, 8))
    for i in np.arange(0, 8):
        for j in np.arange(0, 8):
            M[i, j] = (i + j) % 2
    return M

#ban co
M = chessboard()
plt.subplots(figsize=(6, 6))
plt.imshow(M, cmap='binary')


l = 100
#theo chieu ngang
m = l*6
M2=np.zeros((m, m, 3))
for x in range(m):
    for y in range(m):
        if y < l :
            c1='red' 
            c2='orange' 
            M2[x][y] = colorFader(c1,c2,y/l)
        if (l) <= y < (2*l):
            c1='orange' 
            c2='yellow' 
            M2[x][y] = colorFader(c1,c2,(y-l)/l)
        if (2*l) <= y < (3*l):
            c1='yellow' 
            c2='green' 
            M2[x][y] = colorFader(c1,c2,(y-2*l)/l)
        if (3*l) <= y < (4*l):
            c1='green' 
            c2='blue' 
            M2[x][y] = colorFader(c1,c2,(y-3*l)/l)
        if (4*l) <= y < (5*l):
            c1='blue' 
            c2='indigo' 
            M2[x][y] = colorFader(c1,c2,(y-4*l)/l)
        if  (5*l) <= y < (6*l):
            c1='indigo' 
            c2='violet' 
            M2[x][y] = colorFader(c1,c2,(y-5*l)/l)
plt.subplots(figsize=(6, 6))
plt.imshow(M2)

#theo chieu doc
m = l*6
M3=np.zeros((m, m, 3))
for x in range(m):
    for y in range(m):
        if x < l :
            c1='red' 
            c2='orange' 
            M3[x][y] = colorFader(c1,c2,x/l)
        if (l) <= x < (2*l):
            c1='orange' 
            c2='yellow' 
            M3[x][y] = colorFader(c1,c2,(x-l)/l)
        if (2*l) <= x < (3*l):
            c1='yellow' 
            c2='green' 
            M3[x][y] = colorFader(c1,c2,(x-2*l)/l)
        if (3*l) <= x < (4*l):
            c1='green' 
            c2='blue' 
            M3[x][y] = colorFader(c1,c2,(x-3*l)/l)
        if (4*l) <= x < (5*l):
            c1='blue' 
            c2='indigo' 
            M3[x][y] = colorFader(c1,c2,(x-4*l)/l)
        if  (5*l) <= x < (6*l):
            c1='indigo' 
            c2='violet' 
            M3[x][y] = colorFader(c1,c2,(x-5*l)/l)
plt.subplots(figsize=(6, 6))
plt.imshow(M3)

#theo duong cheo
m = l*3
M4 = np.zeros((m, m, 3))
for x in range(m):
    for y in range(x+1):
        if x < l :
            c1='red'
            c2='orange'
            M4[x-y][y] = colorFader(c1,c2,x/l)
        if (l) <= x < (2*l):
            c1='orange'
            c2='yellow'
            M4[x-y][y] = colorFader(c1,c2,(x-l)/l)
        if (2*l) <= x < (3*l):
            c1='yellow' 
            c2='green' 
            M4[x-y][y] = colorFader(c1,c2,(x-2*l)/l)
for x in range(m-1):
    for y in range(x+1):
        if (2*l) <= x < (3*l-1):
            c1='blue' 
            c2='green' 
            M4[m-1-y][m-1+y-x] = colorFader(c1,c2,(x-2*l)/l)
        if (l) <= x < (2*l):
            c1='indigo' 
            c2='blue' 
            M4[m-1-y][m-1+y-x] = colorFader(c1,c2,(x-l)/l)
        if  x < (l):
            c1='violet' 
            c2='indigo' 
            M4[m-1-y][m-1+y-x] = colorFader(c1,c2,(x)/l)
plt.subplots(figsize=(6, 6))
plt.imshow(M4)
plt.show()