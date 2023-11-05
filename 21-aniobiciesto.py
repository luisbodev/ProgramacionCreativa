year = int(input("Escriba el año a comprobar: "))

biciesto_acaba_en_00 = (year%400==0)
biciesto_no_acaba_en_00 = (year%100!=0) and (year%4==0)

biciesto = biciesto_acaba_en_00 or biciesto_no_acaba_en_00
    
if biciesto:
    print("El año es biciesto")
else :
    print("El año no es biciesto")

