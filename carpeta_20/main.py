# Estudiante: corrige este código y haz un pull request con la versión corregida.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))
