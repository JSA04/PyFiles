from .confere_palavra import confere
from .Termo import Termo


def trata_input(cls: Termo) -> str:
    while True:
        palavra = str(input(f"{cls.rodada + 1} - Tentativa: ")).upper().replace(" ", "")

        cls.tentativa_atual = palavra

        if confere(cls):
            break

    return palavra
