def mostrar_menu():
    print("\n1. Añadir contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")

def añadir_contacto(contactos):
    nombre = input("Nombre del contacto: ")
    telefono = input("Número de teléfono: ")
    email = input("Correo electrónico: ")
    contactos[nombre] = {"teléfono": telefono, "email": email}
    print(f"Contacto {nombre} añadido.")

def eliminar_contacto(contactos):
    nombre = input("Nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print("Contacto no encontrado.")

def buscar_contacto(contactos):
    nombre = input("Nombre del contacto a buscar: ")
    if nombre in contactos:
        contacto = contactos[nombre]
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {contacto['teléfono']}")
        print(f"Email: {contacto['email']}")
    else:
        print("Contacto no encontrado.")

def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos en la agenda.")
    else:
        for nombre, info in contactos.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info['teléfono']}")
            print(f"Email: {info['email']}")
            print()

def main():
    contactos = {}
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            añadir_contacto(contactos)
        elif opcion == "2":
            eliminar_contacto(contactos)
        elif opcion == "3":
            buscar_contacto(contactos)
        elif opcion == "4":
            mostrar_contactos(contactos)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")
