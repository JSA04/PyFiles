from Base_de_Dados.Pandas._pandas_utils import Pandas_Base


def database_pandas_termo() -> Pandas_Base():

    from Termo_Utils.utils import retorna_json, atualiza_json

    database = Pandas_Base()

    database.adiciona_palavras()

    json = retorna_json()
    json["Base"] = "Pandas"
    atualiza_json(json)

    return database
