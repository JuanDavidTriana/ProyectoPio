'''Escribe una función llamada invertir_cadena que reciba una 
cadena y devuelva la cadena invertida. No puedes usar el método '''
def invertir_cadena(cadena):
    invertida = ""
    for char in cadena:
        invertida = char + invertida
    return invertida
