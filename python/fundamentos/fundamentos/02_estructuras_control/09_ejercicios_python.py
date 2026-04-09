# 1. Números Pares Dinámicos
def paresDinamicos():
    pares = int(input("Cuantos números pares desea ver? "))
    for i in range(1, pares + 1):
        print(i * 2)



# 2. Verificador de Edad y Acceso
def verificadorEdad():
    anioNAcimiento = int(input("Anio de nacimiento: "))
    calculoEdad = 2026 - anioNAcimiento
    if calculoEdad >= 18:
        print(f"Eres mayor de edad, tienes {calculoEdad} anios")
    elif calculoEdad < 18:
        print(f"Eres menor de edad, tienes {calculoEdad} anios")
    else:
        print("Error")



# 3. Calculadora de Descuentos
def calculadoraDescuentos():
    precioProducto = int(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad de unidades compradas: "))
    total = precioProducto * cantidad
    descuento = 0
    final = 0
    if (total > 100):
        descuento = total * (10 / 100)
        final = total - descuento
        print(f"Total: {total}\nDescuento: {descuento}\nFinal: {final}")



# 4. Clasificador de Números
def clasificadorNum():
    num = int(input("Ingrese un número: "))
    if (num > 0):
        if (num % 2 == 0):
            print(f"El número {num} es Positivo y Par")
        elif (num % 2 == 1):
            print(f"El número {num} es Positivo e Impar")
    elif (num < 0):
        if (num % 2 == 0):
            print(f"El número {num} es Negativo y Par")
        elif (num % 2 == 1):
            print(f"El número {num} es Negativo e Impar")



# 5. Tabla de Multiplicar Personalizada
def tablaPresonalizada():
    num = int(input("Ingresa un número: "))
    for i in range(1, 13):
        resultado = num * i
        if (resultado % 3 == 0):
            print(f"{num} * {i} = {resultado}")



# 6. Sumatoria con Centinela
def sumatoriaCentinela():
    num = int(input("Ingresa un número: "))
    suma = 0
    while num != 0:
        suma += num
        num = int(input("Ingresa un número negativo para terminar"))
    print(f"Total: {suma}")


# 7. Contador de Vocales
def contadorVocales():
    palabra = input("Ingresa una palabra: ")



# 8. Validación de Contraseña



# 9. Registro de Nombres



# 10. Promedio de Notas



# 11. Filtro de Arreglos



# 12. Buscador de Elementos



# 13. Simulación de Inventario



# 14. Generador de Lista de Compras



# 15. Análisis de Temperaturas



continuar = True
while continuar:
    print("\n---Ejercicios Python---")
    print("---Ejercicio 1---")
    print("---Ejercicio 2---")
    print("---Ejercicio 3---")
    print("---Ejercicio 4---")
    print("---Ejercicio 5---")
    print("---Ejercicio 6---")
    print("---Ejercicio 7---")
    print("---Ejercicio 8---")
    print("---Ejercicio 9---")
    print("---Ejercicio 10---")
    print("---Ejercicio 11---")
    print("---Ejercicio 12---")
    print("---Ejercicio 13---")
    print("---Ejercicio 14---")
    print("---Ejercicio 15---")
    opcion = input("\n---Elije una opción: (1-15) (0 para salir)")
    if opcion == "1":
        print("\nEjecutar ejercicio 1: ")
        print(paresDinamicos())
    elif opcion == "2":
        print("\nEjecutar ejercicio 2: ")
        print(verificadorEdad())
    elif opcion == "3":
        print("\nEjecutar ejercicio 3: ")
        print(calculadoraDescuentos())
    elif opcion == "4":
        print("\nEjecutar ejercicio 4: ")
        print(clasificadorNum())
    elif opcion == "5":
        print("\nEjecutar ejercicio 5: ")
        print(tablaPresonalizada())
    elif opcion == "6":
        print("\nEjecutar ejercicio 5: ")
        print(sumatoriaCentinela())
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no válido. Intenta otra vez.")