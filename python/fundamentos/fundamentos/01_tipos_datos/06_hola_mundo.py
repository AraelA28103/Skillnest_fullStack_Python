""" 
- Imprime en pantalla el texto Hola, mundo usando una sola línea de código.
"""
print("Hola")



"""
- Declara una variable nombre con tu nombre o apodo.
- Imprime la frase Hola, <tu nombre> de dos maneras distintas. Por una parte, usando la concatenación con comas y por otra la concatenación con el símbolo +.
- Ejecuta el archivo después de cada forma de concatenación para confirmar que funciona.
"""
nombre = "Arael"
print("Hola" + nombre)
print("Hola", nombre)



"""
- Declara una variable numero con tu número de la suerte.
- Imprime la frase Mi número de la suerte es el <numero>! de dos maneras distintas. Por una parte, usando la concatenación con comas y por otra la concatenación con el símbolo +.
- Observa que la segunda forma podría lanzar un error si intentas sumar un número con una cadena. Resuélvelo utilizando la conversión de tipo (por ejemplo: str(numero)).
"""
numSuerte = str(73)
print("Mi número de la suerte es el", numSuerte)
print("Mi número de la suerte es el" + numSuerte)



"""
- Declara dos variables llamadas comida1 y comida2 que representen tus comidas favoritas.
- Imprime la frase ¡Me encanta comer <comida1> y <comida2>! de dos maneras distintas. Por una parte, usando format() y por otra usando f-strings.
"""
comida1 = "Arroz con pollo al limon"
comida2 = "Fideos con crema"
print("¡Me encanta comer {} y {}!".format(comida1, comida2))
print(f"¡Me encanta comer {comida1} y {comida2}!")



# BONUS
"""
- Explora otros métodos de cadenas en Python. Por ejemplo, podrías usar upper(), lower(), replace(), o cualquier otro que te parezca interesante.
- Agrega un par de líneas de código extra en tu archivo hola_mundo.py para mostrar cómo funcionan.
"""
# Mayúscula y Minúscula
comidaMayus = comida1.upper()
comida2Minus = comida2.lower()
print(comidaMayus, comida2Minus)

# Reemplazo
comidaNueva = comida2.replace("crema", "salsa") # <-- Reemplaza la palabra "crema" por "salsa"
print(comidaNueva)