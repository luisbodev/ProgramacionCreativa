# Grupo 4
# Integrantes:
#    Luis Bonilla - María Cruz - Gil Fuentes - María Renee Aguilar

# Ejercicio
# Escriban un programa que pida un departamento y diga qué zona de El Salvador es.
# Si no es un departamento de El Salvador deberá escribir “No es un departamento de El Salvador”.
# Zona Occidental (Ahuachapán - Santa Ana - Sonsonate)
# Zona central (La Libertad - San Salvador)
# Zona paracentral (Chalatenango - Cuscatlán - La Paz - Cabañas - San Vicente)
# Zona Oriental (Usulután - San Miguel - Morazán - La Unión)

# Aquí se le esta pidiendo al usuario que ingrese un departamento de El Salvador y se esta guardando en la variable "departamento"
departamento = input("Escribe un departamento de El Salvador: ")

# Se esta modificando la variable "departamento" convirtiendola en mayúsculas y quitandole los espacios al inicio y final
departamento = departamento.upper().strip()

# Aquí se está comparando si el departamento ingresado esta en la zona occidental 
if(departamento == "AHUACHAPAN" or departamento == "AHUACHAPÁN" or departamento == "SANTA ANA" or departamento == "SONSONATE"):
    # Se está imprimiendo el mensaje que indica de que zona es
    print("El departamento es de la Zona Occidental")
# Aquí se está comparando si el departamento ingresado esta en la zona central 
elif(departamento == "LA LIBERTAD" or departamento == "SAN SALVADOR"):
    # Se está imprimiendo el mensaje que indica de que zona es
    print("El departamento es de la Zona Central")
# Aquí se está comparando si el departamento ingresado esta en la zona Paracentral 
elif(departamento == "CHALATENANGO" or departamento == "CUSCATLAN" or departamento == "CUSCATLÁN" or departamento == "LA PAZ" or departamento == "CABAÑAS" or departamento == "SAN VICENTE"):
    # Se está imprimiendo el mensaje que indica de que zona es  
    print("El departamento es de la Zona Paracentral")
# Aquí se está comparando si el departamento ingresado esta en la zona oriental 
elif(departamento == "USULUTAN" or departamento == "USULUTÁN" or departamento == "SAN MIGUEL" or departamento == "MORAZAN" or departamento == "MORAZÁN" or departamento == "LA UNION" or departamento == "LA UNIÓN"):
    # Se está imprimiendo el mensaje que indica de que zona es  
   print("El departamento es de la Zona Oriental")
# Si el departamento no esta dentro de las opciones deberá escribir un mensaje que lo indique
else:
    print("No es un departamento de El Salvador")