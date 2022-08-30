if __name__ != "main":

    from utils.DF_utils import DataFrame_Aluguel_Utils
    from utils.consts import BAIRROS, retorna_aleatorio

    def preenche_bairros(cls: DataFrame_Aluguel_Utils):
        vals = []

        for _ in range(0, cls.get_qtd):
            valor = retorna_aleatorio(BAIRROS)
            vals.append(valor)

        cls.preenche_colunas("Bairro", vals)
