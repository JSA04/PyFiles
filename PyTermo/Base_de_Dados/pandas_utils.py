import pandas
import pandas as pd


class Pandas_Base:

    def __init__(self):
        self.tabela_palavras = pandas.DataFrame()
        self.lastid = 0


    def adiciona_palavras(self, dados : list | tuple = ()) -> None:
        new_lastid = self.lastid + len(dados)

        tabela = pd.DataFrame(
            {"id": range(self.lastid, new_lastid), "palavra": dados}
        )

        self.lastid = new_lastid

        self.tabela_palavras = \
            pd.concat([self.tabela_palavras, tabela])

    def pega_palavra_por_id(self, id) -> str:
        return self.tabela_palavras.loc[
            self.tabela_palavras["id"] == id, "palavra"
        ]

    def verifica_palavra_no_db(self, palavra_a_conferir) -> bool:
        if palavra_a_conferir in self.tabela_palavras["palavra"].values:
            return True
        return False

    def qtd_linhas(self) -> int:
        return self.tabela_palavras.shape[0]


def database_pandas_termo() -> Pandas_Base():
    from Palavras.palavras_dao import palavras

    database = Pandas_Base()
    database.adiciona_palavras(palavras)

    return database
