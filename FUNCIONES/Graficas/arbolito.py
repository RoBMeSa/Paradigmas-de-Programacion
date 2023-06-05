#============================================================
# Graficos usando la tortuga que pinta al caminar
#============================================================
import turtle 
tortuga = turtle.Turtle()
tortuga.left(90) #Giro a la izq de 90 grados
tortuga.speed(3) #Velocidad de la tortuga
# import matplotlib  as plt
#=====================================
# Con angulos de 90 es un arbol H
#=====================================

angulo:float = 90

#===========================================
# El arbol se construye con recursividad
#===========================================
def arbol(i:float, angulo:float):
    if i<10.0:
        return
    else:
        tortuga.forward(i) #Camina i
        tortuga.left(angulo) #Gira a la izquierda 90 grados
        arbol(3.0*i/4.25, angulo) #PIde otro arbol y cambia la longitud del paso
        tortuga.right(2*angulo) #Gira a la derecha 180 grados
        arbol(3.0*i/4.25, angulo)
        tortuga.left(angulo)
        tortuga.backward(i)

arbol(100, angulo)
turtle.done()
        
