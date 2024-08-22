a = 0
b = 0
Temporal = 0

while a==b:
    print("Digite dos números diferentes")
    a = float(input("Ingrese primer número: "))
    b = float(input("Ingrese segundo número: "))

if a < b:
    Temporal = b
    b = a
    a = Temporal

print(f"a:{a}, b:{b}")
