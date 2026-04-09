# 1. Números Pares Dinámicos
def paresDinamicos():
    pares = int(input("Cuantos números pares desea ver? "))
    for i in range(1, pares + 1):
        print(i * 2)
paresDinamicos()



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
verificadorEdad()


# 3. Calculadora de Descuentos
def calculadoraDescuentos():
    precioProducto = int(input("Ingrese el precio del producto: "))
    cantidadComprada = int(input("Ingrese la cantidad de unidades compradas: "))
    precioTotal = precioProducto * cantidadComprada
    if (precioTotal > 100):
        print()
calculadoraDescuentos()


# 4. Clasificador de Números



# 5. Tabla de Multiplicar Personalizada



# 6. Sumatoria con Centinela



# 7. Contador de Vocales



# 8. Validación de Contraseña



# 9. Registro de Nombres



# 10. Promedio de Notas



# 11. Filtro de Arreglos



# 12. Buscador de Elementos



# 13. Simulación de Inventario



# 14. Generador de Lista de Compras



# 15. Análisis de Temperaturas