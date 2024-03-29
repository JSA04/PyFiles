if __name__ != "__main__":
    from utils.DF_utils import DataFrame_Aluguel_Utils as Dau
    from random import randint as ri
    from utils.consts import TIPO_RESIDENCIAL_PEQUENO, TIPO_COMERCIAL_GRANDE, TIPO_COMERCIAL_PEQUENA
    import pandas as pd

    def preenche_area(cls: Dau) -> None:
        valores_a_calcular: pd.DataFrame = cls.df.loc[:, ["Quartos", "Vagas", "Suites"]]

        area: list = []

        for i in range(cls.qtd):
            tipo: pd.Series = cls.get_value("Tipo", i)

            area_comodos: int = valores_a_calcular.loc[i, ["Quartos", "Suites"]].sum() * \
                                ri(15, 25)

            area_vagas: int = 0
            if "Apartamento" != tipo not in TIPO_RESIDENCIAL_PEQUENO:
                area_vagas += valores_a_calcular.loc[i, ["Vagas"]].sum() * ri(5, 10)

            area_comercial: int = 0
            if tipo in TIPO_COMERCIAL_PEQUENA:
                area_comercial += ri(20, 200)
            elif tipo in TIPO_COMERCIAL_GRANDE:
                area_comercial += ri(500, 2000)

            area.append(area_comodos + area_vagas + area_comercial)

        cls.df["Area"] = area
