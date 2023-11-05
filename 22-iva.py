price = float(input("Ingrese el precio sin IVA: "))
type = input("Escribe el tipo de producto (Gravado o Exento): ")

final_price = price

if (type == 'Gravado') :
    final_price = final_price * 1.13

print("El precio final es: ", final_price)