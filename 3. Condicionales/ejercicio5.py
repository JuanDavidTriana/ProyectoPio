calificacion = float(input("Ingrese la calificación del estudiante (0-100): "))

if calificacion >= 0 and calificacion <=100:
    if calificacion >= 90:
        print("Tienes una 'A'.")
    elif calificacion >= 80:
        print("Tienes una 'B'.")
    elif calificacion >= 70:
        print("Tienes una 'C'.")
    elif calificacion >= 60:
        print("Tienes una 'D'.")
    else:
        print("Tienes una 'F'.")
else:
    print("Calificación no válida. Debe estar entre 0 y 100.")
