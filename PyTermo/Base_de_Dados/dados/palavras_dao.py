from .constantes import CAMINHO_ARQUIVO_PALAVRAS, \
                       CARACTERES_INVALIDOS


def verifica(palavra: str) -> bool:

    for caracter in CARACTERES_INVALIDOS:

        if (caracter.upper() in palavra.upper() or 
            len(palavra.strip()) != 5):
            break

    return palavra


def retorna_palavras():
    with open(CAMINHO_ARQUIVO_PALAVRAS, mode="r+", encoding="UTF-8") as arq_palavras:
        lista_de_palavras = arq_palavras.read().split(";")
        
        return list(map(verifica, lista_de_palavras))
