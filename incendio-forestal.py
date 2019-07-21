# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:13:18 2019

@author: mariano
"""
import random
import numpy as np
import matplotlib.pyplot as plt
def generarBosque(n):
    bosque = []
    for i in range(n):
        bosque.append(0)
    return bosque
    
def brotes(bosque, p):
    for i in range(len(bosque)):
        brotar = random.random()
        if brotar >= p:
            bosque[i] = 1

def cuantos(bosque, tipoCelda):
    contador = 0
    for i in range(len(bosque)):
        if bosque[i] == tipoCelda:
            contador += 1
    return contador

def rayos(bosque, f):

    for i in range(len(bosque)):
        rayo = random.random()
        if rayo <= f and bosque[i] == 1:
            bosque[i] = -1

def propagacion(bosque):
    for i in range(0, len(bosque)-1):
        if bosque[i] == -1 and bosque[i+1] == 1:
            bosque[i+1] = -1
    for j in range(len(bosque)-1, 0, -1):
        if bosque[j] == -1 and bosque[j-1] == 1:
            bosque[j-1] = -1
    #if bosque[0] == 1 and bosque[1] == -1:
      #  bosque[0] = -1
    #if bosque[len(bosque)-1] == -1 and bosque[len(bosque)-2] == 1:
     #   bosque[len(bosque)-2] = -1

def limpieza(bosque):
    for i in range(len(bosque)):
        if bosque[i] == -1:
            bosque[i] = 0

def simularIncendio(rep, p, f):
    a = generarBosque(100)
    sobrevivientes = []    
    for i in range(rep):
        brotes(a, p)
        rayos(a, f)
        propagacion(a)
        limpieza(a)
        sobrevivientes.append(cuantos(a, 1))
    return sobrevivientes

def optimizar():
    probs = []
    promedios = []
    valores_p = np.arange(0.0, 1.0, 0.01)
    for i in range(len(valores_p)):
        a = simularIncendio(100, valores_p[i], 0.02)
        avg = np.mean(a)
        probs.append(valores_p[i])
        promedios.append(avg)
    plt.plot(probs, promedios, ".")
    plt.show()

def graficar(n):
    for i in range(n):
        optimizar()
        
graficar(5)