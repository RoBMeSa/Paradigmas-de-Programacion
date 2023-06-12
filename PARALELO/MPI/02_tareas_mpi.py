#============================================
# mpirun -n 4 python3 tareas_mpi.py
#============================================
from mpi4py import MPI

#=========================
# Objeto de comunicadores
#=========================
comm = MPI.COMM_WORLD

#==========================
# Cuantos somos en total
#==========================
size = comm.Get_size()

#==================
# Quien soy
#==================
rank = comm.Get_rank()

#=======================================
# Si yo soy el cero hago esto
#=======================================
if rank == 0:
    print("Yo soy el proceso 0")

#=======================================
# Si yo soy el UNO hago esto
#=======================================
elif rank == 1:
    print("Yo soy el proceso 1")
#=======================================
# Si yo no soy ni el 0 ni el 1 hago esto
#=======================================
else:
    print("Yo no soy ninguno de los 2 primeros")

print("Reportandome soy el proceso ", str(rank), "de ", str(size))


