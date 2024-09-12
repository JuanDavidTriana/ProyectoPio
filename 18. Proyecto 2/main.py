# Sistema de Gestión Administrativa de una Biblioteca

# Lista de libros en la biblioteca (predefinidos)
libros = [
    {
        "titulo": "Cien Años de Soledad",
        "autor": "Gabriel García Márquez",
        "isbn": "978-3-16-148410-0",
        "genero": "Ficción",
        "cantidad": 5
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "isbn": "978-1-23-456789-7",
        "genero": "Clásico",
        "cantidad": 3
    },
    {
        "titulo": "La Odisea",
        "autor": "Homero",
        "isbn": "978-0-12-345678-9",
        "genero": "Épico",
        "cantidad": 4
    }
]

#Lista usuario
usuarios = []

#Funcion para agregar un libro al invetario
def agregar_libro():
    print("---------- Agregar libro ----------")
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")
    isbn = input("Ingrese el ISBN del libro: ")
    genero = input("Ingrese el genero del libro: ")
    cantidad = int(input("Ingrese el cantidad de libros disponibles: "))

    nuevoLibro = {
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "genero": genero,
        "cantidad": cantidad
    }

    libros.append(nuevoLibro)
    print(f"Libro {titulo} agregado al inventario")

#Funcion para editar un libro del inventario
def editar_libro():
    print("---------- Editar libro ----------")
    mostrar_libros()
    isbn = input("Ingrese el ISBN del libro que desea editar: ")
    for libro in libros:
        if libro["isbn"] == isbn:
            libro['titulo'] = input(f"Ingrese el nuevo titulo({libro['titulo']}): ")
            libro['autor'] = input(f"Ingrese el nuevo autor({libro['autor']}): ")
            libro['genero'] = input(f"Ingrese el nuevo genero({libro['genero']}): ")
            libro['cantidad'] = int(input(f"Ingrese el nueva cantidad({libro['cantidad']}): "))
            print(f"El libro con el ISBN: {isbn} ha sido actulizado")
            print(f"{libro["titulo"]} - {libro["autor"]} - ISBN: {libro["isbn"]} - {libro["genero"]} - {libro["cantidad"]}")

#Funcion para eliminar un libro del inventario
def eliminar_libro():
    print("---------- Elimiando libro ----------")
    mostrar_libros()
    isbn = input("Ingrese el ISBN del libro que desea eliminar: ")
    global libros
    libros = [libro for libro in libros if libro['isbn'] != isbn]
    print(f"El libro con el ISBN: {isbn} ha sido eliminado")

#Funsion para mostrar todos los libros del inventario
def mostrar_libros():
    if libros:
        print("Lista de libros en la biblioteca")
        for libro in libros:
            print(f"{libro["titulo"]} - {libro["autor"]} - ISBN: {libro["isbn"]} - {libro["genero"]} - {libro["cantidad"]}")
    else:
        print("No hay libros en el inventario")

#Funcion para agregar un usuario 
def agregar_usuario():
    print("---------- Agregar usuario ----------")
    nombre = input("Ingrese el nombre del usuario: ")
    usuario_id = input("Ingrese el id del usuario: ")

    nuevoUsuario = {
        "nombre": nombre,
        "usuario_id": usuario_id,
        "prestamo": []
    }

    usuarios.append(nuevoUsuario)
    print(f"Usuaruio {nombre} agregado con exito")

#Funcion para editar un usuario 
def editar_usuario():
    print("---------- Editar usuario ----------")
    mostrar_usuario()
    usuario_id = input("Ingrese el id del usuario que desea editar: ")
    for usuario in usuarios:
        if usuario["usuario_id"] == usuario_id:
            usuario['nombre'] = input(f"Ingrese el nuevo nombre del usuario({usuario['nombre']}): ")
            print(f"Usuaruio {usuario_id} editado con exito")

#Funcion para eliminar un usuario
def eliminar_usuario():
    print("---------- Elimiando usuario ----------")
    mostrar_usuario()
    usuario_id = input("Ingrese el id del usuario que desea eliminar: ")
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['usuario_id'] != usuario_id]
    print(f"El usuario con el id: {usuario_id} ha sido eliminado")

#Funcion para mostrar todos los usuario
def mostrar_usuario():
    if usuarios:
        print("Lista de usuarios")
        for usuario in usuarios:
            print(f"{usuario["usuario_id"]} - {usuario["nombre"]}  ")
    else:
        print("No hay usuarios registrados")


#Funcion para registrar el prestamo de un libro
def registrar_prestamo():
    mostrar_libros()
    isbn = input("Ingrese el ISBN del libro que desea prestar: ")
    libro = next((libro for libro in libros if libro['isbn'] == isbn), None)

    if libro and libro['cantidad'] > 0:
        mostrar_usuario()
        usuario_id = input("Ingrese el ID del usuario: ")
        usuario = next((usuario for usuario in usuarios if usuario['usuario_id'] == usuario_id), None)

        if usuario:
            libro["cantidad"] -= 1
            usuario['prestamo'].append(libro["titulo"])
            print(f"Prestamo registrado {libro["titulo"]} al usuario {usuario['nombre']} con el id {usuario['usuario_id']}")
        else:
            print("Usuario no encontrado")
    else:
        print("Libro no disponible o encontrado")


#Funcion para registrar el devuolucion de un libro
def registrar_devolucion():
    mostrar_usuario()
    usuario_id = input("Ingrese el ID del usuario que devuevle el libro: ")
    usuario = next((usuario for usuario in usuarios if usuario['usuario_id'] == usuario_id), None)

    if usuario and usuario['prestamos']:
        print(f"Libro prestados por {usuario['nombre']}")
        for idx, libro in enumerate(usuario["prestamo", 1]):
            print(f"{idx}. {libro}")
        opcion = int(input("Seleccione el numero de libro que sea devolver"))

        if 1 <= opcion <= len(usuario["prestamo"]):
            libro_devuelto = usuario['prestamo'].pop(opcion - 1)
            libro = next((libro for libro in libros if libro['titulo'] == libro_devuelto), None)
            if libro:
                libro['cantidad'] += 1
            print(f"Libro {libro_devuelto}, devuelto con extio")
        else:
            print("Opcion no valida")
    else:
        print("Usuario no encontrado o no tiene libros prestados")


#Funcion para informe de libros prestados
def informe_prestamos():
    print("Inform de libros prestados: ")
    for usuario in usuarios:
        pass


#Funcion principal del menu
def menu():
    while True:
        print("----- Menu -----")
        print("1. Agregar libro")
        print("2. Editar libro")
        print("3. Eliminar libro")
        print("4. Mostar libros")
        print("5. Agregar usuario")
        print("6. Editar usuario")
        print("7. Eliminar usuario")
        print("8. Mostar usuarios")
        print("9. Registar prestamo de libro")
        print("10. Devolver libro")

        print("0. Finalizar")

        opcion = int(input("Selecciona una opcion: "))

        if opcion == 1:
            agregar_libro()
        elif opcion == 2:
            editar_libro()
        elif opcion == 3:
            eliminar_libro()
        elif opcion == 4:
            mostrar_libros()
        elif opcion == 5:
            agregar_usuario()
        elif opcion == 6:
            editar_usuario()
        elif opcion == 7:
            eliminar_usuario()
        elif opcion == 8:
            mostrar_usuario()
        elif opcion == 9:
            registrar_prestamo()
        elif opcion == 10:
            registrar_devolucion()


        elif opcion == 0:
            break

menu()