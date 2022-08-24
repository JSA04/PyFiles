import pandas as pd
from string import capwords

COLUNAS = ["Tipo;Bairro;Quartos;Vagas;Suites;Area;Valor;Condominio;IPTU".split(";")]

#########################################################################################################

CHANCE_PREENCHER_TIPOS = (['Apartamento', 'Casa', 'Casa de Vila',
                           'Terreno Padrão', 'Casa de Condomínio'] * 50 +
    ['Quitinete', 'Flat', 'Loft'] * 20 +
    ['Galpão/Depósito/Armazém', 'Conjunto Comercial/Sala', 'Loja/Salão',
     'Casa Comercial', 'Box/Garagem', 'Sítio',
     'Loteamento/Condomínio', 'Studio', 'Hotel', 'Chácara', 'Pousada/Chalé'] * 5 +
    ['Prédio Inteiro', 'Loja Shopping/ Ct Comercial', 'Indústria'] * 2)

#########################################################################################################

BAIRROS = \
    pd.read_csv("utils\Bairros de Sao Paulo.csv", sep=";").drop_duplicates(subset="Bairros")

BAIRROS = \
    BAIRROS.Bairros.apply(lambda x: capwords(x)).sort_values().tolist()

#########################################################################################################

CHANCE_QTD_QUARTOS_CASA = [1] * 30 + [2] * 20 + [3] * \
                           10 + [4] * 2 + [5] * 1

CHANCE_QTD_SUITES_CASA = lambda x: [0] * 30 + [1] * 20 + [2] * (4 * x) + [3] * (x * 2)
CHANCE_QTD_VAGAS_CASA = [1] * 30 + [2] * 20 + [3] * 5

TIPO_RESIDENCIAL_GRANDE = ['Apartamento', 'Casa', 'Casa de Vila', "Terreno Padrão", 'Casa de Condomínio']
TIPO_RESIDENCIAL_PEQUENO = ['Quitinete', 'Flat', 'Loft']
TIPO_COMERCIAL_PEQUENA = ['Galpão/Depósito/Armazém', 'Conjunto Comercial/Sala', 'Loja/Salão',
                          'Casa Comercial', 'Box/Garagem', 'Sítio',
                          'Loteamento/Condomínio', 'Studio', 'Hotel', 'Chácara', 'Pousada/Chalé']
TIPO_COMERCIAL_GRANDE = ['Prédio Inteiro', 'Loja Shopping/ Ct Comercial', 'Indústria']

#########################################################################################################
