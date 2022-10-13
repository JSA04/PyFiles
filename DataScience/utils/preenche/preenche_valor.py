if __name__ != "__main__":
    from utils.DF_utils import DataFrame_Aluguel_Utils as Dau

    def preenche_valor(cls: Dau):
        caract = cls.df.loc[:, ["Quartos", "Vagas", "Suites", "Area"]]
        valores = []

        for i in range(cls.qtd):
            valor = caract.iloc[i].sum() * 15
            valores.append(valor)

        cls.df["Valor"] = valores
