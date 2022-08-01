from ._pandas_utils import Pandas_Base


def database_pandas_termo() -> Pandas_Base():
    print("Carregando Base De Palavras...")

    database = Pandas_Base()

    database.adiciona_palavras()

    return database

base = database_pandas_termo()

print(base)
