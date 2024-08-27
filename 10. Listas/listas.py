#Definiar varios tipos de diferentes datos
mi_lista = [10, "Hola", 3.14, True]

#Acceder a todos los elemento
print(mi_lista)

#!Operaciones basicas con listas
#Agregar datos a una lista(append)
mi_lista.append("Nicolas")
mi_lista.append("Sebastian")
print(mi_lista)

#Accedder a elementos
print(mi_lista[-1])

#Modificar 
mi_lista[3] = "Juan David"
print(mi_lista)

#Insertar
mi_lista.insert(2,"Evelyn")
print(mi_lista)

#Eliminar
mi_lista.remove(3.14)
mi_lista.remove(mi_lista[3])
print(mi_lista)

#Recorrecor una lista 
for datos in mi_lista:
    print(datos)

#Ordenar numeros
numeros = [5,2,8,4,6,7,9,1,3]
print(numeros, "Sin ordenar")
numeros.sort() #De menor a mayor
print(numeros, "Ordenados de menor a mayor")
numeros.sort(reverse=True)#De mayor a menor
print(numeros, "Ordenados de mayor a menor")

#Ordenar cadenas
nombres = ["Juan", "Ana", "Jose", "Sebastian","Alexandra"]
print(nombres, "Sin ordenar")
nombres.sort() #De menor a mayor
print(nombres, "Ordenados de menor a mayor")
nombres.sort(reverse=True)#De mayor a menor
print(nombres, "Ordenados de mayor a menor")
print(len(nombres))