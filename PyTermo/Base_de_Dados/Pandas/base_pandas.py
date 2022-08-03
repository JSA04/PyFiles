from Base_de_Dados.Pandas._pandas_utils import Pandas_Base


def database_pandas_termo() -> Pandas_Base():

    database = Pandas_Base()

    database.adiciona_palavras()

    return database

