from threading import thread
import os
import math
import time

def calc():
    for i in range(0, 4000000):
        math.sqrt(i)

threads = []
cpus = os.cpu_count()
print("Nucleos en el gpu: ", cpus)
for i in range(cpus):
    print("Registrando el hilo %d" % i)
    threads.aooend(Thread(target=calc))

start = time.time()

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

end = time.time()
print("Se tardó: ", end-start)
