def burbuja(lista):
    n = len(lista) # Tamaño de nuestra lista
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1]  = lista[j+1], lista[j] 

#Ejemplo lista
lista = [5,8,2,1,4,7,3,6,9]
burbuja(lista)
print(f"Lista Ordenada con el metodo burbuja: {lista}")