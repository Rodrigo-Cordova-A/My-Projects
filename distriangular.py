# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 08:22:22 2023

@author: Rodrigo
"""
import numpy as np
import matplotlib.pyplot as plt

def fun_exp (lam, N):
    R = np.random.rand(N)
    x = -np.log(1- R)/lam
    return x
def distriangular(a,b,c, N):
    R = np.random.rand(N)
    x = np.zeros(N)
    corte = (c-a)/(b-a)
    for i in range(0, N):
        if 0 < R[i] < corte:
            x[i] = a + np.sqrt(R[i]*(b-a)*(c-a))
        else:
            x[i] = b - np.sqrt((1 - R[i])*(b-a)*(b-c))
    return x

N = 20000
x = distriangular(50,90,82, N)

print('El valor esperado es aproximadamente ',(sum(x)/N))
maxi = max(x)
C = 50
plt.hist(x, bins = C)
plt.show()
