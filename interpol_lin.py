#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 15:02:15 2021

@author: dr.guillermo
"""

#interpolación 
import numpy as np
import matplotlib.pyplot as plt

#sistema de ecuaciones
x=np.array([1,2.]) 
y=np.array([2,6])

N=len(x)
A=np.zeros((N,N))
b=np.zeros(N)
b=y
# Ax = b 
# llenamos N columnas
# utilizamos la matriz traspuesta
for i in range(N):
    A.T[i]=x**i   # recordemos que x**0 = 1
                  # x**1, x**2
    
# verificamos que se forme la matriz
# print(A)
print(A,b) 

#resolvemos el sistema de ecuaciones 
# en a nos regresa la ordenada y la pendiente
a=np.linalg.solve(A,b)
print("Solución= ")
print(a)

# Gráficamos los datos experimentales
plt.plot(x,y,'ro')

# calculamos la y teórica y la gráficamos en azul
yteo= a[0]+a[1]*x

plt.plot(x,yteo,'b-')
plt.title('Interpolación Lineal')
plt.show()