# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 22:32:47 2019

@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt

f = 50
fs = 1000
A = 1
N = 10
T = 1/f
a=(N*(1/f))/(1/fs)
c=int(a)
t = np.linspace(0,N*T,c)
s = A*np.sin(2*np.pi*f*t)
plt.plot(t,s)
plt.xlabel('t')
plt.ylabel('s(t)')
plt.title('bieu dien S(t)')
plt.show
plt.savefig('books_read.png')






