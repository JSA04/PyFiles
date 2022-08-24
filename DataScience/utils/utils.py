import pandas as pd
from random import randint as rI
from utils.consts import COLUNAS


class DataFrame_Aluguel_Utils:
    def __init__(self):
        self.df : pd.DataFrame = pd.DataFrame(columns=COLUNAS)
        self.qtd = self.escolhe_quantidade_de_items()

    def cria_tabela_inteira(self):
        self._preenche_tipos()
        self._preenche_bairros()
        self._preenche_comodos()

    def _preenche_coluna(self, coluna_a_preencher: str,
                        valores_a_usar: pd.Series | str = "Other"):

        from utils.utils_imports import preenche_coluna

        preenche_coluna(self, coluna_a_preencher, valores_a_usar)

    def _preenche_bairros(self):
        from utils.utils_imports import preenche_bairros

        preenche_bairros(self)

    def _preenche_tipos(self):
        from utils.utils_imports import preenche_tipos

        preenche_tipos(self)

    def _preenche_comodos(self):
        from utils.utils_imports import preenche_comodos

        preenche_comodos(self)

    @staticmethod
    def escolhe_quantidade_de_items() -> int:
        return int(rI(1**4, 2**4))

    @property
    def get_qtd(self):
        return self.qtd

    @property
    def get_df(self):
        return self.df
