# Pega uma palavra aleatoria do arquivo de palavras.

from random import randint
from Termo_Utils.Termo import Termo


def escolhe_palavra(jogo : Termo):
    print("Escolhendo palavra...")
    al = randint(0, jogo.base_de_dados.qtd_linhas())

    palavra = jogo.base_de_dados.retorna_palavra_por_id(al)

    return palavra.upper()
