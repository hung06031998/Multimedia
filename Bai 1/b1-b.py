# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 00:29:50 2019

@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt

f = 50
fs = 10000
A = 1
N = 1
T = 1/f
c=(N*T)/(1/fs)
t = np.linspace(0,N*T,c)
n = 2
for i in range(0,2*n+2):
    s =+ (A/((2*i+1)*(2*i+1)))*np.sin(2*np.pi*(2*i+1)*f*t)
#ket thuc vong lap
plt.plot(t,s)
plt.xlabel('t')
plt.ylabel('s(t)')
plt.title('bieu dien S(t)')
plt.show
plt.savefig('books_read_2.png')
