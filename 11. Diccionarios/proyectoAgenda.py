import os
from tabulate import tabulate

def limpiar_terminal():
    """Limpia la terminal para sistemas Unix y Windows."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Muestra el menú principal de opciones."""
    menu = (
        "\n1. Añadir contacto",
        "2. Eliminar contacto",
        "3. Buscar contacto",
        "4. Mostrar todos los contactos",
        "5. Salir"
    )
    print("\n".join(menu))

def gestionar_contacto(contactos, accion):
    """Gestiona la adición, eliminación o búsqueda de contactos."""
    limpiar_terminal()
    nombre = input("Nombre del contacto: ").strip().title()
    
    if accion == "añadir":
        if nombre in contactos:
            print(f"El contacto {nombre} ya existe.")
        else:
            telefono = input("Número de teléfono: ").strip()
            email = input("Correo electrónico: ").strip()
            contactos[nombre] = {"teléfono": telefono, "email": email}
            print(f"Contacto {nombre} añadido.")
    
    elif accion == "eliminar":
        if nombre in contactos:
            confirmacion = input(f"¿Estás seguro de que deseas eliminar el contacto {nombre}? (s/n): ").strip().lower()
            if confirmacion == 's':
                contactos.pop(nombre)
                print(f"Contacto {nombre} eliminado.")
            else:
                print("Eliminación cancelada.")
        else:
            print("Contacto no encontrado.")
    
    elif accion == "buscar":
        contacto = contactos.get(nombre)
        if contacto:
            print(f"Nombre: {nombre}\nTeléfono: {contacto['teléfono']}\nEmail: {contacto['email']}")
        else:
            print("Contacto no encontrado.")
    
    input("\nPresiona Enter para continuar...")

def mostrar_contactos(contactos):
    """Muestra todos los contactos almacenados."""
    limpiar_terminal()
    if contactos:
        tabla = [[nombre, info['teléfono'], info['email']] for nombre, info in contactos.items()]
        headers = ["Nombre", "Teléfono", "Email"]
        print(tabulate(tabla, headers=headers, tablefmt='grid'))
    else:
        print("No hay contactos en la agenda.")
    
    input("\nPresiona Enter para continuar...")

def main():
    """Función principal que ejecuta el programa."""
    contactos = {
        "Alice Johnson": {"teléfono": "123-456-7890", "email": "alice@example.com"},
        "Bob Smith": {"teléfono": "234-567-8901", "email": "bob@example.com"},
        "Carol Williams": {"teléfono": "345-678-9012", "email": "carol@example.com"},
        "David Brown": {"teléfono": "456-789-0123", "email": "david@example.com"},
        "Emma Davis": {"teléfono": "567-890-1234", "email": "emma@example.com"},
        "Frank Miller": {"teléfono": "678-901-2345", "email": "frank@example.com"},
        "Grace Wilson": {"teléfono": "789-012-3456", "email": "grace@example.com"},
        "Hannah Moore": {"teléfono": "890-123-4567", "email": "hannah@example.com"},
        "Ian Taylor": {"teléfono": "901-234-5678", "email": "ian@example.com"},
        "Jack White": {"teléfono": "012-345-6789", "email": "jack@example.com"}
    }
    
    acciones = {
        "1": ("añadir", gestionar_contacto),
        "2": ("eliminar", gestionar_contacto),
        "3": ("buscar", gestionar_contacto),
        "4": ("mostrar", mostrar_contactos)
    }
    
    while True:
        limpiar_terminal()
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "5":
            print("Saliendo del programa.")
            break
        elif opcion in acciones:
            if opcion == "4":
                acciones[opcion][1](contactos)
            else:
                acciones[opcion][1](contactos, acciones[opcion][0])
        else:
            print("Opción no válida. Por favor, elige una opción válida.")
            input("\nPresiona Enter para continuar...")


main()
