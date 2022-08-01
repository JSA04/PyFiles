from Base_de_Dados.base_mysql import database_mysql_termo
from Base_de_Dados.base_pandas import database_pandas_termo
from typing import Union


def retorna_base_de_dados(tipo: str = '') -> Union[database_mysql_termo,
                                                   database_pandas_termo]:
    while True:
        if tipo.upper() in ["MYSQL", "SQL"]:
            return database_mysql_termo()

        elif tipo.upper() in ["PANDAS", "PD"]:
            return database_pandas_termo()

        else:

            from os import system

            tipo = input("Qual A Base De Dados Que Deseja Usar?\n"
                         "\n1 - MySQL"
                         "\n2 - Pandas\n"
                         "\nR: ").strip()

            system("cls")

            if tipo.upper() in ["1", "MS", "MYSQL", "SQL"]:
                tipo = "MYSQL"

            elif tipo.upper() in ["2", "PANDAS", "PD"]:
                tipo = "PANDAS"

            else:
                print("\033[31mDado Digitado É Invalido.\033[m\n")
