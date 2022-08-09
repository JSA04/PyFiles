from Base_de_Dados.Pandas._pandas_utils import Pandas_Base


def database_pandas_termo() -> Pandas_Base():

    from Termo_Utils.utils import retorna_json, atualiza_json

    database = Pandas_Base()

    dados = retorna_json()
    dados["Base"] = "Pandas"
    atualiza_json(dados)

    database.adiciona_palavras()

    return database
