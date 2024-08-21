'''Crear un programa que defina un número 1 al 100. El jugador
debe intentar adivinar el número, y el programa le indicará si esta
Caliente o Frio (Caliente 10 unidades o menos del número)'''

import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

print("¡Adivina el número entre 1 y 100!")

print(numero_secreto)

# Pedir el primer intento
intento = int(input("Ingrese su intento: "))

while intento != numero_secreto:
    # Comparar el intento con el número secreto directamente
    if intento > numero_secreto:
        diferencia = intento - numero_secreto
    else:
        diferencia = numero_secreto - intento

    if diferencia <= 10:
        print("Caliente")
    else:
        print("Frío")

    if intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

    # Pedir un nuevo intento
    intento = int(input("Inténtelo de nuevo: "))

print("¡Felicitaciones! Has adivinado el número.")
