from Termo_Utils.Termo import Termo
from Base_de_Dados.dados.json_utils import retorna_json, atualiza_json
from os import system
from Base_de_Dados.database import database_mysql_termo, \
                                   database_pandas_termo


def _pede_para_mudar_db(cls: Termo):
    jsonDB = retorna_json()

    if jsonDB["Base"] == "MySQL":
        opcoes = ("1 - Mudar Base De Dados\n"
                  "2 - Mudar Configurações do Banco de Dados\n"
                  "3 - Desvincular Base De Dados\n"
                  "4 - Voltar\n\nR: ")

    elif jsonDB["Base"] == "Pandas":
        opcoes = ("1 - Mudar Base De Dados\n"
                  "2 - Desvincular Base De Dados\n"
                  "3 - Voltar\n\nR: ")
    else:
        opcoes = ("1 - Configurar Base De Dados\n"
                  "2 - Voltar\n\nR: ")

    while True:
        resp = input(opcoes).upper()

        if resp == "1" and not jsonDB["Base"]:
            from Base_de_Dados.database import retorna_base_de_dados

            system("cls")

            cls.base_de_dados = retorna_base_de_dados()
            break


        if resp == "1":

            if jsonDB["Base"] == "MySQL":

                jsonDB["MySQL_Host"] = jsonDB["MySQL_User"] = \
                    jsonDB["MySQL_PW"] = ""

                cls.base_de_dados = database_pandas_termo()

            else:

                cls.base_de_dados = database_mysql_termo()

            atualiza_json(jsonDB)
            break

        elif resp == "2" and jsonDB["Base"] == "MySQL":
            jsonDB["MySQL_User"] = ""
            cls.base_de_dados = database_mysql_termo()
            break

        elif (resp == "2" and jsonDB["Base"] == "Pandas") or \
             (resp == "3" and jsonDB["Base"] == "MySQL"):

            jsonDB["Base"] = ""
            jsonDB["MySQL_Host"] = jsonDB["MySQL_User"] = \
                jsonDB["MySQL_PW"] = ""

            atualiza_json(jsonDB)
            break

        elif resp in ["2", "3", "4"]:
            break

        else:
            print("\033[31mDigite Uma Resposta Válida.\033[m")
