#import numpy untuk array
import numpy as np
#import matplotlib untuk menampilkan kordinat
from matplotlib import pyplot as plt
x0,y0 = input('masukkan kordinat 1: ').split()
x1,y1 = input('masukkan kordinat 2: ').split()
#konversi input sebelum (str -> int)
x0=int(x0)
x1=int(x1)
y0=int(y0)
y1=int(y1)
#array titik kordinat
data = np.array([[0,0],[0,0]])
#kordinat 1
data = np.append(data, [[x0,y0]], axis=0)
data = np.delete(data, 0, 0)
data = np.delete(data, 0, 0)
#selisih X
deltX = x1 - x0
#selisih Y
deltY = y1 - y0
#delta X*2
delt2X = 2 * deltX
#delta Y*2
delt2Y = 2 * deltY
#other calc
step = delt2Y - delt2X
#menghitung p0
p0 = delt2Y - deltX
while x0<x1:
        if p0 > 0:
                x0 = x0 + 1
                y0 = y0 + 1
                p0 = p0 + step
                data = np.append(data, [[x0,y0]], axis=0)	
        else:
                x0 = x0 + 1
                p0 = p0 + delt2Y
                data = np.append(data, [[x0,y0]], axis=0)
    
#menampilkan hasil titik dalam array
x, y = data.T
plt.scatter(x,y)
plt.show()

