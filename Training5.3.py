import importlib.util
from pathlib import Path

_module_path = Path(__file__).with_name("Training5.2.py")
_spec = importlib.util.spec_from_file_location("training5_2", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
aplicar_descompte = _module.aplicar_descompte
def calcular_iva(preu):
    return preu * 0.21

def calcular_factura(preu, tipus_client):
    preu_amb_descompte = aplicar_descompte(preu, tipus_client)
    iva = calcular_iva(preu_amb_descompte)
    return preu_amb_descompte + iva

preu = float(input("Introdueix el preu: "))
tipus_client = input("Tipus de client: ").strip().lower()
total = calcular_factura(preu, tipus_client)
print(f"Total factura: {total:.2f} €")