# Diccionarios
estudiante = {"nombre": "Gonzalo", "curso": "Python"} # <-- Notación Literal
# Imprimir el valor de estudiante
print(estudiante["nombre"])



estudiante["nombre"] = "Vicente"
print(estudiante["nombre"])



estudiante["nombre"] = "Arael"
print(estudiante["nombre"])



# Diccionario de países
paises = {} # <-- Diccionario vacío
paises["MEX"] = "México" # <-- Agregando valores
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"
paises["PER"] = "Perú"
paises["ARG"] = "Argentina"
print(paises)



if "CRI" in paises: #Preguntamos si existe la clave en el diccionario
   print("¿Deseas reemplazar el valor?")
else: #No existe esa clave
   paises["CRI"] = "Costa Rica"
print(paises) # <-- Confirmar si se añadió



valor_removido = paises.pop("MEX") #Elimina el elemento y devuelve su valor
del paises["COL"] #Elimina el elemento
print(paises) #Imprime: {'CHL': 'Chile'}



# Sintaxis multi-línea
pintor = {
   "nombre": "Frida Kahlo",
   "pais": "México",
   "fecha_nacimiento": "6 de julio de 1907"
}

# Diccionarios anidados
escuela = {
   "nombre": "Coding Dojo LATAM",
   "profesores": [
       {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},
       {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},
       {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}
   ]
}

