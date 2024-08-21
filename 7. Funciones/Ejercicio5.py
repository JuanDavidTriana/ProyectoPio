'''Programa de Calculadora'''

def suma(x,y):
    return x + y

def resta(x,y):
    return x - y

def multiplicacion(x,y):
    return x * y

def dividir(x,y):
    if y != 0:
        return x / y
    else:
        return "Error: Division por cero"
    
def opciones():
    print("Opciones: ")
    print("1. Suma")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def calculadora():
    opciones()
    while True:
        operacion = int(input("Digite la opcion de desea: "))
        if (operacion >= 1 and operacion <=5):
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            if operacion == 1:
                print("Suma")
                print(f"Resultado: {suma(num1,num2)}")
                print("#############################")
            elif operacion == 2:
                print("Resta")
                print(f"Resultado: {resta(num1,num2)}")
                print("#############################")
                opciones()
            elif operacion == 3:
                print("Multiplicar")
                print(f"Resultado: {multiplicacion(num1,num2)}")
                print("#############################")
                opciones()
            elif operacion == 4:
                print("Divicion")
                print(f"Resultado: {dividir(num1,num2)}")
                print("#############################")
                opciones()
            elif operacion == 5:
                print("Muchas Gracias... Saliendo....")
                break
        else:
            print("Opciones no valida....")
            print("#############################")
            opciones()
            

calculadora()