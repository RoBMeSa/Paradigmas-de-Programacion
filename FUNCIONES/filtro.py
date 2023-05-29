#======================
# Uso de filtros
#======================

#====================================================
# Hacer una lista de los numeros por arriba del promedio
#====================================================

# Módulo de estadística
import statistics

bigdata = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
promedio = statistics.mean(bigdata)
print promedio

#==================================================================
# Hazme una lista de elementos que cumplan la condicion x > promedio
# filter(condicion, datos)
#==================================================================

print(list(filter(lambda x: x > promedio, bigdata)))

#=======================
# Limpiar los dados
#=======================

paises = ["", "Argentina", "", "Brasil", "", "Chile", "Mexico", "", "Colombia", "", "", "Cuba", "Venezuela"]
