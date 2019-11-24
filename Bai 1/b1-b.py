# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 00:29:50 2019

@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt
import math

f = 50
fs = 1000
A = 1
N = 1
n = 2
T = 1.0/float(f)
c=(N*T)/(1.0/float(fs))
a=int(c)
print(a)
t = np.linspace(0,N*T,a)
s=np.zeros(len(t))
for i in range(2*n+2):
    s += ((float(A)/(2*i+1)**2)*np.sin(2*math.pi*(2*i+1)*f*t))
#ket thuc vong lap
plt.plot(t,s)
plt.xlabel('t')
plt.ylabel('s(t)')
plt.title('bieu dien S(t)')
plt.show
plt.savefig('b1-b.png')

