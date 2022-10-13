if __name__ != "__main__":
    import pandas as pd
    from random import randint as ri
    from utils.consts import COLUNAS, print_v

    class DataFrame_Aluguel_Utils:
        def __init__(self):
            self.df: pd.DataFrame = pd.DataFrame(columns=COLUNAS)
            self.qtd = self.escolhe_quantidade_de_items()

        def cria_tabela_inteira(self):
            self._1_tipos()
            self._2_bairros()
            self._3_comodos()
            self._4_area()
            self._5_valor()

        def preenche_colunas(self, colunas_a_preencher: str | list,
                             valores_a_usar: list = "Other"):

            from utils.utils_imports import preenche_coluna

            preenche_coluna(self, colunas_a_preencher, valores_a_usar)

        def _1_tipos(self):
            from utils.utils_imports import preenche_tipos

            preenche_tipos(self)

        def _2_bairros(self):
            from utils.utils_imports import preenche_bairros

            preenche_bairros(self)

        def _3_comodos(self):
            from utils.utils_imports import preenche_comodos

            preenche_comodos(self)

        def _4_area(self):
            from utils.utils_imports import preenche_area

            preenche_area(self)

        def _5_valor(self):
            from utils.utils_imports import preenche_valor

            preenche_valor(self)

        def _6_impostos(self):
            from utils.utils_imports import preenche_impostos

            preenche_impostos(self)

        @staticmethod
        def escolhe_quantidade_de_items() -> int:
            return int(ri(1**4, 2**4))

        @property
        def get_qtd(self):
            return self.qtd

        @property
        def get_df(self):
            return self.df

        def get_value(self, coluna: str | int, indice: int) -> pd.Series:
            try:
                return self.df.loc[indice][coluna]
            except KeyError:
                print_v("Não foi possivel encontrar o valor")

        def __str__(self):
            return str(self.df)
