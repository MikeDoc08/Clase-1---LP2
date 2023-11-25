# Función recursiva para calcular el factorial de un número:

# Recursión: Cálculo del Factorial

def factorial(n):
    # Caso Base
    if n == 0 or n == 1:
        return 1
    # Caso Recursivo
    else:
        return n * factorial(n - 1)
    
print(factorial(4))


# 4!
# 4x3x2x1 = 24


# Iteración: Cálculo del Factorial

def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# print(factorial_iterativo(4))