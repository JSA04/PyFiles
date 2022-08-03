from Base_de_Dados.MySQL._mysql_utils import Mysql_Base
from mysql.connector.errors import ProgrammingError


def database_mysql_termo() -> Mysql_Base:
    database = Mysql_Base()

    print("Carregando Base De Palavras...")

    try:
        if database.qtd_linhas() == 0:
            database.adiciona_palavras()

    except ProgrammingError:
        database.cria_tabela_palavras()
        database.adiciona_palavras()

    return database

