#======================================================
# Ejemplo de comunicacion bloqueada a un algoritmo compartido
#======================================================
from multiprocessing import Process, Array, Lock
import time

def sumale100(numeros, candado):
    for i in range(100):
        time.sleep(0.01)
        #Usando candado
        for i in range (len(numeros)):
            #Lo que este dentro de con candado no puede accederse 
            # Desde otro proceso al mismo tiempo
            with candado:
                #Hacer la operacion
                numeros[i] += 1

if __name__ == "__main__":
    #==========================================================
    # Candado para evitar que dos procesos se empalmen
    #==========================================================
    candado = Lock()

    #Numero común a los procesos, d de dobles
    numeros_compartidos = Array('d', [0.0, 100.0, 200.0])

    #: quiere decir todos los elementos
    print("Al principio vale =", numeros_compartidos[:])

    #Dos procesos
    p1 = Process(target=sumale100, args=(numeros_compartidos, candado))
    p2 = Process(target=sumale100, args=(numeros_compartidos, candado))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Al final vale = ", numeros_compartidos[:])

