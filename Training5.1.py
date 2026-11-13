def calcular_preu  (a, b):
    r= int(a) + int(b)
    return r

print("Calculadora de preus")
a= input("Preu de les peces: ")
b= input("Cost de ma d'obra: ")
Preu = calcular_preu(a, b)
print("El resultat de la suma és: ", Preu, "€")

#Respon:
#1. Quants paràmetres té la funció? Son dos el preu de les peces i el cost de la mà d’obra.
#2. Quin valor retorna? Retorna el cost de ma d'obra més el preu de les peces.
#3. Què passaria si eliminéssim el return? la funcio faria la suma però no retornaria cap valor, per tant no es podria utilitzar el resultat de la funció en altres parts del codi.
