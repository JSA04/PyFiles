import pandas as pd
from string import capwords

CHANCE_PREENCHER_TIPOS = pd.Series(['Apartamento', 'Casa', 'Casa de Vila', 'Terreno Padrão', 'Casa de Condomínio'] * 50 +
                  ['Quitinete', 'Flat', 'Loft'] * 20 +
                  ['Galpão/Depósito/Armazém', 'Conjunto Comercial/Sala', 'Loja/Salão',
                   'Casa Comercial', 'Box/Garagem', 'Sítio',
                   'Loteamento/Condomínio', 'Studio', 'Hotel', 'Chácara', 'Pousada/Chalé'] * 5 +
                  ['Prédio Inteiro', 'Loja Shopping/ Ct Comercial', 'Indústria'] * 2)

BAIRROS = \
    pd.read_csv("../Bairros de Sao Paulo.csv", sep=";").drop_duplicates(subset="Bairros")
CHANCE_PREENCHER_BAIRROS = \
    BAIRROS.Bairros.apply(lambda x: capwords(x)).sort_values() 
                                                    
CHANCE_PREENCHER_QUARTOS = pd.Series([1] * 30 + [2] * 20 + [3] * 
                                10 + [4] * 2 + [5] * 1)

TIPO_RESIDENCIAL_GRANDE = ['Apartamento', 'Casa', 'Casa de Vila', 'Casa de Condomínio']
TIPO_RESIDENCIAL_PEQUENO = ['Quitinete', 'Flat', 'Loft']
TIPO_COMERCIAL_PEQUENA = ['Galpão/Depósito/Armazém', 'Conjunto Comercial/Sala', 'Loja/Salão',
                   'Casa Comercial', 'Box/Garagem', 'Sítio',
                   'Loteamento/Condomínio', 'Studio', 'Hotel', 'Chácara', 'Pousada/Chalé']
TIPO_COMERCIAL_GRANDE = ['Prédio Inteiro', 'Loja Shopping/ Ct Comercial', 'Indústria']