'''Mini Proyecto: Gestor de Tareas
Objetivo:
Crear una aplicación de consola que permita al usuario gestionar una lista de tareas. 
El usuario podrá añadir tareas, ver la lista de tareas, ordenarlas por prioridad, y eliminar tareas completadas.
Funcionalidades:
Añadir Tarea: Permite al usuario añadir una nueva tarea con una #!descripción y una prioridad.
Mostrar Tareas: Muestra todas las tareas actuales.
Ordenar Tareas: Ordena las tareas por su prioridad.
Eliminar Tarea: Permite al usuario eliminar una tarea completada.
Estructura del Proyecto:
La lista de tareas será una lista de #!diccionarios
, donde cada diccionario representará una tarea con una descripción 
y una prioridad.
'''

def agregar_tarea(tareas):
    print("-----------------------Agregar tarea-----------------------")
    descripcion = input("Ingresa la descripcion de la tarea: ")
    prioridad = int(input("Ingrese la prioridad de la tarea(1-10):"))
    tarea = {"descripcion":descripcion, "prioridad": prioridad}
    tareas.append(tarea)
    print("Tarea agregada con exito")

def mostar_tareas(tareas):
    if len(tareas) == 0:
        print("No hay tareas para mostar.")
    else:
        tareas.sort(key=lambda x: x["prioridad"])
        i = 1
        for tarea in tareas:
            print(f"{i}. Tarea: {tarea['descripcion']} - Prioridad: {tarea['prioridad']}")
            i += 1

def ordenar_tareas(tareas):
    tareas.sort(key=lambda x: x["prioridad"])
    print("Tarea ordenada por prioridad")

def eliminar_tareas(tareas):
    pass

def menu():

    tareas = [{"descripcion":"Programar ciclos", "prioridad": 5},
            {"descripcion":"Programar condicinales", "prioridad": 10},
            {"descripcion":"Programar variables", "prioridad": 8}]

    while True:
        print("Gestion de Tareas")
        print("1. Agegar Tarea")
        print("2. Mostrar Tarea")
        print("3. Ordenar Tarea por prioridad")
        print("4. Eliminar Tarea")
        print("5. Salir")
        opcion = input("Eliga una Opcion: ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            mostar_tareas(tareas)
        elif opcion == "3":
            ordenar_tareas(tareas)
        elif opcion == "4":
            pass
        elif opcion == "5":
            print("Saliendo del gestor de tareas....")
            break
        else:
            print("Opcion invalida. Intenta de nuevo")

menu()