price = float(input("Ingrese el precio del producto: $"))
customer_type = input("Escribe el tipo de cliente (Normal o Preferencial): ")

price_with_discount = price * 0.8

print("El precio con descuento es: $", price_with_discount)

if (customer_type == 'Preferencial') :
    print("¡Felicidades! Ha obtenido el descuento")