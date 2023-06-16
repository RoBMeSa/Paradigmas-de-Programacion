from multiprocessing import Process
import os
import math
import time

def calc():
    for i in range (0, 4000000):
        math.sqrt(i)

procesos = []
cpus = os.cpu_count()
print("Nucleos en el gpu: ", cpus)
for i in range(cpus):
    print("Registrando el proceso %d" % i)
    procesos.aooend(Thread(target=calc))

start = time.time()

for proceso in procesos:
    proceso.start()
for proceso in procesos:
    proceso.join()

end = time.time()
print("Se tardó: ", end-start)
