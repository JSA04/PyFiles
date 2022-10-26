from Base_de_Dados.MySQL.base_mysql import database_mysql_termo
from Base_de_Dados.Pandas.base_pandas import database_pandas_termo
from typing import Union
from Base_de_Dados.dados.json_utils import retorna_json
from os import system


def retorna_base_de_dados() -> (Union[database_mysql_termo,
                                      database_pandas_termo,
                                      None]):
    dados: dict = retorna_json()

    if dados["Base"] == "Pandas":
        return database_pandas_termo()
    elif dados["Base"] == "MySQL":
        return database_mysql_termo()
    else:
        return _pede_base()


def _pede_base() -> Union[database_mysql_termo,
                          database_pandas_termo,
                          None]:
    while True:
        system("cls")

        print("Qual A Base De Dados Que Deseja Usar?\n")

        print("1 - MySQL")
        print("2 - Pandas")
        print("3 - Pular")

        tipo = input("\nR: ").strip()

        system("cls")

        if tipo.upper() in ["1", "MS", "MYSQL", "SQL", "M"]:
            return database_mysql_termo()

        elif tipo.upper() in ["2", "PANDAS", "PD", "P"]:
            return database_pandas_termo()

        elif tipo.upper() in ["3", "PULAR"]:
            return None

        else:
            print("\033[31mDado Digitado É Invalido.\033[m\n")
