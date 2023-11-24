# Funciones de Listas:

# len(lista): Devuelve la longitud de la lista.
# sum(lista): Devuelve la suma de los elementos de la lista.
# max(lista): Devuelve el elemento máximo de la lista.
# min(lista): Devuelve el elemento mínimo de la lista.

# Ejemplo: Encontrar la suma y el promedio de una lista de números

numeros = [10, 20, 30, 40, 50]

def sumaTotal():
    suma_total = sum(numeros)          # Resultado: 150
    return suma_total

# print(sumaTotal())

def longd():
    longitud = len(numeros)             # Resultado: 5
    return longitud

# print(longd())

def prom():
    promedio = sumaTotal() / longd()    # Resultado: 30.0
    print(promedio)

# prom()


# Ejemplo: Encontrar el elemento máximo y mínimo en una lista de temperaturas

temperaturas = [23, 19, 25, 18, 27]

def tempMax():
    temperatura_maxima = max(temperaturas)  # Resultado: 27
    print(temperatura_maxima)

# tempMax()

def tempMin():
    temperatura_minima = min(temperaturas)  # Resultado: 18
    print(temperatura_minima)

# tempMin()