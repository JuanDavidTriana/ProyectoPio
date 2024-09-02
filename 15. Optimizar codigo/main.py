import os

productos = [
    {"nombre": "Laptop", "precio": 3000000.00, "stock": 10},
    {"nombre": "Mouse", "precio": 150000.00, "stock": 20},
    {"nombre": "Teclado", "precio": 100000.00, "stock": 15},
    {"nombre": "Monitor", "precio": 600000.00, "stock": 5},
]

carrito = []

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux o Mac

def annadir_productos_carrito(nombre_producto, cantidad):
    limpiar_pantalla()
    producto = next((p for p in productos if p["nombre"] == nombre_producto), None)

    if producto:
        if producto["stock"] >= cantidad:
            
            item_carrito = next((c for c in carrito if c["nombre"] == nombre_producto), None)

            if item_carrito:
                item_carrito['cantidad'] += cantidad
            else:
                carrito.append({"nombre": nombre_producto, "cantidad": cantidad})
                producto['stock'] -= cantidad

            print("Producto añadido al carrito con exito...")
        else:
            input(f"No hay suficientes stock para el producto {nombre_producto}. enter para continuar....")
    else:
        input(f"El producto {nombre_producto} no existe. enter para continuar....")


    input(carrito)

    limpiar_pantalla()

def quitar_producto_carrito():
    pass

def vaciar_carrito():
    pass

def comprar_productos():
    pass

def main():
    while True:
        limpiar_pantalla()
        print("--------------------- Menu E-Commerce ---------------------")
        print("Opciones: ")
        print("1. Añadir producto al carrito")
        print("2. Quitar productos del carrtio")
        print("3. Vaciar carrito")
        print("4. Comprar productos")
        print("5. salir")

        try:
            opcion = int(input("Elije una opcion: "))

            if opcion == 1:
                limpiar_pantalla()
                print("--------------------- Agregar producto al carrito ---------------------")
                nombre = input("nombre del producto: ")
                cantidad = int(input("Ingrese cantidad: "))
                annadir_productos_carrito(nombre,cantidad)
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                print("Saliendo de la tienda.....")
                break
            else:
                input("Opcion no valida, precion enter para continuar...")
        except ValueError:
            input("Error...Ingrese un numero...")
main()