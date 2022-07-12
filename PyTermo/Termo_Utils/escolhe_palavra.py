# Pega uma palavra aleatoria do arquivo de palavras.

from random import randint


def escolhe(jogo):
    al = randint(0, jogo.base.qtd_linhas())

    palavra = jogo.base.pega_palavra_por_id(al)

    return palavra.upper()
