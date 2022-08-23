from utils_imports import rI, pd

class DataFrame_Aluguel_Utils:
    def __init__(self, dataframe):
        self.df : pd.DataFrame = dataframe
        self.qtd = self.escolhe_quantidade_de_items
    

    def preenche_coluna(self, coluna_a_preencher: str, valores_a_usar: pd.Series|str = "Other"):
        from utils_imports import preenche_coluna

        preenche_coluna(self, coluna_a_preencher, valores_a_usar)

    
    def preenche_comodos(self):
        from utils_imports import preenche_comodos

        preenche_comodos(self)

    @staticmethod
    def _escolhe_qtd_suites_ou_vagas(valor : int, tipo : str):
        if tipo in ['Apartamento', 'Casa', 'Casa de Vila', 'Casa de Condomínio']:
            qtds = [0] * 10 + [1] * (valor * 3) + [2] * (valor * 2) + [3] * valor
            num_al = rI(1, len(qtds)) - 1
            qtds = qtds[num_al]
        elif tipo in ['Quitinete', 'Flat', 'Loft']:
            qtds = 0
        elif tipo in ['Galpão/Depósito/Armazém', 'Conjunto Comercial/Sala', 'Loja/Salão',
                   'Casa Comercial', 'Box/Garagem', 'Terreno Padrão', 'Sítio',
                   'Loteamento/Condomínio', 'Studio', 'Hotel', 'Chácara', 'Pousada/Chalé']:
            qtds = rI(100, 200)
        elif tipo in ['Prédio Inteiro', 'Loja Shopping/ Ct Comercial', 'Indústria']:
            qtds = rI(1000, 10000)
        return qtds

    @property
    def escolhe_quantidade_de_items(self):
        return rI(0, int(2**4.3))

    @property
    def get_df(self):
        return self.df