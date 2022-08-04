from .Termo import Termo


def mostra_pede_para_mudar_DB(cls : Termo):
    from Base_de_Dados.dados.json_utils import retorna_json

    jsonDB = retorna_json()

    if jsonDB["Base"] != "":
        print("Sua Base De Dados Atual é:")
        print(f'\033[01m{jsonDB["Base"]}\033[m')
    else:
        print("Nenhuma Base De Dados Configurada.")

    if jsonDB["Base"] == "MySQL":
        print("\nAs Configurações Do Seu Banco De Dados São:")
        print(f"\033[01mHOST: {jsonDB['MySQL_Host']}")
        print(f"USUARIO: {jsonDB['MySQL_User']}\033[m")

    print()

    _pede_para_mudar_db(cls)

def _pede_para_mudar_db(cls : Termo):
    from Base_de_Dados.database import database_mysql_termo, database_pandas_termo
    from Base_de_Dados.dados.json_utils import retorna_json, escreve_json
    from os import system
    global opcoes

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

        if resp == "1" and jsonDB["Base"] == "":
            from Base_de_Dados.database import retorna_base_de_dados

            system("cls")

            cls.base_de_dados = retorna_base_de_dados()
            break

        if resp == "1":

            if jsonDB["Base"] == "MySQL":

                jsonDB["Base"] = "Pandas"
                jsonDB["MySQL_User"] = ""
                cls.base_de_dados = database_pandas_termo()

            else:

                jsonDB["Base"] = "MySQL"
                cls.base_de_dados = database_mysql_termo()

            escreve_json(jsonDB)

        elif resp == "2" and jsonDB["Base"] == "MySQL":
            jsonDB["MySQL_User"] = ""
            cls.base_de_dados = database_mysql_termo()
            break

        elif (resp == "2" and jsonDB["Base"] == "Pandas") or \
             (resp == "3" and jsonDB["Base"] == "MySQL"):

            jsonDB["Base"] = ""
            jsonDB["MySQL_User"] = jsonDB["MySQL_PW"] = ""
            escreve_json(jsonDB)
            break

        elif resp in ["2", "3", "4"]:
            break

        else:
            print("\033[31mDigite Uma Resposta Válida.\033[m")
