while True:

    a = float(input("Ingrese primer número: "))
    b = float(input("Ingrese segundo número: "))

    if(a == b):
        print("Números no validos, los números tiene que ser diferentes")
    else:
        if a > b:
            print("A es mayor")
        else:
            print("B es mayor")
        
        break

