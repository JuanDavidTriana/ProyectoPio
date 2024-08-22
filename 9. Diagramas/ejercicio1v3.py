def comparador(a,b):
    if(a == b):
        print("Error números igulaes, tienes que dijitar numeros diferes")
    else:
        if a > b:
            print("A es mayor")
        else:
            print("B es mayor")

def main():
    a,b = 0,0
    while a==b:
        a = float(input("Ingrese primer número: "))
        b = float(input("Ingrese segundo número: "))
        comparador(a,b)

main()