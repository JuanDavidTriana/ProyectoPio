def funciones_externa(mensaje):
    print(f"Mensaje desde la función extrar: {mensaje}")

    def funcion_interna():
        print(f"Mensaje desde la función interna: {mensaje}")

    funcion_interna()
    

funciones_externa("Hola Mundo")