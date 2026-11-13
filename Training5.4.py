IVA = 0.21
DESCOMPTES = {
    "particular": 0.00,
    "habitual": 0.10,
    "empresa": 0.15,
}


def calcular_preu_inicial(cost_peces, cost_ma_obra):
    """Retorna el preu inicial de la reparació (peces + mà d'obra)."""
    return cost_peces + cost_ma_obra


def calcular_descompte(preu, tipus_client):
    """Retorna l'import del descompte segons el tipus de client."""
    percentatge = DESCOMPTES.get(tipus_client, 0.0)
    return preu * percentatge


def calcular_iva(base_imposable):
    """Retorna l'import de l'IVA sobre la base imposable."""
    return base_imposable * IVA


def calcular_total(preu, descompte, iva):
    """Retorna el total a pagar."""
    return preu - descompte + iva


def mostrar_menu():
    print("\n===== SERVEI TÈCNIC INFORMÀTIC =====")
    print("1. Introduir una nova reparació")
    print("2. Consultar el nombre de reparacions")
    print("3. Consultar la facturació acumulada")
    print("4. Sortir")


def llegir_import(missatge):
    """Demana un import i insisteix fins que sigui un número no negatiu."""
    while True:
        try:
            valor = float(input(missatge))
            if valor < 0:
                print("  Error: l'import no pot ser negatiu.")
            else:
                return valor
        except ValueError:
            print("  Error: has d'introduir un número.")


def llegir_tipus_client():
    """Demana el tipus de client i insisteix fins que sigui vàlid."""
    opcions = ", ".join(DESCOMPTES.keys())
    while True:
        tipus = input(f"Tipus de client ({opcions}): ").strip().lower()
        if tipus in DESCOMPTES:
            return tipus
        print("  Error: tipus de client no vàlid.")


def mostrar_factura(nom, preu, descompte, iva, total):
    print("\n------------- FACTURA -------------")
    print(f"Client:          {nom}")
    print(f"Preu inicial:    {preu:10.2f} €")
    print(f"Descompte:      -{descompte:10.2f} €")
    print(f"IVA ({IVA * 100:.0f} %):     {iva:10.2f} €")
    print("-----------------------------------")
    print(f"TOTAL A PAGAR:   {total:10.2f} €")
    print("-----------------------------------")


def introduir_reparacio():
    """Demana les dades, mostra la factura i retorna el total facturat."""
    nom = input("Nom del client: ").strip()
    cost_peces = llegir_import("Cost de les peces (€): ")
    cost_ma_obra = llegir_import("Cost de la mà d'obra (€): ")
    tipus = llegir_tipus_client()

    preu = calcular_preu_inicial(cost_peces, cost_ma_obra)
    descompte = calcular_descompte(preu, tipus)
    iva = calcular_iva(preu - descompte)
    total = calcular_total(preu, descompte, iva)

    mostrar_factura(nom, preu, descompte, iva, total)
    return total


def main():
    num_reparacions = 0
    facturacio_total = 0.0

    while True:
        mostrar_menu()
        opcio = input("Selecciona una opció: ").strip()

        if opcio == "1":
            facturacio_total += introduir_reparacio()
            num_reparacions += 1
        elif opcio == "2":
            print(f"\nReparacions realitzades: {num_reparacions}")
        elif opcio == "3":
            print(f"\nFacturació acumulada: {facturacio_total:.2f} €")
        elif opcio == "4":
            print("\nFins aviat!")
            break
        else:
            print("\nOpció no vàlida. Tria un número de l'1 al 4.")


if __name__ == "__main__":
    main()

#
# Exercici 5: Reflexió final

#4. Quina diferència hi ha entre print() i return?
print() mostra un valor per pantalla; return retorna el resultat a qui ha cridat la funció i l’acaba.

#5. Per què és millor dividir un programa en funcions?
Perquè el codi és més ordenat, fàcil de llegir i de revisar, i cada funció fa una única tasca.

#6. Què és un paràmetre?
Una variable de la definició de la funció que rep les dades amb què treballa.

#7. Què és una variable local?
Una variable creada dins d’una funció, que només existeix dins d’ella.

#8. Quins avantatges té reutilitzar una funció?
Evita repetir codi, estalvia temps i, si cal canviar alguna cosa, només es modifica en un lloc.