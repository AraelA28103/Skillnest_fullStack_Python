# Actividad: Gestor de inventario

"""
1. Creación: Crear una lista llamada inventario que contenga los siguientes artículos:
    - Laptop
    - Ratón
    - Monitor
    - Cable HDMI
"""
inventario = ["Laptop", "Ratón", "Monitor", "Cable HDMI"]
print(inventario)

""" 2. Expansión: Utiliza el método correspondiente para agregar "Impresora" y "Teclado" al final de la lista. """
inventario.append("Impresora")
inventario.append("Teclado")
print(inventario)

""" 3. Conteo: Utiliza la función integrada para mostrar cuantos elementos totales hay en la lista. """
print(len(inventario))
print(inventario)

""" 4. Acceso y Modificación: Modifica "Teclado" por "Teclado mecánico". """
inventario[5] = "Teclado mecánico"

""" 5. Slicing: Crea una lista nueva llamada "Promoción", debe contener solo los 3 primeros elementos de la lista "Inventario". """
promocion = inventario[:3]
print(promocion)

""" 6. Mostrar la lista "Inventario" ordenado alfabeticamente. """
inventario.sort()
print(inventario)

""" 7. Elimina el último elemento de loa lista "Inventario" mostrando el elemento eliminado y la lista final. """
elemento_eliminado = inventario.pop()
print(elemento_eliminado)