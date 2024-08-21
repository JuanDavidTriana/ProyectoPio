
'''Escribir un progrma aque imprima la tabla de multiplicar del 1 al 10'''

for i in range(0,11,2):
    print(f"La tabla de multiplicar del {i}")
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")
    print() #Separacion