from Base_de_Dados.mysql_utils import database_mysql_termo
from Base_de_Dados.pandas_utils import database_pandas_termo


def database(tipo: str):
    if tipo.upper() in ["MYSQL", "SQL"]:
        return database_mysql_termo()

    elif tipo.upper() in ["PANDAS", "PD"]:
        return database_pandas_termo()
