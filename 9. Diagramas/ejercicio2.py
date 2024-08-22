def ordenamientoDosNumeros(a,b):
    Temporal = b
    b = a
    a = Temporal
    mostrarOrdenamiento(a,b)

def mostrarOrdenamiento(a,b):
    print(f"a:{a}, b:{b}")

def main():
    a,b =0,0
    while a==b:
        print("Digite dos números diferentes")
        a = float(input("Ingrese primer número: "))
        b = float(input("Ingrese segundo número: "))
    ordenamientoDosNumeros(a,b)

main()