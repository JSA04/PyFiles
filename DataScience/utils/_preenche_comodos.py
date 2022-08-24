from random import randint as rI
from utils.utils import DataFrame_Aluguel_Utils
from utils.consts import TIPO_COMERCIAL_GRANDE,\
                   TIPO_COMERCIAL_PEQUENA,\
                   TIPO_RESIDENCIAL_GRANDE,\
                   TIPO_RESIDENCIAL_PEQUENO,\
                   CHANCE_QTD_QUARTOS_CASA,\
                   CHANCE_QTD_SUITES_CASA,\
                   CHANCE_QTD_VAGAS_CASA



def preenche_comodos(cls : DataFrame_Aluguel_Utils):
    vals = {"Q" : [], "S" : [], "V" : []}

    for i in range(0, cls.get_qtd):
        tipo = cls.df.loc[i]["Tipo"]

        if not tipo:
            print("É necessario ter a coluna tipo preenchida.")
            break

        vals_al : list = qtd_aleatorias(tipo)

        vals["Q"].append(vals_al[0])
        vals["S"].append(vals_al[1])
        vals["V"].append(vals_al[2])

    cls._preenche_coluna("Quartos", vals["Q"])
    cls._preenche_coluna("Suites", vals["S"])
    cls._preenche_coluna("Vagas", vals["V"])


def qtd_aleatorias(tipo) -> list | bool:
    global Q, S, V

    if tipo in TIPO_RESIDENCIAL_GRANDE:

        Q = CHANCE_QTD_QUARTOS_CASA[rI(0, len(CHANCE_QTD_QUARTOS_CASA) - 1)]
        s = CHANCE_QTD_SUITES_CASA(Q)
        S = s[rI(0, len(s) - 1)]
        V = CHANCE_QTD_VAGAS_CASA[rI(0, len(CHANCE_QTD_VAGAS_CASA) - 1)]

    elif tipo in TIPO_RESIDENCIAL_PEQUENO:
        Q, S, V = ([1] * 10 + [2])[rI(0, 10)], 0, 1

    elif tipo in TIPO_COMERCIAL_GRANDE:
        Q = S = 0
        V = rI(10 ** 3, 10 ** 4)

    elif tipo in TIPO_COMERCIAL_PEQUENA:
        Q = S = 0
        V = rI(10**2, 200)
    else:
        return False
    return [Q, S, V]

