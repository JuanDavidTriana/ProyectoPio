def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else: 
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote] 
        mayores = [x for x in lista[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

#Ejemplo lista
lista = [5,8,2,1,4,7,3,6,9]
lista_ordenada = quick_sort(lista)
print(f"Lista Ordenada con el metodo rapido: {lista_ordenada}")