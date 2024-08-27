import os

#----------------------Simulacion de bd-----------------------

#Productos disponibles en el e-commercer
productos = [
    {"nombre": "Laptop", "precio": 3000000.00, "stock": 10},
    {"nombre": "Mouse", "precio": 150000.00, "stock": 20},
    {"nombre": "Teclado", "precio": 100000.00, "stock": 15},
    {"nombre": "Monitor", "precio": 600000.00, "stock": 5},
]

#Carrito
carrito = []

#Cupon
cupones = [
    {"cupon": "COMPRAMAX100", "descuento": 15, "min": 100000, "limiteDeUso": 3}
]

#Administrador
administradores = [
    {"usuario": "admin", "contrasena": "admin"},
    {"usuario": "Sebastian", "contrasena": "FD321"}
]

#----------------------------------------------------------------
def limpiar_terminar():
    if os.name == 'nt': os.system('cls') #Windows
    else: os.system('clear') #Linux o Mac

def opcion_no_valida():
    input("Opcion no valida.... Enter para continuar")
    limpiar_terminar()

def mostrar_productos():
    pass

def cliente(nombre):

    def carrito():

        def mostrar():
            pass

        def agregar():
            pass

        def eliminar():
            pass

        def actualizar():
            pass

        def vaciar():
            pass

    def calcular_total():
        pass

    def procesar_compra():
        pass

def administrador(elemento,peticion):

    def productos():

        def agregar():
            pass

        def elimar():
            pass

        def actualizar():
            pass

    def cupones():
        def agregar():
            pass

        def elimar():
            pass

        def actualizar():
            pass

    if (elemento == "cupones" & peticion == "crear"):
        print("Crear Cupones")


def main():

    limpiar_terminar()
    while True:
        print("------------E-Commerce------------")
        print("1. Cliente")
        print("2. Administrador")
        print("3. Salir")
        opcion = int(input("Elija un usuario para iniciar el app: "))
        
        if opcion == 1:
            pass
        elif opcion == 2:
            limpiar_terminar() #Limpiar Terminar
            print("------------Administrador------------")
            sesion = False
            usuario = input("Nombre de usuario: ")
            contrasena = input("Contraseña: ")

            for administrador in administradores: #Recorremos la lista de adminstradores
                if (usuario in administrador["usuario"]) & (contrasena in administrador["contrasena"]):
                    sesion = True
                    limpiar_terminar()
                
            if sesion:
                print(f"------------Administrador {usuario}------------")
                print("1. Productos")
                print("2. Cupones")
                print("3. Salir")
                opcion = int(input(f"Elija una opcion para trabajar: "))

                if opcion == 1:
                    pass
                elif opcion == 2:
                    print(f"------------Administrador cupones {usuario}------------")
                    print("1. Crear un cupon")
                    print("2. Actulizar")
                    print("3. Eliminar")
                    opcion = int(input(f"Elija una opcion para trabajar: "))

                    if opcion == 1:
                        administrador("cupones","crear")   

                elif opcion == 3:
                    print("Saliente")
                    break
                else: opcion_no_valida()
                    

                
            if sesion == False: print("Nombre o contraseña no validos...")
        

        elif opcion == 3:
            print("Saliendo.......")
            break
        else: opcion_no_valida()

main()
