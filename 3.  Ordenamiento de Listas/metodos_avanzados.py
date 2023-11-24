# Métodos Avanzados:

# count(valor): Devuelve el número de veces que aparece el valor en la lista.

def contador():
    frutas = ['manzana', 'plátano', 'manzana', 'naranja', 'manzana']
    conteo_manzanas = frutas.count('manzana')  # Resultado: 3
    print(conteo_manzanas)

contador()


# index(valor): Devuelve el índice del primer elemento con el valor especificado.

def indice():
    numeros = [10, 20, 30, 20, 40]
    indice_primera_vez_20 = numeros.index(20)  # Resultado: 1
    print(indice_primera_vez_20)

indice()