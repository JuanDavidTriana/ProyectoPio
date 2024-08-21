ingresos = float(input("Ingresa tus ingresos en COP: "))

if ingresos > 0:
    if ingresos < 100000:
        impuesto = ingresos * 0.05
    elif 100000 <= ingresos < 200000:
        impuesto = ingresos * 0.15
    elif 200000 <= ingresos < 350000:
        impuesto = ingresos * 0.20
    elif 350000 <= ingresos < 600000:
        impuesto = ingresos * 0.30
    else:
        impuesto = ingresos * 0.45
    #Opcion 1
    print(f"El impuesto que debes pagar es de: {impuesto} COP")
    #Opcion 2
    print("El impuesto que debes pagar es de:", impuesto, "COP")
else:
    print("Ingresesos no validos")