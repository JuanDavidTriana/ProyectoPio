'''Vamos a crear programa que simule el juego de adivinar palabra'''

import random

#Lista de palabras para el juegos
palabras = ['python','scrum','programacion','metodologia']

def elegir_palabra(palabras:list):
    #Elegimos la palabra
    return random.choice(palabras)

def jugar_adivinar_palabra(palabra):
    intentos = 2
    print("!Bievenidos al juego de adivinar la palabra!")
    print(f"Tienes {intentos} intentos para adivinar la palabra.")
    while intentos > 0:
        intento = input("Adivina la palabra: ").lower()
        if intento == palabra:
            print(f"Felicidades, adivinaste la palabra")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"Incorrectos, te quedan intentos {intentos}")
            else:
                print(f"Te has quedado sin intentos. la palabra era {palabra}")

palabra = elegir_palabra(palabras)
jugar_adivinar_palabra(palabra)