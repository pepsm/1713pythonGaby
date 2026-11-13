def aplicar_descompte(preu, tipus_client):
    if tipus_client == "client habitual":
        return preu*0.9
    elif tipus_client == "empresa":
        return preu*0.85
    elif tipus_client == "particular":
        return preu
    else:
        print("Error, el tipus de client no es valid")
        return preu

preu = float(input("Introdueix el preu: "))
tipus_client = input("Tipus de client: ")
preu_final = aplicar_descompte (preu, tipus_client)
print("Preu final", preu_final, "€")