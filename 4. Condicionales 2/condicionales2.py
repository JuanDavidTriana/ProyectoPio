'''Vamos a crear un app que nos va a preguntar la edad del usuario en el caso que 
el usuario sea mayor de edad y cuente con licencia de conducir le va a mostrar un mensaje
que le informe que puede conducir, en el caso que sea mayor de edad pero no tenga 
licencia le motrarar que no conducir por que no tiene licencia y en el caso que sea
menor de edad le informara que no puede conducir por este motivo'''

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    
    tiene_licencia = input("¿Tiene licencia de conducir?: ").lower()

    if tiene_licencia == "si":
        print("Puede Conducir")
    else:
        print("No puede conducir sin licencia")
else:
    print("Eres menor de edad, no puedes conducir")