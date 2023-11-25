# Sintaxis y Ejemplos de Uso:

def sintaxis():
    # Sintaxis básica
    # nueva_lista = [expresion for elemento in iterable if condicion]

    # Ejemplo: Crear una lista de cuadrados de los números del 0 al 9
    cuadrados = [x**2 for x in range(10)]  # Resultado: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    print(cuadrados)

# sintaxis()

def sintaxisCondicional():
    # Ejemplo: Obtener los cuadrados de los números pares del 0 al 9
    cuadrados_pares = [x**2 for x in range(10) if x % 2 == 0]  # Resultado: [0, 4, 16, 36, 64]
    print(cuadrados_pares)

sintaxisCondicional()