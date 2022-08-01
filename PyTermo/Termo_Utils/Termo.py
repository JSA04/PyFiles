class Termo:
    def __init__(self, tipo_base_de_dados=""):
        from .utils import retorna_base_de_dados

        self._limpa_terminal()

        self.tentativas = []
        self.rodada = 0
        self.tentativa_atual = ""

        self.base_de_dados = retorna_base_de_dados(tipo_base_de_dados)

        self._limpa_terminal()

    def start(self):

        print("Seja bem vindo ao Termo!\n")

        while True:
            from Termo_Utils.acao import executa_acao

            print("1 - Jogar")
            print("2 - Ver Streak")
            print("3 - Sair\n")

            acao = executa_acao(self)

            if acao == 3:
                self._limpa_terminal()
                break

            self._limpa_terminal()

    def _play(self):

        from .utils import (pede_e_confere_tentativa, Conferidor,
                           escolhe_palavra, atualiza_e_retorna_streak)

        palavra_certa = escolhe_palavra(self)

        self._limpa_terminal()

        print(palavra_certa)
        for round in range(0, 6):

            self.rodada = round

            tentativa = pede_e_confere_tentativa(self)

            conferidor = Conferidor(tentativa, palavra_certa)

            self.tentativas.append(conferidor.retorna_obj_Tentativa)

            for obj in self.tentativas:
                obj.imprime_tentativa()

            if conferidor.esta_correto:
                print("\033[32mParabens! Você Venceu!")
                print(f"Seu Streak É De {atualiza_e_retorna_streak()}.\033[m")

                break
            elif not conferidor and tentativa == 6:
                print("\033[31mGAME OVER!\033[m")

        self._pausa()
        self._limpa_terminal()

    def _streak(self):
        from .utils import retorna_streak

        print(f"Seu Streak É De {retorna_streak()}")

        self._pausa()

    def _leave(self):
        self._limpa_terminal()

        print("Até Mais!")

        self._pausa()

    @staticmethod
    def _limpa_terminal():
        from os import system

        system("cls")

    @staticmethod
    def _pausa():
        from os import system

        system("pause")
