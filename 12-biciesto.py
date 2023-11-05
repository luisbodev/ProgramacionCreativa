year = int(input("Ingrese el año a comparar: "))

flag = year%4 == 0

print("¿El año es biciesto según calendario juliano?", flag)