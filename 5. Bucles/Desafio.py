"""Desafio: Crear un programa que deterine si un numero ingresado por el usuario es primo """

numero = int(input("Ingresa un numero: "))
primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        print(f"el numero {numero} no es un numero primo debido a que al dividirlo entre {i} su residuo dio 0")
        break

if primo:
    print(f"el numero {numero} es un numero primo")