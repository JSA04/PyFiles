from _operator import index

if __name__ != "__main__":
    import pandas as pd
    from string import capwords

    #########################################################################################################

    COLUNAS = ["Tipo;Bairro;Quartos;Vagas;Suites;Area;Valor;Condominio;IPTU".split(";")]

    #########################################################################################################

    TIPOS_COM_PROBABILIDADE = (['Apartamento', 'Casa', 'Casa de Vila',
                                'Terreno Padrão', 'Casa de Condomínio'] * 50 +
                               ['Quitinete', 'Flat', 'Loft'] * 20 +
                               ['Galpão/Depósito/Armazém', 'Conjunto Comercial/Sala',
                                'Loja/Salão',
                                'Casa Comercial', 'Box/Garagem', 'Sítio',
                                'Loteamento/Condomínio', 'Studio', 'Hotel',
                                'Chácara', 'Pousada/Chalé'] * 5 +
                               ['Prédio Inteiro', 'Loja Shopping/ Ct Comercial',
                                'Indústria'] * 2)

    #########################################################################################################


    BAIRROS = \
        pd.read_csv("utils/Bairros.csv", sep=";").drop_duplicates(subset="Bairros")

    BAIRROS: pd.Series = \
        BAIRROS.Bairros.apply(lambda x: capwords(x)).sort_values()

    BAIRROS: list = BAIRROS.tolist()



    #########################################################################################################

    CHANCE_QTD_QUARTOS_CASA: list = [1] * 30 + [2] * 20 + [3] * \
                              10 + [4] * 2 + [5] * 1

    CHANCE_QTD_SUITES_CASA: list = lambda x: [0] * 30 + [1] * 20 + [2] * (4 * x) + [3] * (x * 2)
    CHANCE_QTD_VAGAS_CASA: list = [1] * 30 + [2] * 20 + [3] * 5

    TIPO_RESIDENCIAL_GRANDE: list = ['Apartamento', 'Casa', 'Casa de Vila', "Terreno Padrão", 'Casa de Condomínio']
    TIPO_RESIDENCIAL_PEQUENO: list = ['Quitinete', 'Flat', 'Loft']
    TIPO_COMERCIAL_PEQUENA: list = ['Galpão/Depósito/Armazém', 'Conjunto Comercial/Sala', 'Loja/Salão',
                              'Casa Comercial', 'Box/Garagem', 'Studio', 'Pousada/Chalé']
    TIPO_COMERCIAL_GRANDE: list = ['Prédio Inteiro', 'Loteamento/Condomínio', 'Loja Shopping/ Ct Comercial',
                             'Indústria','Sítio', 'Hotel', 'Chácara']

    #########################################################################################################
    def retorna_aleatorio(lista_de_valores: list):

        from random import randint

        valor: int = randint(0, len(lista_de_valores) - 1)

        return lista_de_valores[valor]

    def print_v(values: str):
        print(f"\033[31m{str}\033[m")
