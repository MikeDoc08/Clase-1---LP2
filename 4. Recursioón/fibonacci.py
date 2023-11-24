# Fibonacci

def fibonacci(n):
    if n < 0:
        return "Error: el término de la secuencia no puede ser negativo."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_aux(n, 0, 1)

def fibonacci_aux(n, a, b):
    if n == 0:
        return a
    else:
        return fibonacci_aux(n - 1, b, a + b)

# Ejemplo de uso
resultado = fibonacci(5)
print(resultado)  # Resultado: 5 (término 5 de la secuencia de Fibonacci)


# En este ejemplo, fibonacci_aux es la función recursiva indirecta que realiza los cálculos de la secuencia de Fibonacci. La función principal fibonacci se encarga de manejar casos especiales y llamar a la función auxiliar con los valores iniciales. La recursión múltiple se logra al llamar a fibonacci_aux dentro de sí misma. Este enfoque puede ser útil en situaciones donde dividir la lógica entre dos funciones mejora la claridad y modularidad del código.