
# Crear una Lista:

mi_lista = [1, 2, 3, 4, 5]

def crearLista():
    print(mi_lista)

crearLista()


# Acceder a Elementos por Índice:

def accederElemento():
    primer_elemento = mi_lista[0]  # Accede al primer elemento
    ultimo_elemento = mi_lista[-1]  # Accede al último elemento

    print(f"Primer elemento : {primer_elemento} - Ultimo elemento : {ultimo_elemento} ")

# accederElemento()


#  Modificar Elementos:

def modificarElementoIndice():
    mi_lista[1] = 10  # Modifica el segundo elemento de la lista
    print(mi_lista)

# modificarElementoIndice()


# Añadir Elementos al Final:

def añadirFinal():
    mi_lista.append(6)  # Añade el número 6 al final de la lista
    print(mi_lista)

# añadirFinal()


# Insertar Elementos en una Posición Específica:

def insertElementPosicion():
    mi_lista.insert(2, 8)  # Inserta el número 8 en la posición 2
    print(mi_lista)

# insertElementPosicion()


# Eliminar Elementos por Valor:

def eliminarElementoValor():
    mi_lista.remove(4)  # Elimina el primer elemento con el valor 4
    print(mi_lista)

# eliminarElementoValor()


# Eliminar Elementos por Índice:

def eliminarElementoIndice():
    elemento_eliminado = mi_lista.pop(2)  # Elimina y devuelve el elemento en la posición 3
    print(elemento_eliminado)
    print(mi_lista)

# eliminarElementoIndice()


# Longitud de la Lista:

def longitud():
    longitud = len(mi_lista)  # Devuelve la cantidad de elementos en la lista
    print(longitud)

# longitud()


# Operaciones con Listas:

def operacionesListas():
    otra_lista = [7, 8, 9]
    concatenacion = mi_lista + otra_lista  # Concatena dos listas
    repetir_lista = mi_lista * 2  # Repite la lista dos veces
    print(concatenacion)
    print(repetir_lista)

# operacionesListas()


def extender():
    mi_lista.extend([80, 90, 100])

    print(mi_lista)

extender()