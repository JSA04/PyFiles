class Termo:
    def __init__(self):
        from .utils import retorna_base_de_dados

        self._limpa_terminal()

        # A função reseta dados, inicialmente cria alguns dados do jogo atual.
        self._reseta_dados()

        # Guarda objeto da Base de Dados para efetuar para outros módulos executar querys e afins.
        self.base_de_dados = retorna_base_de_dados()

        self._limpa_terminal()

    def roda(self):
        from Base_de_Dados.json_utils import retorna_json
        print("Seja bem vindo ao Termo!\n")

        while True:
            from .acao import executa_acao

            #  O módulo "executa_acao" pergunta ao usuario o que ele deseja
            # fazer e depois executa uma função dessa classe que faz o que
            # o usuario deseja.

            acao = executa_acao(self)

            if acao == "LEAVE":
                self._limpa_terminal()
                break
            elif acao == "SEM_DB":
                self._limpa_terminal()
                print("\033[31mÉ Preciso Uma Base Base De Dados Para Continuar.\033[m")

        base = retorna_json()["Base"]
        if base == "MySQL":
            self.base_de_dados.db.close()

    def _play(self):

        from Termo_Utils.utils import (Conferidor_de_Tentativa, trata_input, escolhe_palavra,
                            acresenta_streak, retorna_streak, reseta_streak)

        self.palavra_certa_atual = escolhe_palavra(self)

        self._limpa_terminal()

        if self.tentativas:
            self._reseta_dados()

        for round in range(0, 6):

            self.rodada : int = round

            trata_input(self)
            conferidor = Conferidor_de_Tentativa(self)
            conferidor.add_tentativa_a_lista(self)

            for tentativa in self.tentativas:
                print(tentativa)

            if conferidor.esta_correto:
                acresenta_streak()
                print("\033[32mParabens! Você Venceu!")
                print(f"Seu Streak É De {retorna_streak()}.\033[m")
                break

            elif not conferidor and self.rodada == 6:
                print("\033[31mGAME OVER!\033[m")
                reseta_streak()

        self._reseta_dados()
        self._pausa()
        self._limpa_terminal()

    def _streak(self):
        from Termo_Utils.utils import retorna_streak

        streak = retorna_streak()

        self._limpa_terminal()

        print(f"Seu Streak É De {streak}")

        self._pausa()
        self._limpa_terminal()

    def muda_configuracao_DB(self):
        from Termo_Utils.utils import mostra_pede_para_mudar_DB

        self._limpa_terminal()

        mostra_pede_para_mudar_DB(self)

        self.base_de_dados
        self._limpa_terminal()

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

    def _reseta_dados(self):
        self.tentativas = []
        self.rodada = 0
        self.tentativa_atual = ""
        self.palavra_certa_atual = ""
