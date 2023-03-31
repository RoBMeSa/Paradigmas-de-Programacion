''' ESTE ES UN SUPERCOMENTARIO
    DE INICIO A NUESTRO RESUMEN
'''
#======================
# Operaciones básicas
#=====================
print (2+3)
print (2*3)
print (2/3)
print (2**10)
print (2**.5)
print (10%2)
print (10%.1)

#=========================================
# Para saber el tipo de objeto se usa type
#=========================================
t=0
print(type(t)) #entero
t=3.6
print(type(t)) #real (flotante)
t=True
print(type(t)) #booleano (bool)

#==========================
# Mensajes a pantalla
#==========================
print("Este es un comando de python. ", "Este es otro enunciado.", t)
print('id: ',1)
print('First Name: ', 'Steve')
print('Last Name: ', 'Jobs')
print("vamos a sumar esto" + "con esto otro")
#=========================================
#  Continuar una instrucción en varios renglones
#=========================================
if 100>99 and \
        200 <= 300 and\
        True != False:
            print('Hello World')

#=============================================
#  Comandos diferentes en la misma linea
#=============================================
print("Hola ");print("tu¡ ") #Se considera mala practica

#=============================================
# Usando parentesis redondos, cuadrados o llaves
# Se puede escribir en varios renglones
#=============================================
list = [1,2,3,4,
        5,6,7,8,
        9,10,11,12]

matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

print(list)
print(matriz)

#=========================================================================
# Identación estricta para procesos dependientes de : (Dos puntos)
#=========================================================================
if 10>5:
    print ("diez es mayor que cinco")
    print ("Otra identación")
for i in list:
    print(i)
    print("ok")
if 10>5:
    print("verdadero")
elif 5>3: #comienza segundo condicional
    print("esto no se imprimirá")
else:
    print("aqui nunca llega")

#====================
# Funciones
#====================
def say_hello(name):
    print("Hello ", name)
    print("Welcome to Python Tutorials")

say_hello("Julián")

#===========================================================================
#   Input permite obtener datos del usuario en prompter
#===========================================================================
nombre = input("Dame tu nombre: ")
print("Hola como estás", nombre)

#=================================================
# Los enteros son de precisión limitada
#=================================================
y = 5000000000000000000000000000000000000000
print(y)

#========================================================
# Se pueden delimitar números con guión bajo pero no con coma
#=========================================================
y = 5_000_000
print(y)

#============================================================
# La función int() cambia strings y floats a enteros 
#============================================================
numero = int(input("Dame tu edad: "))
type(numero)

#============================================================
# La notación científica de flotantes utiliza e o E
#===========================================================
# 1.2 x10^{-9}
#===============
y= 1.2E-09
print(y)


#============================================================
# La funcion float() convierte strigs y enteros a flotantes
#============================================================
y = float("14.3")
print(y)

#=============================================================
# Los complejos se escriben con la raíz de menos uno 
# j siempre con un número como prefijo
# no acepta la j suelta
#============================================================
z = 1+1j

#suma +
#resta - 
#multiplicación *
#division /
#modulo %
#exponente **
#// funcion piso
#Funciones para transformar números int() float() complex()
#Operaciones abs() round() pow()

print(round(3.14159,4))

#==================================
# Strings de varias lineas
#==================================
parrafo =  """ En el bosque de la china
 la chinita se perdio"""
print(parrafo)

#================================================
# La funcion len() obtiene el tamaño del string
#================================================
n = len(parrafo)
print(n)

#===================================================================
#   Las letras en un string ocupan lugar como en un arreglo 
#   (también de atras para adelante comenzando en -1 el último)
#===================================================================
palabra = "hola"
print(palabra[0])
print(palabra[-4])

#===============================================
# Conjunto en Python
#===============================================
even_nums = {2,4,6,8,10} #Conjunto de numeros pares
print(even_nums)

# El bool no es parte del conjunto
emp = {1,'Steve',10.5,True} #Conjunto de diferentes objetos
print(emp)

nums = {1,2,2,3,4,4,5,5}
print(nums)

#================================================
#  Convertir secuencia a conjunto 
# No lo genera en orden
#================================================
s = set('hello')
print(s)
s = set((1,2,3,4,5)) # Tupla a conjunto
print(s)

s.add(100)
print(s)

s.update(nums)
print(s)

s.remove(100)
print(s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

su = s1|s2 #Union
print(su)

si = s1&s2 #Interseccion
print(si)

sr = s1 - s2  #Diferencia de conjuntos
print(sr)

sp = s2-s1
print(sp)

ss = s1^s2 #Diferencia simétrica
print(ss)

#============================================
# Uso de diccionarios
#============================================
capitals = {"USA":"Washington D.C", "France":"Paris","India":"New Dehli"}
print(capitals)

#============================================
# Llave valor
#============================================

# Diccionario valor
d={}

#Llave entera, valor string
numNames={1:"One", 2:"Two", 3:"Three"}

#Llave real, valor string
numNames={1:"One and half", 2.5: "Two and half", 3.5:"Three and half"}

#Llave tupla, valor string
items={("Parker","Reynolds","Camlin"):"pen",("LG","Whirpool","Samsung"):"Refrigerator"}

#Llave string, valor int
romanNums = {'I':1,'II':2,'III':3,'IV':4, 'V':5}
print(romanNums)
print(romanNums["I"])

print(capitals.get("India"))
print(capitals.get("india"))

#Reportar llave y valor
capitals["Mexico"] = "CDMX"
print(capitals)

#Borrar dato del diccionario
del capitals["Mexico"]
print(capitals)

#Borrar todo el diccionario
del capitals

#Reportar llaves
print(romanNums.keys())

#Reportar valores 
print(romanNums.values())

#Juicio de llave (está o no está la llave en el diccionario)
print("I" in romanNums)
print("X" in romanNums)
print("XX" not in romanNums)

#===================================================
#    Listas
#    Las listas pueden ser de objetos diferentes
#===================================================

miprimeralista = [] #Lista vacia
print(miprimeralista)

#===================================================
#    Llenado de lista
#===================================================
miprimeralista = [1, "Javier", 1.34,"Bosco", "Angel", "Abigail", True]
print(miprimeralista)

#===================================================
#   list: hacer una lista
#   range(i,j): secuencia de i hasta j-1
#===================================================
nums = list(range(1,61))

for i in nums:
    print(i)

#===================================================
#  Incluir nuevos elementos en la lista
#===================================================
nums.append(61)
nums.append(62)
nums.append(63)
print(nums)

#==================================================
# Quitar elementos de la lista
#==================================================
nums.remove(61)
print(nums)


