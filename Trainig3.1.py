Numero1 = int(input("Introdueix el primer número: "))
Numero2 = int(input("Introdueix el segon número: "))
Numero3 = int(input("Introdueix el tercer número: "))
if Numero1 > Numero2:
    print("El primer número és més gran que el segon.")
elif Numero2 > Numero1:
    print("El segon número és més gran que el primer.")
elif Numero2 > Numero3:
    print("El segon número és més gran que el tercer.")
else:
    print("El tercer número és més gran que el segon.")