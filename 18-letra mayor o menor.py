# Escribir un programa que pida una cadena y nos diga si la primera letra está
# antes en el alfabeto que la última letra
# Tendrá dos opciones:
# "La primera letra está antes en el alfabeto que la última letra"
# "La primera letra no está antes en el alfabeto que la última letra"


word = input("Ingrese una palabra: ")

first = word[0]
last = word[-1]

if first < last :
    print("La primera letra está antes en el alfabeto que la última letra")
else:
    print("La primera letra no está antes en el alfabeto que la última letra")