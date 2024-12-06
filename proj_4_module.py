import numpy as np
import matplotlib.pyplot as plt
import random as rd

rd.seed(1550)
def mov(L, p, a = 0, b = 0):

    x = [a]
    y = [b]
    r = [0]
    dx, dy = 0, 0
    if p>1:
        return "No uses eso como probabilidad"
    for j in range(L**2):
        rx = round(rd.random(),2)
        ry = round(rd.random(),2)
        
        if rx <= p:
            dx = 1
            
        else:
            dx = -1
            
        if ry <= p:
            dy = 1
        else:
            dy = -1
        x.append(x[-1] + dx)
        y.append(y[-1] + dy)
        r.append(np.sqrt(((x[-1]-a)**2 + (y[-1]-b)**2)))

    return x, y, r
def mov2(L, a = 0, b = 0):

    x = [a]
    y = [b]
    r = [0]
    dx, dy = 0, 0
    for _ in range(L**2):
        rx = rd.uniform(0,2*np.pi)
        ry = rd.uniform(0,2*np.pi)
        
        dx = x[-1]+np.cos(rx)
        dy = y[-1]+np.sin(rx)
        x.append(dx)
        y.append(dy)
        r.append(np.sqrt(((x[-1]-a)**2 + (y[-1]-b)**2)))

    return x, y, r
T = np.linspace(0,0.99999,1000)

L = 650
T2 = [i for i in range(L**2-1)]
X,Y, r= mov2(L)
R = [np.mean(mov(15,i)[-1]) for i in T]
R2 = [np.abs(r[i+1]-r[i]) for i in T2]
#X = np.matrix.flatten(X)
#Y = np.matrix.flatten(Y)

plt.hist(R2)


plt.show()
