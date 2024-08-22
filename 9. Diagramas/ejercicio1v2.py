def comparador(a,b):
    if(a == b):
        print("Error números igulaes, tienes que dijitar numeros diferes")
        return False
    else:
        if a > b:
            print("A es mayor")
            return True
        else:
            print("B es mayor")
            return True

def main():
    while True:
        a = float(input("Ingrese primer número: "))
        b = float(input("Ingrese segundo número: "))
        comparador(a,b)

main()