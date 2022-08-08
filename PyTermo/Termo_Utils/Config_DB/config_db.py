from Termo_Utils.Termo import Termo
from .muda_db import _pede_para_mudar_db
from Base_de_Dados.dados.json_utils import retorna_json


def mostra_e_pede_para_mudar_DB(cls: Termo):
    jsonDB = retorna_json()

    if jsonDB["Base"]:
        print("Sua Base De Dados Atual é:")
        print(f'\033[01m{jsonDB["Base"]}\033[m\n')
    else:
        print("Nenhuma Base De Dados Configurada.\n")

    if jsonDB["Base"] == "MySQL":
        print("As Configurações Do Seu Banco De Dados São:")
        print(f"\033[01mHOST: {jsonDB['MySQL_Host']}")
        print(f"USUARIO: {jsonDB['MySQL_User']}\033[m\n")

    _pede_para_mudar_db(cls)
