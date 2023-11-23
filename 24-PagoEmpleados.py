hours = int(input("Cantidad de horas: "))
hours_type = input("Tipo de horas (normal o extras): ")

hours_type = hours_type.lower().strip()



if (hours_type == "normal") :
    total_pago = hours * 10
    print("El total a pagar es", total_pago)
elif (hours_type == "extras") :
    total_pago = hours * 20
    print("El total a pagar es", total_pago)
else :
    print("Tipo de horas incorrecto")

    