#import pandas as pd
from utils.utils import DataFrame_Aluguel_Utils


def preenche_comodos(cls : DataFrame_Aluguel_Utils):
    valores = {"QUA" : [], "SUI" : [], "VAG" : []}

    for i in range(0, cls.qtd):
        tipo = cls.df["Tipo"]

        valores["SUI"].append(qtd_aleatorias(tipo))

def qtd_aleatorias(tipo):
    return 1, 2, 3

    # if tipo in TIPO_COMERCIAL_GRANDE:

    # elif tipo in TIPO_COMERCIAL_PEQUENA:
    # elif tipo in TIPO_RESIDENCIAL_GRANDE:
    # elif tipo in TIPO_RESIDENCIAL_PEQUENO:

dici = {"QUA" : [], "SUI" : [], "VAG" : []}

dici += qtd_aleatorias

print(dici)