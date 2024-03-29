if __name__ != "__main__":
    from utils.DF_utils import DataFrame_Aluguel_Utils as Dau
    from utils.consts import TIPOS_COM_PROBABILIDADE, retorna_aleatorio


    def preenche_tipos(cls: Dau):

        vals = []

        for _ in range(0, cls.get_qtd):
            valor = retorna_aleatorio(TIPOS_COM_PROBABILIDADE)
            vals.append(valor)

        cls.preenche_colunas("Tipo", vals)
