#Hola Mundo
nombre = str(input("Ingrese el nombre del estudiante: "))
nota1 = float(input(f"Ingrese la nota 1 del estudiante {nombre}: "))
nota2 = float(input(f"Ingrese la nota 2 del estudiante {nombre}: "))
nota3 = float(input(f"Ingrese la nota 3 del estudiante {nombre}: "))
#Promedio
promedio = (nota1 + nota2 + nota3) / 3

print("El promedio de " , nombre , " es de " , promedio)
print(f"El promedio de estudiante {nombre} de las notas 1({nota1}),2({nota2}) y 3({nota3}) es {promedio}")