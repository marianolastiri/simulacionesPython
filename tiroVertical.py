# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 11:01:34 2019

@author: mariano
"""

import matplotlib.pyplot as plt
dt = 0.001
numero_pasos = 20500
g = 9.8
y0 = 0
vy = 1
y1 = 0.1
tiempos = [0, dt]
alturas = [y0, y1]
for i in range (1 , numero_pasos - 1) :
    # actualizo la posicion
    y_actual = alturas[i]
    y_prev = alturas[i-1]
    nueva_posicion = 2 * y_actual - y_prev - g * dt**2
    alturas.append (nueva_posicion)
    # actualizo el tiempo
    nuevo_tiempo = tiempos [i] + dt
    tiempos.append (nuevo_tiempo)

print(tiempos)
print(alturas)

plt.title (" Posicion del objeto ")
plt.plot (tiempos, alturas,"r")
plt.xlabel ("tiempo (s)")
plt.ylabel ("altura (m)")
plt.show ()