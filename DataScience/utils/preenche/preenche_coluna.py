import pandas as pd

if __name__ != "__main__":
    from utils.DF_utils import DataFrame_Aluguel_Utils as Dau
    from utils.consts import print_v
    from typing import List


    def preenche_coluna(cls: Dau,
                        coluna_a_preencher: str | list,
                        valores_a_usar: list):

        if confere_parametros(cls, coluna_a_preencher, valores_a_usar):
            if type(coluna_a_preencher) == list:
                for i, coluna in enumerate(coluna_a_preencher):
                    cls.df[coluna] = valores_a_usar[i]
            else:
                cls.df[coluna_a_preencher] = valores_a_usar


    def confere_parametros(cls: Dau, colunas: str | list, valores: List[list]) -> bool:
        if type(colunas) == list:
            if len(colunas) == len(valores):
                col: str = ""
                try:
                    for coluna in colunas:
                        col: pd.Series = coluna[:]
                        teste: pd.Series = cls.df[coluna]
                except KeyError:
                    print_v(f"A coluna {col} não existe")
                return True
            else:

                menor: str = f"{len(colunas)} colunas" if len(colunas) < len(valores) \
                    else f"{len(valores)} lista de valores"

                maior: str = f"{len(valores)} lista de valores" if len(colunas) < len(valores) \
                    else f"{len(colunas)} colunas"

                print_v(f"Não foi possivel preencher as colunas pois há apenas {menor}"
                        f"para {maior}.")
                return False

        elif type(colunas) == str:
            if valores:
                try:
                    teste: pd.Series = cls.df[colunas]
                except KeyError:
                    print_v(f"A coluna {colunas} não existe")
                return True
