from Base_de_Dados.MySQL.base_mysql import database_mysql_termo
from Base_de_Dados.Pandas.base_pandas import database_pandas_termo
from typing import Union
from Base_de_Dados.dados.json_utils import retorna_json, escreve_json
from os import system


def retorna_base_de_dados() -> (Union[database_mysql_termo,
                                      database_pandas_termo,
                                      None]):

    dados = retorna_json()

    if dados["Base"] == "Pandas":
        return database_pandas_termo()
    elif dados["Base"] == "MySQL":
        return database_mysql_termo()
    else:
        return _pede_base(dados)


def _pede_base(dados) -> (Union[database_mysql_termo,
                           database_pandas_termo,
                           None]):

    while True:
        tipo = input("Qual A Base De Dados Que Deseja Usar?\n"
                     "\n1 - MySQL:\n"
                     "Só Funcionará Em Computadores Com MySQL Server Instaladado.\n"
                     "\n2 - Pandas:\n"
                     "Funcionará Em Todos Os Dispositivos.\n"
                     "\n3 - Pular\n"
                     "\nR: ").strip()

        system("cls")

        if tipo.upper() in ["1", "MS", "MYSQL", "SQL", "M"]:
            dados["Base"] = "MySQL"
            escreve_json(dados)
            return database_mysql_termo()

        elif tipo.upper() in ["2", "PANDAS", "PD", "P"]:
            dados["Base"] = "Pandas"
            escreve_json(dados)
            return database_pandas_termo()

        elif tipo.upper() in ["3", "PULAR"]:
            return None

        else:
            print("\033[31mDado Digitado É Invalido.\033[m\n")

