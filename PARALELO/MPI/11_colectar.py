from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = (rank+1)**2

#===================================
# Manden sus datos al proceso root = 0 (en orden)
#======================================

datas = comm.gather(data, root= 0)

#==================================
# Asegurarse que todo funcione
#==================================

if rank == 0:
    for i in range ( size):
        assert datas[i] == (i+1)**2
else:
    assert datas is None

print(datas)

