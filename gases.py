# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:22:59 2019

@author: mariano
"""
import random
k = 0.1
#tamaño de la caja
xMax = 1000
yMax = 1000

#intervalo temporal
dt = 0.001
#posiciones en X de las npart
posicionX = []

#posiciones en Y de las npart
posicionY = []

#velocidades en X de las partículas
velocidadX = []

#velocidades en Y de las partículas
velocidadY = []

def iniciar_particulas(npart):
    for i in range(npart):
        posicionX.append(random.random()*xMax)
        posicionY.append(random.random()*yMax)
        velocidadX.append(random.random()*10)
        velocidadY.append(random.random()*10)


def calcular_fuerzas():
    fuerzaTotal = []
    for k in range(len(posicionX)):
        fuerzaTotal.append([0, 0])
    for i in range(len(posicionX)):
        for j in range(len(posicionX)):
            if i != j:
                dij = (posicionX[i] - posicionX[j])**2 + (posicionY[i] - posicionY[j])**2
                fX = 4*k*(posicionX[i]-posicionX[j])/dij**3
                fY = 4*k*(posicionY[i]-posicionY[j])/dij**3
                fuerzaTotal[i][0] = fuerzaTotal[i][0] + fX
                fuerzaTotal[i][1] = fuerzaTotal[i][1] + fY
    return fuerzaTotal
    
def nuevo_estado():
    for i in range(len(velocidadX)):
        velocidadX[i] = velocidadX[i] + calcular_fuerzas()[i][0] * dt
        velocidadY[i] = velocidadY[i] + calcular_fuerzas()[i][1] * dt
        posicionX[i] = posicionX[i] + velocidadX[i] * dt
        posicionY[i] = posicionY[i] + velocidadY[i] * dt
        if posicionX[i] > xMax:
            velocidadX[i] = -velocidadX[i]
            posicionX[i] = posicionX[i] - 2*(posicionX[i] - xMax)
        if posicionY[i] > yMax:
            velocidadY[i] = -velocidadY[i]
            posicionY[i] = posicionY[i] - 2*(posicionY[i] - yMax)
        if posicionX[i] < 0:
            velocidadX[i] = -velocidadX[i]
            posicionX[i] = posicionX[i] + 2 * posicionX[i]
        if posicionY[i] < 0:
            velocidadY[i] = -velocidadY[i]
            posicionY[i] = posicionY[i] + 2 * posicionY[i]
        
def cantidad_simulaciones(numero_pasos):
    for i in range(numero_pasos):
        nuevo_estado()
        print (10, file = salida)
        print (" ",file = salida)
        for jj in range (10):
            print ("6", posicionX[jj], posicionY[jj], "0", file = salida )


salida = open("salida.xyz", "w")
iniciar_particulas(10)
cantidad_simulaciones(1000)
salida.close()



