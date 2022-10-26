class Base:

    import pandas as pd

    def __init__(self):
        self.tabela_palavras = self.pd.DataFrame()
        self.lastid = 0

    def adiciona_palavras(self) -> None:

        from Base_de_Dados.dados.palavras_dao import retorna_palavras

        palavras = retorna_palavras()

        new_lastid: int = self.lastid + len(palavras)

        tabela = self.pd.DataFrame(
            {"id": range(self.lastid, new_lastid), "palavra": palavras}
        )

        self.lastid: int = new_lastid

        self.tabela_palavras = \
            self.pd.concat([self.tabela_palavras, tabela])

        self.tabela_palavras.set_index("id", inplace=True)

    def retorna_palavra_por_id(self, id) -> str:
        palavra: str = self.tabela_palavras.loc[
            id, "palavra"
        ]

        return palavra

    def verifica_palavra_no_db(self, palavra_a_conferir) -> bool:
        if palavra_a_conferir in self.tabela_palavras["palavra"].values:
            return True
        return False

    def qtd_linhas(self) -> int:
        return self.tabela_palavras.shape[0]


b = Base()
b.adiciona_palavras()
palavra = b.retorna_palavra_por_id(2)
print(b.tabela_palavras)
print("palavra " + palavra)
