import sys
from Termo_Utils.Termo import Termo
from os import system

termo = Termo()

try:
    termo.roda()

except KeyboardInterrupt:
    from Base_de_Dados.dados.json_utils import retorna_json
    
    dados = retorna_json()
    
    system("cls")
    
    if dados["Base"] == "MySQL":
        termo.base_de_dados.db.close()

system("exit")