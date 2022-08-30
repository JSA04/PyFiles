if __name__ != "__main__":
    from utils.DF_utils import DataFrame_Aluguel_Utils
    import pandas as pd

    def preenche_area(cls: DataFrame_Aluguel_Utils):
        qtd = pd.DataFrame([cls.df["Quartos"], cls.df["Vagas"], cls.df["Suites"]])

        print(qtd)
