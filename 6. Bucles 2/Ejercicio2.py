'''Crear un programa que pida número al usuario y los sume. 
El programa termina cuando el usuario ingrese un 0'''

suma = 0
num = int(input("Ingrese un número (ingrese 0 para salir): "))

while num != 0: 
    suma += num
    num = int(input("Ingrese otro número: "))

print(f"La suma de los números ingresados es {suma}")