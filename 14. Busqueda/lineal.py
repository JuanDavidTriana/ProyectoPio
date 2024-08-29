def busqueda_lineal(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    return "Dato no encontrado"


#Ejemplo lista
lista = [5,8,2,1,4,7,3,6,9]
x = 4
resultado = busqueda_lineal(lista,x)
print(f"Elementos encontrado en el indice: {resultado}")