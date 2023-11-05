# Escribir un programa que diga si un año es bisiesto según el calendario juliano.

year = int(input("Ingrese el año a comprobar: "))

if year % 4 :
    print("El año no es biciesto")
else:
    print("El año es biciesto")

