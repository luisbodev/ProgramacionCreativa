# Dado un número que representa un mes (así 1 es enero, 2 es febrero, etc.) hacer
# una aplicación web que escriba si el mes pertenece a la primera parte del año
# o a la segunda.

mes = int(input("Ingrese número del mes: "))

if mes <= 6 :
    print("El mes pertenece a la primera parte del año")
else:
    print("El mes pertenece a la segunda parte del año")
