# Una Lista o Areglo es una estructura de datos que permite guardar un conjunto de valores.
lista_vacia = []
lista_compras = ['tomate', 'pan', 'queso', 'jamón']

# A diferencia de otros lenguajes, las listas en Python pueden tener distintos tipos de datos, cadenas, números, inclusive otras listas o tuplas.
lista_especial = [1, 2, ['a', 'b', 'c'], True]



"""
En Python es puedes combinar y duplicar valores utilizando los operadores + y *.
Si “sumas” dos listas, se creará una nueva lista que contiene todos los valores de ambas listas combinadas.
"""
verso1 = ['dale', 'a', 'tu', 'cuerpo']
verso2 = ['alegria', 'macarena']
estrofa = verso1 + verso2
print(estrofa)
cancion = 3 * estrofa
print(cancion)



"""
Cada cajón está representado por un número, al cual lo conocemos como índice; este sirve como dirección/posición única que apunta a cada ítem dentro del mueble.
Para acceder a ellos lo haremos de la siguiente manera:
"""
cajonera = ["pantalones", "camisetas", "calcetines"]
print(cajonera[0]) #Accedemos al cajón con índice 0. Imprime: "pantalones"
print(cajonera[1]) #Accedemos al cajón con índice 1. Imprime: "camisetas"
print(cajonera[2]) #Accedemos al cajón con índice 2. Imprime: "calcetines"
cajonera[1] = "sueters" #Cambiamos el valor del cajón con índice 1
print(cajonera) #Imprime: ['pantalones', 'sueters', 'calcetines']



"""
Como mencionamos anteriormente, las listas son dinámicas, por lo que a través de la función .append() podemos agregar elementos.
Esta función agrega un nuevo elemento al final de la lista dada.
"""
cajonera.append("vestidos") #Agregamos "vestidos" al final de la lista
print(cajonera) #Imprime: ['pantalones', 'sueters', 'calcetines', 'vestidos']



"""
Slicing o “Troceado” nos permite regresar una copia de parte de nuestra lista en base a índices específicos.
La síntaxis utilizada es: [x:y], donde x es el índice inicial y y el índice final.
"""
lista_grande = [2, 4, 6, 8, 10, 12, 14, 16]
print(lista_grande[3:]) #Imprime:[8, 10, 12, 14, 16]
print(lista_grande[:6]) #Imprime:[2, 4, 6, 8, 10, 12]
print(lista_grande[3:6]) #Imprime:[8, 10, 12]



# FUNCIONES INTEGRADAS

# len(secuencia): Regresa la cantidad de elementos en la secuencia.
vocales = ['a', 'e', 'i', 'o', 'u']
print(len(vocales)) #Imprime: 5

"""
Ejemplos de funciones para secuencias:
len(secuencia): devuelve la longitud (cantidad de elementos) de una secuencia.
max(secuencia): devuelve el valor más alto en una secuencia.
min(secuencia): devuelve el valor más bajo en una secuencia.
sorted(secuencia): devuelve una secuencia ordenada.
"""



# MÉTODOS ESPECÍFICOS DE LISTAS

# La sintaxis de estos métodos es colocar primero la lista, seguida de un punto y después el método, como por ejemplo:
frozen = ["Elsa", "Anna", "Olaf"]
frozen.pop() #Sintaxis: nombre_lista.funcion()
print(frozen) #Imprime: ['Elsa', 'Anna']

"""
Algunos métodos comunes para las listas son:
list.append(valor): añade un valor al final de la lista.
list.pop(índice): elimina un valor en la posición dada. Si no se pasa ningún parámetro, se eliminará el último valor en la lista.
list.index(valor): devuelve el índice (posición) del valor dado si existe en la lista y genera un error si no existe.
list.reverse(): invierte el orden de los elementos, en su lugar.*
list.sort(): ordena los elementos de menor a mayor, o alfabéticamente para cadenas.
"""