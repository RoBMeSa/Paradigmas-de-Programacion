import numpy as np
import mathplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mathplotlib import cm
import time

#-------------------------------------------------------------
#Numero de celdas
n = np.array([512,512])
#Tamaño del dominio (menor que uno)
L = np.array([1.0,1.0])
#Constante de difusion
k = 0.2
#Pasos de tiempo
pasos = 100
#-------------------------------------------------------------


#Tamaño de las celdas
dx = L/n
udx2 = 1.0/(dx*dx)
#Paso de tiempo
dt = 0.25*(min(dx[0], dx[1])**2)/k
print("dt = ", dt )
#Total de celdas
nt = n[0]*n[1]
#Llenar la solucion con ceros
u = np.zeros(nt, dtype=np.float64) #Arreglo de lectura
un = np.zeros(nt, dtype= np.float64) #Arreglo de escritura

def evolucion(u, n, udx2, dt, i, k):


