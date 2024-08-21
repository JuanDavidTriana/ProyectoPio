'''Programa que pida un número y lo muestre el 
programa para cuando se ingrese un número negativo'''

num = int(input("Ingrese un número(Ingrese un número negativo para salir): "))

while num >= 0:
    print(f"El número es: {num}")
    num = int(input("Ingrese otro número: "))
