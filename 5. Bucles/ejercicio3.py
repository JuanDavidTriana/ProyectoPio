'''Escribir un programa que cuente cuántas vocales 
hay en una palabra ingresada por el usarios'''

palabra = input("Ingrese una palabra:").lower()
vocales = "aeiou"
numeros = "1234567890"
carateres = "°!#$%&/()=?¡¨[]:_;*+-"
contador = 0
esValido = False

for letra in palabra:

    if (letra in numeros or letra in carateres):
        esValido = True
        break
        
    if letra in vocales:
        #print(f"Vocal: {letra}")
        contador += 1

if esValido: # lo mismo que poner (esValido == True)
    print("Error, la palabra no es valida por que tiene números o caraterestes")
else:
    print(f"El número de vocales en la palabra {palabra}, es {contador}")