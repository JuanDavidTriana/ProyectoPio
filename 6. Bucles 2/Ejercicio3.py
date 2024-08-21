'''Escribir un programa que siga pidiendo al usuario que ingrese
una contraseñas hasta que coincida con una contraseña predefinida'''

#Contraseña predefinida
contrasena = 'HolaProgramadores'

#Número maximo de intentos permitidos
intentos_max = 4

# Contador intentos
intentos = 0

#Bucle para pedir la contraseña 
while intentos < intentos_max:
    
    intentoContrasena = input("Ingrese contraseña: ")

    if intentoContrasena == contrasena:
        print("Contraseña correcta.")
        break #Salir bucle
    else:
        intentos += 1
        intentos_restantes = intentos_max - intentos

        if intentos_restantes > 0:
            print(f"Contraseña incorrecta, te quedan {intentos_restantes} intentos")
        else:
            print("Has superado el número maximo de intentos")
            break #Salir bucle