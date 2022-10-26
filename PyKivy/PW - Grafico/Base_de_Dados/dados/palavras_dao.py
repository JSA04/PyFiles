def verifica(palavra: str) -> str:

    palavra = palavra.upper()
    caracteres_invalidos = "-_áãâà.éèêóòôõìíìúîùç "

    for caracter in caracteres_invalidos:

        if (caracter.upper() in palavra or
                len(palavra.strip()) != 5):
            break

    return palavra


def retorna_palavras() -> list:
    with open(r"./Base_de_Dados/dados/palavras.csv", mode="r",
              encoding="UTF-8") as arq_palavras:

        lista_de_palavras: list = arq_palavras.read().split(";")

        #  Aqui a clase 'set' ajuda a remover palavras duplicadas
        # que existem no arquivo.
        lista_de_palavras: set = set(map(verifica, lista_de_palavras))

        arq_palavras.close()

    #  Aqui eu transformo o 'set' novamente em lista para o acesso mais fácil
    # pelos outros módulos e retorna.
    return list(lista_de_palavras)
