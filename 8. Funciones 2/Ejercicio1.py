'''Calculadora con Funciones Anidadas'''

def calculadora_avanzada(operacion, x, y):
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: División por cero"

    if operacion == 'sumar':
        return sumar(x, y)
    elif operacion == 'restar':
        return restar(x, y)
    elif operacion == 'multiplicar':
        return multiplicar(x, y)
    elif operacion == 'dividir':
        return dividir(x, y)
    else:
        return "Operación no válida"

# Ejemplo de uso
resultado = calculadora_avanzada('restar', 10, 5)
print("Resultado:", resultado)
