# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 09:14:14 2019

@author: mariano
"""
import numpy as np
import matplotlib.pyplot as plt
dt = 60*60*24
tiempo_total = 400
x_tierra = [-147095000000.0, -147095000000.0]
y_tierra = [2617920000.0, 0.0]
x_sol = 0.0
y_sol = 0.0
masa_tierra = 5972190000000000000000000
masa_sol = 1989100000000000000000000000000
G = 6.67259 * (10**-11)
dias = [0, 1]
for i in range (1, tiempo_total-1):
    delta_x = x_sol - x_tierra[i]
    delta_y = y_sol - y_tierra[i]
    # calculo la fuerza de x
    f_x = (G*masa_tierra*masa_sol/(delta_x**2 + delta_y**2)) * (delta_x/np.sqrt(delta_x**2 + delta_y**2))
    x_actual = x_tierra[i]
    x_prev = x_tierra[i-1]
    x_nueva = 2*x_actual - x_prev + (f_x/masa_tierra) * dt**2
    x_tierra.append (x_nueva)
    # idem para y
    f_y = (G*masa_tierra*masa_sol/(delta_x**2 + delta_y**2)) * (delta_y/np.sqrt(delta_x**2 + delta_y**2))
    y_actual = y_tierra[i]
    y_prev = y_tierra[i-1]
    y_nueva = 2*y_actual - y_prev + (f_y/masa_tierra) * dt**2
    y_tierra.append(y_nueva)
    # actualizo el tiempo
    dias.append(i)
print(x_tierra)
print(y_tierra)
plt.title (" Posicion del objeto ")
plt.plot (x_tierra, y_tierra,"b")
plt.plot (x_sol, y_sol,"yo")
plt.xlabel ("x")
plt.ylabel ("y")
plt.show ()