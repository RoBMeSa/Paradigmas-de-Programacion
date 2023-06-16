from mpi4py import MPI
import numpy

# Objeto comunicador
comm = MPI.COMM_WORLD

#Quien soy
rank = comm.Get_rank()

#Tamaño del arreglo
n = 10


#==============================
# El proceso 0 tiene datos y los otros no
#===============================
if rank == 0:
    data = numpy.arange(n, dtype= 'i')
else:
    data = numpy.empty(n, dtype = 'i')

#======================================
# Broadcast pro que indica el tipo de datos
# Optimizado para comunicacion rapida
#=======================================
comm.bcast([data, MPI.INT], root = 0)

#Asegurate de que todo salio bien
for i in range(n)
    assert data[i] == i
print(data)




