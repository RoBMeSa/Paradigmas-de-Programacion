import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()


#================================
# Arreglo con un solo elemento
#================================
randNum = np.zeros(1)

if rank == 1:
        randNum = np.random.random_sample(1)
        print("Proceso ", rank, " generó ", randNum[0])
        comm.Isend(randNum, dest=0)
        req = comm.Irecv(randNum, source=0)
        req.Wait()
        print("proceso ", rank , " recibió el numero", randNum[0])
if rank == 0:
        randNum = np.random.random_sample(1)
        print("Proceso ", rank, " generó ", randNum[0])
        comm.Isend(randNum, dest=1)
        req = comm.Irecv(randNum, source=1)
        req.Wait()
        print("proceso ", rank , " recibió el numero", randNum[0])
