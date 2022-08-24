from utils.utils import DataFrame_Aluguel_Utils
from utils.consts import CHANCE_PREENCHER_TIPOS
from random import randint as rI


def preenche_tipos(cls: DataFrame_Aluguel_Utils):
    vals = []

    for _ in range(0, cls.get_qtd):
        valor = CHANCE_PREENCHER_TIPOS[rI(0, len(CHANCE_PREENCHER_TIPOS))]
        vals.append(valor)

    cls._preenche_coluna("Tipo", vals)
