import os

# ---------------------- Simulación de Base de Datos -----------------------

# Lista de productos disponibles en el e-commerce
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 3000000.00, "stock": 10},
    {"id": 2, "nombre": "Mouse", "precio": 150000.00, "stock": 20},
    {"id": 3, "nombre": "Teclado", "precio": 100000.00, "stock": 15},
    {"id": 4, "nombre": "Monitor", "precio": 600000.00, "stock": 5},
]

# Lista de cupones disponibles
cupones = [
    {"codigo": "COMPRAMAX100", "descuento": 15, "minimo": 100000, "limiteDeUso": 3}
]

# Lista de administradores
administradores = [
    {"usuario": "admin", "contrasena": "admin"},
    {"usuario": "Sebastian", "contrasena": "FD321"}
]

# ---------------------- Funciones Utilitarias -----------------------

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux o Mac

def mostrar_mensaje_error():
    input("Opción no válida. Presiona Enter para continuar...")
    limpiar_pantalla()

# ---------------------- Gestión de Productos -----------------------

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    nuevo_id = len(productos) + 1

    productos.append({"id": nuevo_id, "nombre": nombre, "precio": precio, "stock": stock})
    print(f"Producto '{nombre}' agregado con éxito.")

def eliminar_producto():
    mostrar_productos()
    producto_id = int(input("Ingrese el ID del producto que desea eliminar: "))
    
    for producto in productos:
        if producto["id"] == producto_id:
            productos.remove(producto)
            print(f"Producto '{producto['nombre']}' eliminado con éxito.")
            return
    
    print("Producto no encontrado.")

def actualizar_stock():
    mostrar_productos()
    producto_id = int(input("Ingrese el ID del producto cuyo stock desea actualizar: "))
    
    for producto in productos:
        if producto["id"] == producto_id:
            nuevo_stock = int(input(f"Ingrese el nuevo stock para '{producto['nombre']}': "))
            producto["stock"] = nuevo_stock
            print(f"Stock de '{producto['nombre']}' actualizado a {nuevo_stock}.")
            return
    
    print("Producto no encontrado.")

def mostrar_productos():
    print("\nProductos disponibles:")
    for producto in productos:
        print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")
    print("")

def administrar_productos():
    while True:
        print("------------ Administrador de Productos ------------")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Stock")
        print("4. Ver Productos")
        print("5. Salir")
        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            eliminar_producto()
        elif opcion == 3:
            actualizar_stock()
        elif opcion == 4:
            mostrar_productos()
        elif opcion == 5:
            break
        else:
            mostrar_mensaje_error()

# ---------------------- Gestión de Cupones -----------------------

def agregar_cupon():
    codigo = input("Ingrese el código del cupón: ")
    descuento = float(input("Ingrese el porcentaje de descuento: "))
    minimo = float(input("Ingrese el monto mínimo para aplicar el descuento: "))
    limite = int(input("Ingrese el límite de uso del cupón: "))

    cupones.append({"codigo": codigo, "descuento": descuento, "minimo": minimo, "limiteDeUso": limite})
    print(f"Cupón '{codigo}' agregado con éxito.")

def eliminar_cupon():
    mostrar_cupones()
    codigo = input("Ingrese el código del cupón que desea eliminar: ")
    
    for cupon in cupones:
        if cupon["codigo"] == codigo:
            cupones.remove(cupon)
            print(f"Cupón '{codigo}' eliminado con éxito.")
            return
    
    print("Cupón no encontrado.")

def mostrar_cupones():
    print("\nCupones disponibles:")
    for cupon in cupones:
        print(f"Código: {cupon['codigo']}, Descuento: {cupon['descuento']}%, Mínimo: {cupon['minimo']}, Límite de Uso: {cupon['limiteDeUso']}")
    print("")

def administrar_cupones():
    while True:
        print("------------ Administrador de Cupones ------------")
        print("1. Agregar Cupón")
        print("2. Eliminar Cupón")
        print("3. Ver Cupones")
        print("4. Salir")
        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            agregar_cupon()
        elif opcion == 2:
            eliminar_cupon()
        elif opcion == 3:
            mostrar_cupones()
        elif opcion == 4:
            break
        else:
            mostrar_mensaje_error()

# ---------------------- Función Principal -----------------------

def iniciar_sesion_administrador():
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")

    for admin in administradores:
        if admin["usuario"] == usuario and admin["contrasena"] == contrasena:
            return True
    return False

def main():
    limpiar_pantalla()
    while True:
        print("------------ E-Commerce ------------")
        print("1. Cliente")
        print("2. Administrador")
        print("3. Salir")
        opcion = int(input("Elija un usuario para iniciar la app: "))

        if opcion == 1:
            print("Función de cliente en desarrollo...")
        elif opcion == 2:
            limpiar_pantalla()
            if iniciar_sesion_administrador():
                while True:
                    print("------------ Menú Administrador ------------")
                    print("1. Administrar Productos")
                    print("2. Administrar Cupones")
                    print("3. Salir")
                    opcion_admin = int(input("Elija una opción: "))

                    if opcion_admin == 1:
                        administrar_productos()
                    elif opcion_admin == 2:
                        administrar_cupones()
                    elif opcion_admin == 3:
                        break
                    else:
                        mostrar_mensaje_error()
            else:
                print("Usuario o contraseña incorrectos.")
        elif opcion == 3:
            print("Saliendo...")
            break
        else:
            mostrar_mensaje_error()

# ---------------------- Ejecutar el Programa -----------------------

if __name__ == "__main__":
    main()
