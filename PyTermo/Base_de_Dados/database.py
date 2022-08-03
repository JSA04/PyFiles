from Base_de_Dados.MySQL.base_mysql import database_mysql_termo
from Base_de_Dados.Pandas.base_pandas import database_pandas_termo
from typing import Union
import json
from os import system


local_arq = r"Base_de_Dados\dados\data.json"


def retorna_base_de_dados() -> (Union[database_mysql_termo,
                                      database_pandas_termo]):

    with open(local_arq) as arquivo:
        global dados

        dados = json.load(arquivo)

        if dados["Base"] == "Pandas":
            return database_pandas_termo()
        elif dados["Base"] == "MySQL":
            return database_mysql_termo()

        tipo = ""

    with open(local_arq, mode="w") as arquivo:

        while True:
            if tipo.upper() in ["MS", "MYSQL", "SQL", "M"]:
                dados["Base"] = "MySQL"
                arquivo.write(json.dumps(dados))
                return database_mysql_termo()

            elif tipo.upper() in ["PANDAS", "PD", "P"]:
                dados["Base"] = "Pandas"
                arquivo.write(json.dumps(dados))
                return database_pandas_termo()

            tipo = input("Qual A Base De Dados Que Deseja Usar?\n"
                         "\n1 - MySQL"
                         "\n2 - Pandas\n"
                         "\nR: ")
            system("cls")

            if tipo.upper() in ["1", "MS", "MYSQL", "SQL", "M"]:
                tipo = "MySQL"

            elif tipo.upper() in ["2", "PANDAS", "PD", "P"]:
                tipo = "Pandas"

            else:
                print("\033[31mDado Digitado É Invalido.\033[m\n")
