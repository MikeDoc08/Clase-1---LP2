# Ordenamiento de Listas:

# sorted(lista): Devuelve una nueva lista ordenada sin modificar la lista original.

numeros = [4, 2, 8, 1, 6]

def sorteD():
    numeros_ordenados = sorted(numeros)  # Resultado: [1, 2, 4, 6, 8]
    print(numeros_ordenados)

sorteD()


# lista.sort(): Ordena la lista original in-place, es decir, modifica la lista directamente.

def sorT():
    numeros.sort()
    # Resultado después de la ordenación in-place: [1, 2, 4, 6, 8]
    print(numeros)

sorT()


# Personalización del Ordenamiento:

def ordenamientoPersonalizado():
    palabras = ["perro", "gato", "elefante", "ratón"]
    palabras_ordenadas = sorted(palabras, key=len)  # Ordenar por longitud de palabra
    # Resultado: ["gato", "perro", "ratón", "elefante"]

    print(palabras_ordenadas)

ordenamientoPersonalizado()
