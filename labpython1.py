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
lista = [1,2,3,4,
        5,6,7,8,
        9,10,11,12]

matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

print(lista)
print(matriz)

#=========================================================================
# Identación estricta para procesos dependientes de : (Dos puntos)
#=========================================================================
if 10>5:
    print ("diez es mayor que cinco")
    print ("Otra identación")
for i in lista:
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
nums.append(61)
print(nums)

#==================================================
# Quitar elementos de la lista
#==================================================
nums.remove(61)
print(nums)

#==================================================
#  Quitar elemento con el índice i
#==================================================
i = 61
del nums[i]
print(nums)

#==================================================
# Borrar la lista
#==================================================
del nums
#==================================================
#  Sumar listas
#==================================================
L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2)

#==================================================
#  Llenado a mano
#==================================================
potencial = []
for i in range(0,10000):
    potencial.append(float(i))
print(potencial[100])

#==================================================
#  Generar una tupla con la lista
#==================================================
potencial = tuple(potencial)
print(potencial[100])

#=================================================
# Laboratorio 3
#=================================================

#================================================
# Condicionales
#================================================
precio = 50
#====================
#  Si esto
#====================
if precio < 50:
    print("El precio es menor que 50")
#============================
#  Si no... Si esto otro...
#============================
elif precio >50:
    print("El precio es mayor a 50")
#============================
#  Si nada de lo anterior...
#============================
else:
    print("El precio es 50")

precio = 50
cantidad = 5 
total = precio * cantidad

#=============================
#  Condicionales anidados
#=============================

if total > 100:
    if total > 500:
        print("Total es mayor que 500")
    else:
        if total < 500 and total > 400:
            print("Total es menor que 500 pero mayor a 400")
        elif total < 500 and total > 300:
            print("total entre 300 y 500")
        else:
            print("total entre 100 y 300")
#=========================================
#  Condicional de igualdad son == 
#=========================================
elif total == 100:
    print("Total es 100")
else:
    print("Total menor que 100")

#=============================================
#  Contador mientras la condicion sea verdadera
#=============================================
num =0
while num < 5:
     num = num + 1
     print('num = ', num)

num = 0
while num < 5:
    num += 1                # num +=1 es lo mismo que num = num + 1
    print('num = ', num)
    if num == 3:        # Conficion antes de salir del bucle
        break
num = 0
while num < 5:
    num += 1
    if num > 3:
        continue        # evitar lo que sigue, continuar con las iteraciones
    print('num = ',num)

#=================================================
#  Bucle sobre lista
#=================================================
nums = [10, 20, 30, 40, 50]
for i in nums:
    print(i)

#=================================================
#  Bucle sobre un string
#=================================================

for char in 'Hello':
    print(char)

#=================================================
# Bucle sobre un diccionario
# items = elementos
#=================================================
numNames = {1:'One', 2:'Two', 3:'Three'}
for pair in numNames.items():
    print(pair)

#=================================================
# Bucle sobre diccionario 
# Key = llave
# Value = valor
#=================================================
for k,v in numNames.items():
    print("key = ", k, ", value = ", v)
    
#=================================================
#   Primera funcion 
#=================================================
def saludo():
    #=============================================
    # Documentacion rapida de la función
    #=============================================
    """Esta funcion saluda"""
    print('¡Quiúboles!, ¿Como estás?')

#=================================================
#  Llamado de la función
#=================================================
saludo()

#=================================================
# Se ejecuta pero no se asigna
#=================================================
salida = saludo()

#==============================
#  Esto no funciona
#==============================

print(salida)

#================================
# Mostrar documentacion
#================================
# Help(saludo)

#================================
#  Funcion con argumento
#================================
def salu2(nombre):
    """ Esta función te saluda por tu nombre"""
    print(" ¡Que onda ese", nombre,"!")
    salu2("Julián")
    salu2("Ángel")

#=================================================
# Ahorrar trabajo del interprete
# nombre:str la variable nombre es un str
#=================================================

def saludos(nombre:str):
    """Esta funcion te saluda por tu nombre estrictamente"""
    print(" ¡Que onda ese", nombre,"!")
saludos("Julian")
a = 123
print(type(a))
saludos (a)


#=================================================
# Funcion con muchos argumentos
#=================================================
def saludos_multiples(nombre1, nombre2, nombre3):
    """Esta funcion saluda a 3 personas al mismo tiempo"""
    print("Hola ", nombre1, ", ", nombre2, " y ", nombre3)
saludos_multiples("Hugo", "Paco", "Luis")

#=================================================
# Funcion con cualquier numero de argumentos
#=================================================
def muchos_saludos(*nombres):
    """Esta funcion saluda a todos los que quieras"""
    i = 0
    #=============================================
    # end= es para ponerlo de corrido
    #=============================================
    print("Hola ", end= "")
    while len(nombres) > i:
        #Ultimo nombre 
        if(i==len(nombres)-1):
            print(nombres[i])
        else:
            #Cualquier otro nombre
            print(nombres[i], end=", ")
        i+=1
muchos_saludos("Bosco", "Angel", "David", "Tamara", "Mili", "Edwin", "Lev", "Luis", "Abigail")

def greet(firstname, lastname):
    print('Hello', firstname, lastname)

#=================================================
# Llamar la funcion con argumentos en desorden
#=================================================
greet(lastname='jobs', firstname='Steve')# Se pueden especificar las variables en desorden 

#=================================================
#  Funcin con argumentos escondidos ** 
#=================================================
def greet(**person):
    #=============================================
    #  Persona tiene caracteristicas firstname y lastname
    #=============================================
    print('Hello ', person['firstname'], person['lastname'])

greet(firstname='Steve', lastname='Jobs')
greet(lastname='JObs', firstname = 'Steve')
greet(firstname='Bill', lastname='Gates', age=55) # Se pueden pasar más parámetros de los necesarios

#================================================
#  Funcion con valores por defecto
#================================================
def greet(name = 'Guest'):
    print('Hello ', name)
greet () # Utiliza el valor dado de antemano
greet('Steve')

#=================================================
# Funcion con resultado
#================================================
def suma(a,b):
    return a + b

#================================================
#  Programacion funcional
#  Se pueden funciones en funciones
#================================================
total = suma(5, suma(10,20))
print(total)

#================================================
# Calculo lambda
# Nombre de la funcion = lambda variable : funcion
#===============================================

x_al_cuadrado = lambda x : x * x
a1 = x_al_cuadrado(5)
print(a1)

#=============================
# Lambda de varias variables
#=============================
suma = lambda x1, x2,x3: x1+x2+x3
print(suma(99,98,97))

sumas = lambda *x: x[0] + x[1] + x[2] + x[3]

print(sumas(100,200,300,400))

#================================================
#  Uso de una funcion anonima
#  El argumento va afuera entre paréntesis
#================================================

print((lambda x: x*x)(6)) # Funcion anonima

#================================================
# Funcion con variable global
# EVITE EL EXCESO!!!!!!!!!!!!!111
#================================================
name = 'Steve'
def greet():
    global name # Para utilizar una variable global ( que viene de fuera del bloque)
    name = 'Bill'
    print('Hello ' , name)
greet()

#Algoritmo 1
#=====================================
# Serie exponencial
# Factorización de x
# Negativos con función inversa
#=====================================
n = 200
x = -100.0
flag = False
if x<0: 
    flag = True
    x = -x
s=1.0
for i in range (n,0,-1):
    s *= x/float(i)
s+= 1.0
if flag == True:
    s = 1/s
print(s)


    

