from utils.utils import DataFrame_Aluguel_Utils
from utils.consts import BAIRROS
from random import randint as rI


def preenche_bairros(cls: DataFrame_Aluguel_Utils):
    vals = []

    for _ in range(0, cls.get_qtd):
        valor = BAIRROS[rI(0, len(BAIRROS)) - 1]
        vals.append(valor)

    cls._preenche_coluna("Bairro", vals)
