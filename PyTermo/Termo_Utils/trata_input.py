from Termo_Utils.confere_palavra import confere
from Termo import Termo


def pede_e_confere_tentativa(jogo : Termo) -> str:
    while True:
        palavra = str(input(f"{jogo.rodada + 1} - Tentativa: "))
        palavra = palavra.upper().replace(" ", "")

        jogo.tentativa_atual = palavra

        if confere(jogo):
            break

    return palavra
