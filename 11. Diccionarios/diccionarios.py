#Definir
mi_diccionario = {
    "nombre"    :   "Juan",
    "edad"      :     26,
    "ciudad"    :   "Ibague"
}

#Acceso a los valores
print(mi_diccionario["ciudad"]) #Salir: Ibague

#Añadir o actulizar
mi_diccionario["Curso"] = "Programacion POO"  #Crear
mi_diccionario["nombre"] = "David" #Actualizar

#Eliminar un elemento
#del mi_diccionario["ciudad"]
#mi_diccionario.pop("nombre")

#Interar
for clave, valor in mi_diccionario.items():
    print(clave, valor)


