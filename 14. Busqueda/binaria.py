def busqueda_binaria(lista, x):
    inicio = 0
    fin = len(lista) - 1 

    while inicio <= fin:

        mitad = inicio + (fin - inicio) // 2

        if lista[mitad] == x:
            return mitad
        elif lista[mitad] < x:
            inicio = mitad + 1
        else:
            fin = mitad -1

    return "Dato no encontrado"

#Ejemplo lista
lista = [1,2,3,4,5,6,7,8,9,10]
x = 9
resultado = busqueda_binaria(lista,x)
print(f"Elementos encontrado en el indice: {resultado}")