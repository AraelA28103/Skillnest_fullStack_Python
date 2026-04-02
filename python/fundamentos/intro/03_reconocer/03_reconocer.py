"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random # Importar librerías (Similar a bootstrap)


nombre = "Frida Kahlo" # Creación de variable tipo texto (string)
print(type(nombre)) # Imprime una variable identificando su tipo de dato "type()"
print(len(nombre)) # Devuelve el largo de una variable

 
edad = 25 # <-- Creación de variable tipo numerica


if edad < 18: # Se establece condición "if", si edad es menor a 18
   print("Eres menor de edad.") # Imprime un mensaje
elif edad == 18: # Se establece condición "else if", si edad es igual a 18
   print("Tienes 18 años.") # Imprime un mensaje
else: # Se establece condición "else", si las otras condiciones no se ejecutaron
   print("Eres mayor de edad.") # Imprime un mensaje


frutas = ["manzana", "pera", "fresa"] # Creación de variable tipo array
print(frutas[0]) # De la variable array imprime el 1er elemento 
frutas[0] = "banana" # Actualiza el 1er elemento de la variable array
frutas.append("uva") # Agrega "uva" al final del array
frutas.remove("pera") # Elimina "pera" del array


dimensiones = (200, 50) # Creación de variable tipo tupla (Variable inmutable)
print(dimensiones[0]) # Imprime el 1er elemento de la variable tupla


persona = { # Creación de variable tipo objeto (object)
   "nombre": "Carlos", # Se establece un item y su respectivo valor
   "edad": 30 # Se establece un item y su respectivo valor
}
print(persona["nombre"]) # Imprime un valor de un item
persona["edad"] = 31 # Se actualiza el valor del item "edad" a 31
persona["ciudad"] = "Santiago" # Se actualiza el valor del item "ciudad" a Santiago
del persona["ciudad"] # Elimina X item


for i in range(5): # Se crea un bucle en rango 5
   if i == 2: # Cuando "i" sea igual a 2
       continue # Ignora el proceso y "continúa"
   if i == 4: # Cuando "i" sea igual a 4
       break # Rompe el bucle
   print(i) # Imprime los valores de la variable "i"


contador = 0 # Creación de variable numerica
while contador < 3: # Mientras la variable sea menor a 3 continúa
   print(f"while contador es: {contador}") # Imprime concatenando cierto texto y al variable contador
   contador += 1 # Se suma 1 al valor actual de la variable contador


def saludar_usuario(nombre): # def = function en JS
   return f"Hola, {nombre}" # Devuelve el valor de la funcion concatenado con texto


print(saludar_usuario("Francisca")) # Se imprime usando la función saludar_usuario "Hola, Fransisca"