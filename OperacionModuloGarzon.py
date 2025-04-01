def calcular_modulo(dividendo, divisor):
    """
    Calcula el módulo (resto) de la división entre dos números.
    """
    return dividendo % divisor

# Ejemplo de uso
if __name__ == "__main__":
    dividendo = int(input("Introduce el dividendo: "))
    divisor = int(input("Introduce el divisor: "))
    
    resultado = calcular_modulo(dividendo, divisor)
    print(f"El módulo de {dividendo} dividido entre {divisor} es: {resultado}")