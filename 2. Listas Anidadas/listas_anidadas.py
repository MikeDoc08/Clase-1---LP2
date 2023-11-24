
# Lista Anidada

lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def anidada():
    # Lista anidada
    print(lista_anidada)

anidada()


# Acceso y Manipulación de Elementos en Listas Anidadas

def acceso():
    # Acceder a un elemento en la fila 2, columna 3
    elemento = lista_anidada[1][2]  # Resultado: 6
    print(elemento)

# acceso()

def manipulacion():
    # Modificar un elemento en la fila 3, columna 1
    lista_anidada[2][0] = 10
    # Resultado después de la modificación: [[1, 2, 3], [4, 5, 6], [10, 8, 9]]
    print(lista_anidada)

# manipulacion()



