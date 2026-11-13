i = 0 
hi_ha_negatiu = False

while i < 10:
     num = float(input("Introdueix un nombre: "))
     if num < 0:
         hi_ha_negatiu = True
     i =  i + 1

if hi_ha_negatiu:
    print("Hi ha hagut almenys un nombre negatiu")
else:
    print("No hi ha cap nombre negatiu")