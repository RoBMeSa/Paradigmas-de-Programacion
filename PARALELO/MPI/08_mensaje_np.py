from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#===================================
# Se indica el tipo de datos explicitamente
#===================================

#===================================
# Ejemplo 1 USANDO ENTEROS
#===================================

if rank == 0:
   #=================================== 
   # Arreglo de enteros del 0 al 9
   #===================================

    data = numpy.arange(10, dtype = 'i')
    #===================================
    # Envio bloqueante especificando el tipo de dato
    #===================================
    comm.Send([data, MPI.INT], dest = 1, tag = 77)

elif rank == 1:
    data = numpy.empty(10, dtype = 'i')
    comm.Recv([data, MPI.INT], source = 0, tag = 77)
    print(data)


#==================================================
# Tambien se puede sin decir el tipo de dato pero deben
# coincidir el tipo de arreglos a los extremos del mensaje
#==================================================

#==============================
# Ejemplo 2 usando flotantes
#==============================
if rank == 0:
     data = numpy.arange(10, dtype=numpy.float64)
     comm.Send(data, dest=1, tag = 13)
elif rank == 1:
     data = numpy.empty(10, dtype = numpy.float64)
     comm.Recv(data, source = 0, tag = 13)
     print(data)


