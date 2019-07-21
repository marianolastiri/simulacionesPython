# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:33:24 2019

@author: mariano
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:42:40 2019

@author: mariano
"""
import random
import numpy as np
import csv

def mis_vecinos(coord_centro):
    x = coord_centro[0]
    y = coord_centro[1]
    vecinos = [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y+1), (x+1,y+1), (x+1,y), (x+1,y-1), (x,y-1)]
    return vecinos

def buscar_adyacente(tablero, coord_centro, objetivo):
    coord_vecina = []
    x = mis_vecinos(coord_centro)
    for i in range(len(x)):
        if tablero[x[i]] == objetivo:
            coord_vecina.append(x[i])
    return coord_vecina


def fase_mover(tablero):
    n_fila = tablero.shape[0]
    n_col = tablero.shape[1]
    for i in range(1, n_fila-1):
        for j in range(1, n_col-1):
            if tablero[(i,j)] != " ":
                vacio = buscar_adyacente(tablero, (i,j), " ")
                if vacio != []:
                    tablero[vacio[0]] = tablero[(i, j)]
                    tablero[(i, j)] = " "
                
def fase_alimentacion(tablero):
    n_fila = tablero.shape[0]
    n_col = tablero.shape[1]
    for i in range(1, n_fila-1):
        for j in range(1, n_col-1):
            if tablero[(i,j)] == "L":
                vacio = buscar_adyacente(tablero, (i,j), "A")
                if vacio != []:
                    tablero[vacio[0]] = tablero[(i, j)]
                    tablero[(i, j)] = " "

def fase_reproduccion(tablero):
    n_fila = tablero.shape[0]
    n_col = tablero.shape[1]
    for i in range(1, n_fila-1):
        for j in range(1, n_col-1):
            if tablero[(i,j)] != " ":
                pareja = buscar_adyacente(tablero, (i,j), tablero[(i,j)])
                vacio = buscar_adyacente(tablero, (i,j), " ")
                if pareja != [] and vacio != []:
                    tablero[vacio[0]] = tablero[(i,j)]

def evolucionar(tablero):
    fase_alimentacion(tablero)
    fase_reproduccion(tablero)
    fase_mover(tablero)
    
def evolucionar_en_el_tiempo(tablero, tiempo_limite):
    for i in range(tiempo_limite):
        evolucionar(tablero)
    
def mezclar_celdas(tablero):
    celdas = []
    n_fila = tablero.shape[0]
    n_col = tablero.shape[1]
    for i in range(1, n_fila-1):
        for j in range (1, n_col-1):
            celdas.append((i, j))
    random.shuffle(celdas)
    return celdas

def generar_tablero_azar(filas, columnas, n_antilopes, n_leones):
    t = np.repeat(" ", filas*columnas).reshape(filas, columnas)
    n_fila = t.shape[0]
    n_col = t.shape[1]
    tipo = []
    for i in range(n_fila):
        for j in range(n_col):
            t[(0, j)] = "M"
            t[(i, 0)] = "M"
            t[(n_fila-1, j)] = "M"
            t[(i, n_col-1)] = "M"
    x = mezclar_celdas(t)
    for i in range(n_antilopes):
        tipo.append("A")
    for j in range(n_leones):
        tipo.append("L")
    for k in range(len(tipo)):
        if len(x) > k:
            t[x[k]] = tipo[k]
    return t

def cuantos_de_cada(tablero):
    n_fila = tablero.shape[0]
    n_col = tablero.shape[1]
    contador = [0, 0]
    for i in range(1, n_fila-1):
        for j in range(1, n_col-1):
            if tablero[(i, j)] == "A":
                contador[0] = contador[0] + 1
            elif tablero[(i, j)] == "L":
                contador[1] = contador[1] + 1
    return contador
    
def registrar_evolucion(tablero, tiempo_limite):
    cantidades = []
    for i in range(tiempo_limite):
        registro = cuantos_de_cada(tablero)
        cantidades.append(registro)
        evolucionar_en_el_tiempo(tablero, i)   
    registro = cantidades
    with open ("predpres.csv", "w", newline = "") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["antilopes", "leones"])
        csv_writer.writerows(registro)
    return cantidades

a = generar_tablero_azar(12, 12, 10, 5)
print(a)
b = registrar_evolucion(a, 5)
print(b)