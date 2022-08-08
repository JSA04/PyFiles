from .confere_tentativa import Conferidor_de_Tentativa
from .escolhe_palavra import escolhe_palavra
from .trata_input import trata_input
from Termo_Utils.utils import acresenta_partida, retorna_streak
from Termo_Utils.Termo import Termo


def play(cls: Termo):
    cls.palavra_certa_atual = escolhe_palavra(cls)

    cls._limpa_terminal()

    if cls.tentativas:
        cls._reseta_dados()

    for round in range(0, 6):

        cls.rodada = round

        trata_input(cls)
        conferidor = Conferidor_de_Tentativa(cls)
        conferidor.add_tentativa_a_lista(cls)

        for tentativa in cls.tentativas:
            print(tentativa.imprime_tentativa())

        if conferidor.esta_correto:
            acresenta_partida("G")
            print("\033[32mParabens! Você Venceu!")
            print(f"Seu Streak É De {retorna_streak()}.\033[m")
            break

        elif not conferidor and cls.rodada == 6:
            acresenta_partida("P")
            print("\033[31mGAME OVER!\033[m")

    cls._reseta_dados()
    cls._pausa()
    cls._limpa_terminal()
