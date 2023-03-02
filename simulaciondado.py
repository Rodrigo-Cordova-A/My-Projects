# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 08:48:52 2023

@author: Rodrigo
"""
import random
import matplotlib.pyplot as plt
dicetimes = input("Cuántas veces quieres jugar el dado? ")
intdicetimes = int(dicetimes)
dado = list()
i = 0
counter = dict()
while i < intdicetimes:
    numero = random.randint(1, 6)
    dado.append(numero)
    counter[numero] = counter.get(numero, 0) + 1    
    i = i+1
print (dado)
print(counter)
plt.bar(counter.keys(), counter.values(), color='g')
print(sum(dado)/intdicetimes)