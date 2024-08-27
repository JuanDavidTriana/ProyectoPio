from tabulate import tabulate

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas para mostrar.")
    else:
        headers = ["#", "Descripción", "Prioridad"]
        rows = [[i + 1, tarea["descripcion"], tarea["prioridad"]] for i, tarea in enumerate(sorted(tareas, key=lambda x: x["prioridad"]))]
        print(tabulate(rows, headers, tablefmt="grid"))

def gestionar_tareas():
    tareas = [{"descripcion":"Programar ciclos", "prioridad": 5},
            {"descripcion":"Programar condicinales", "prioridad": 10},
            {"descripcion":"Programar variables", "prioridad": 8}]

    while True:
        print("\nGestión de Tareas")
        print("1. Agregar Tarea")
        print("2. Mostrar Tareas")
        print("3. Eliminar Tarea")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            descripcion = input("Ingresa la descripción de la tarea: ")
            prioridad = int(input("Ingresa la prioridad de la tarea (1-10): "))
            tareas.append({"descripcion": descripcion, "prioridad": prioridad})
            print("Tarea agregada con éxito.")
        elif opcion == "2":
            mostrar_tareas(tareas)
        elif opcion == "3":
            mostrar_tareas(tareas)
            indice = int(input("Ingresa el número de la tarea a eliminar: ")) - 1
            if 0 <= indice < len(tareas):
                tareas.pop(indice)
                print("Tarea eliminada con éxito.")
            else:
                print("Índice inválido.")
        elif opcion == "4":
            print("Saliendo del gestor de tareas...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

gestionar_tareas()
