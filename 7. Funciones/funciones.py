#Funcion Simple
def saludar():
    print("Hola Soy un funciones")
saludar()

#Funcion con Parámetros
def saludar2(nombre:str):
    print(f"Hola {nombre}, Bienvenido a PIO")
saludar2('Juan')

#Funcion con Valores de Retorno
def suma(numero1:int, numero2:int):
    return numero1 + numero2
resultado = suma(3,4)
print(resultado)