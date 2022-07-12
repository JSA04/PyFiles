import pandas as pd
from auxiliares_pandas import noteprint, h1, h2, h3

h1("Guia de pandas")


h2("Funcionalidades do Pandas")


noteprint("DataFrame()",
"""Retorna uma tabela do pandas a partir de um dicionario do python, chamada
de DataFrame.""")

carros = {"Carro": ["Onix", "Fox"],
          "Fabricacao": [2016, 2013],
          "Modelo": [2016, 2014],
          "Valor": [56000, 26600]}

tabela_carros = pd.DataFrame(carros)
print(
    tabela_carros
)

noteprint("pandas.read_excel()",
"""Retorna um DataFrame a partir de um arquivo excel e retorna em forma de um 
DataFrame.""")


tabela_carros = pd.read_excel("carros.xlsx")
print(
    tabela_carros
)

noteprint("DataFrame.head()",
"""Retorna as X primeiras linhas da tabela, sendo X o número passado como 
parametro, que no caso é 3.""")

print(
    tabela_carros.head(3)
)

noteprint("DataFrame.shape",
"""Retorna as dimenções da tabela, como (X,Y). Sendo X = linhas e 
Y = colunas.""")

print(
    tabela_carros.shape
)

noteprint("DataFrame.describe()",
"""Retorna todas as colunas compostas por números e mostra a quantidade de dados 
a média dos dados, desvio padrão, menor número, 25, 50 e 75 porcento do número 
e maior número.""")

print(
    tabela_carros.describe()
)

h2("Pegando colunas especificas")

h3("""Para pegar a ultima coluna devemos colocar o nome das colunas que 
desejamos após da tabela entre colchetes.""")

print(
    tabela_carros["carro"]
)

h3("""Quando queremos mais de uma coluna, devemos passar uma lista como 
parametro com as colunas que desejamos.""")

colunas = ["carro", "valor"]
print(
    tabela_carros[colunas]
)

h3("""IMPORTANTE: Quando o pandas nos retorna uma coluna ou linha sozinhas,
é o que chamamos de "Series", assim como diz o "type()" dela.""")

print(
    type(tabela_carros["carro"])
)

h2("Pegando linhas especificas")


noteprint("DataFrame.loc",
"""O loc localiza linhas de um dataframe quando passamos o indice dela entre
colchetes a ele.""")

print(
    tabela_carros.loc[0]
)

h3("""Para pegarmos mais de uma linha, devemos passar um intervalo assim 
como passamos a uma lista""")

print(
    tabela_carros.loc[2:5]
)

h3("Podemos também passar uma condição para buscar um valor.")

print(
    tabela_carros.loc[
        tabela_carros["marca"] == "Volksvagem"
    ]
)

h3("Para filtrar as colunas que queremos, passamos elas no segundo parametro.")


print(
    tabela_carros.loc[
        tabela_carros["marca"] == "Volksvagem", ["carro", "valor", "cor"]
    ]
)

h3("""Para pegarmos um item especifico, passamos o indice dele e depois a coluna 
dele.""")

print(
    tabela_carros.loc[1, "carro"]
)

h2("Adicionar uma coluna")


h3("Para criar uma coluna seguimos esse modelo.")

tabela_carros["preco_a_vista"] = tabela_carros["valor"] * 0.95

print(
    tabela_carros
)

h3("""Para criar uma coluna atribuindo o valor 0 para todos os elementos, o pandas
recomenda usar o loc para criar a coluna. Passando primeiro quais linhas 
deve-se preencher, depois o nome da nova coluna.""")

tabela_carros.loc[:, "Imposto"] = 0

print(
    tabela_carros
)

h2("Juntando DataFrames")


noteprint("DataFrame.append()", "O append é a função que junta duas tabelas.")

tabela_carros_importados = pd.read_excel("carros_i.xlsx")
tabela_carros = tabela_carros.append(tabela_carros_importados)

print(
    tabela_carros
)

h3("Removendo linhas e colunas da tabela")


noteprint("DataFrame.drop()", """O drop exclui uma:
* Linha, quando passamos (índice da linha, axis=0)
* Coluna, quando passamos (índice da coluna, axis=1)""")


tabela_carros = tabela_carros.drop("Imposto", axis=1)
print(
    tabela_carros
)

noteprint("DataFrame.dropna()",
"""O dropna é utilizado para excluir linhas ou colunas que possuem valores NaN
Para excluir uma linha ou coluna que tenha TODOS os valores NaN, fazemos do
jeito abaixo passando o axis = 0 para excluir linha ou 1 para a coluna: 

 - tabela_carros = tabela_carros.dropna(how="all", axis=0)

Para excluir linhas que possuem pelo menos 1 valor NaN, fazemos:

 - tabela_carros = tabela_carros.dropna(axis=0)""")

noteprint("DataFrame.fillna",
"""Para prencher colunas que possuem valores NaN, utilizamos o fillna""")

tabela_carros["preco_a_vista"] = (
    tabela_carros['preco_a_vista'].fillna(
        tabela_carros['preco_a_vista'].mean())
)

noteprint("DataFrame.ffill",
"""Ultilizamos o ffill para prencher valores NaN com o valor acima na tabela.""")

tabela_carros = tabela_carros.ffill()

print(
    tabela_carros
)

noteprint("DataFrame.value_counts()",
"""O value_counts mostra a quantidade de vezes que cada valor aparece na coluna
que especificamos.""")


tabela_carros["carro"].value_counts()

noteprint("DataFrame.groupby()",
'''O groupby agrupa os valores com o mesmo nome da coluna especificada. 
No caso abaixo é "carro", e com isso é possivel realizar operações que 
desejamos, que no caso foi "mean"(media) com os dados numericos deles''')

preco_medio = tabela_carros.groupby("carro").mean()

print(
    preco_medio
)

h3("Mesclando duas DataFrames")

noteprint("DataFrame.merge()",
"""O merge mescla dois dataframes, procurando colunas com nomes iguais.""")

tabela_gerentes = pd.read_excel("carros_gpm.xlsx")

tabela_carros = tabela_carros.merge(tabela_gerentes)

print(tabela_carros)
