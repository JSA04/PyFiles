from Termo_Utils.Termo import Termo
from os import system

termo = Termo()

try:
    termo.roda()

except KeyboardInterrupt:
    from Termo_Utils.utils import retorna_json

    dados = retorna_json()

    system("cls")

    if dados["Base"] == "MySQL":
        termo.base_de_dados.db.close()
