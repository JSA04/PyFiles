from Termo_Utils.Termo import Termo
from Base_de_Dados.dados.json_utils import retorna_json, atualiza_json
from os import system
from Base_de_Dados.database import database_mysql_termo, \
                                   database_pandas_termo


def _pede_para_mudar_db(cls: Termo):
    jsonDB = retorna_json()

    base = jsonDB["Base"]

    if base == "MySQL":
        opcoes = ("1 - Mudar Base De Dados\n"
                  "2 - Mudar Configurações do Banco de Dados\n"
                  "3 - Desvincular Base De Dados\n"
                  "4 - Resetar Dados\n"
                  "5 - Voltar\n\nR: ")

    elif base == "Pandas":
        opcoes = ("1 - Mudar Base De Dados\n"
                  "2 - Desvincular Base De Dados\n"
                  "3 - Resetar Dados\n"
                  "4 - Voltar\n\nR: ")
    else:
        opcoes = ("1 - Configurar Base De Dados\n"
                  "2 - Resetar Dados\n"
                  "3 - Voltar\n\nR: ")

    while True:
        resp = input(opcoes).upper()

        if resp == "1" and not base:
            from Base_de_Dados.database import retorna_base_de_dados

            system("cls")

            cls.base_de_dados = retorna_base_de_dados()

        elif resp == "1":

            if base == "MySQL":

                jsonDB["MySQL_Host"] = jsonDB["MySQL_User"] = \
                    jsonDB["MySQL_PW"] = ""

                cls.base_de_dados = database_pandas_termo()
            else:

                cls.base_de_dados = database_mysql_termo()

        elif resp == "2" and base == "MySQL":
            jsonDB["MySQL_User"] = ""
            cls.base_de_dados = database_mysql_termo()

        elif (resp == "2" and base == "Pandas") or \
             (resp == "3" and base == "MySQL"):

            jsonDB["Base"] = ""
            jsonDB["MySQL_Host"] = jsonDB["MySQL_User"] = \
                jsonDB["MySQL_PW"] = ""

            atualiza_json(jsonDB)

        elif (resp == "4" and base == "MySQL") or \
             (resp == "3" and base == "Pandas") or \
             (resp == "2" and not base):


            jsonDB = {
                "Base": "", "MySQL_Host": "", "MySQL_User": "", "MySQL_PW": "",
                "Total_Partidas": 0, "Partidas_Ganhas": 0, "Partidas_Perdidas": 0,
                "Streak": 0}

            atualiza_json(jsonDB)

        elif resp in ["3", "4", "5"]:
            break

        else:
            print("\033[31mDigite Uma Resposta Válida.\033[m")
            continue
        break
