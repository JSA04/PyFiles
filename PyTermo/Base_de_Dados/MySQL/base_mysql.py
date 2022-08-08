from typing import Union
from Termo_Utils.utils import retorna_json, atualiza_json
from Base_de_Dados.MySQL._mysql_utils import Mysql_Base
from mysql.connector.errors import ProgrammingError



def database_mysql_termo() -> Union[Mysql_Base, None]:

    dados = retorna_json()
    while True:
        database = Mysql_Base()

        print("Carregando Base De Palavras...")

        try:
            if database.db is None:
                break

            elif database.qtd_linhas() == 0:
                database.adiciona_palavras()

        except ProgrammingError:
            try:
                database.cria_tabela_palavras()
                database.adiciona_palavras()

            except ProgrammingError:
                print("\n\033[31mEste usuário não possui acesso ao Banco de Dados.\033[m")

        dados["Base"] = "MySQL"
        atualiza_json(dados)
        return database
