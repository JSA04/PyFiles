if __name__ != "__main__":
    from random import randint as ri
    from utils.DF_utils import DataFrame_Aluguel_Utils
    from utils.consts import TIPO_COMERCIAL_GRANDE, \
        TIPO_COMERCIAL_PEQUENA, \
        TIPO_RESIDENCIAL_GRANDE, \
        TIPO_RESIDENCIAL_PEQUENO, \
        CHANCE_QTD_QUARTOS_CASA, \
        CHANCE_QTD_SUITES_CASA, \
        CHANCE_QTD_VAGAS_CASA


    def preenche_comodos(cls: DataFrame_Aluguel_Utils):
        vals = {"Q": [], "S": [], "V": []}

        for i in range(0, cls.get_qtd):
            tipo = cls.get_value("Tipo", i)

            if not tipo:
                print("É necessario ter a coluna tipo preenchida.")
                break

            vals_al: list = qtd_aleatorias(tipo)

            vals["Q"].append(vals_al[0])
            vals["S"].append(vals_al[1])
            vals["V"].append(vals_al[2])

        cls.preenche_colunas(["Quartos", "Suites", "Vagas"],
                             [vals["Q"], vals["S"], vals["V"]])

    def qtd_aleatorias(tipo) -> list | bool:

        if tipo in TIPO_RESIDENCIAL_GRANDE:

            q = CHANCE_QTD_QUARTOS_CASA[ri(0, len(CHANCE_QTD_QUARTOS_CASA) - 1)]
            s1 = CHANCE_QTD_SUITES_CASA(q)
            s = s1[ri(0, len(s1) - 1)]
            v = CHANCE_QTD_VAGAS_CASA[ri(0, len(CHANCE_QTD_VAGAS_CASA) - 1)]

            return [q, s, v]

        elif tipo in TIPO_RESIDENCIAL_PEQUENO:
            q, s, v = ([1] * 10 + [2])[ri(0, 10)], 0, 1
            return [q, s, v]

        elif tipo in TIPO_COMERCIAL_GRANDE:
            q = s = 0
            v = ri(10 ** 3, 10 ** 4)
            return [q, s, v]

        elif tipo in TIPO_COMERCIAL_PEQUENA:
            q = s = 0
            v = ri(10 ** 2, 200)
            return [q, s, v]
        return False
