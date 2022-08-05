from typing import Union


class Termo:
    def __init__(self):
        from .utils import retorna_base_de_dados
        from Base_de_Dados.database import database_mysql_termo, \
                                           database_pandas_termo

        self._limpa_terminal()

        # A função reseta dados, inicialmente cria alguns dados do jogo atual.
        self._reseta_dados()

        #  Guarda objeto da Base de Dados para efetuar para outros módulos 
        # executar querys e afins.
        self.base_de_dados: Union[database_mysql_termo,
                            database_pandas_termo] = retorna_base_de_dados()

        self.sair = False

        self._limpa_terminal()

    def roda(self) -> None:
        from .utils import retorna_json, atualiza_json
        print("Seja bem vindo ao Termo!\n")

        while True:
            from .acao import executa_acao

            #  O módulo "executa_acao" pergunta ao usuario o que ele deseja
            # fazer e depois executa uma função dessa classe que faz o que
            # o usuario deseja.

            acao = executa_acao(self)

            if self.sair:
                break

        self._limpa_terminal()

        base = retorna_json()["Base"]
        if base == "MySQL":
            self.base_de_dados.db.close()

    def _play(self):

        from Termo_Utils.utils import (Conferidor_de_Tentativa, trata_input, escolhe_palavra,
                            acresenta_streak, retorna_streak, acresenta_partida)

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
                print(tentativa.imprime_tentativa())

            if conferidor.esta_correto:
                acresenta_partida("G")
                print("\033[32mParabens! Você Venceu!")
                print(f"Seu Streak É De {retorna_streak()}.\033[m")
                break

            elif not conferidor and self.rodada == 6:
                acresenta_partida()
                print("\033[31mGAME OVER!\033[m")


        self._reseta_dados()
        self._pausa()
        self._limpa_terminal()

    def _status(self) -> None:
        from .utils import retorna_json

        dados = retorna_streak()

        self._limpa_terminal()

        print("Seu Status\n")
        print(f"Ganhas: {dados['Partidas_Ganhas']}")
        print(f"Perdidas: {dados['Partidas_Perdidas']}")
        print(f"Total: {dados['Total_Partidas']}")
        print(f"Streak: {dados['Streak']}")

        self._pausa()
        self._limpa_terminal()

    def muda_configuracao_DB(self) -> None:
        from .utils import mostra_pede_para_mudar_DB

        self._limpa_terminal()

        mostra_pede_para_mudar_DB(self)

        self.base_de_dados
        self._limpa_terminal()

    def _leave(self) -> None:
        self._limpa_terminal()

        print("Até Mais!")

        self.sair = True

        self._pausa()

    @staticmethod
    def _pausa() -> None:
        from os import system

        system("pause")

    @staticmethod
    def _limpa_terminal() -> None:
        from os import system

        system("cls")

    def _reseta_dados(self):
        self.tentativas = []
        self.rodada = 0
        self.tentativa_atual = ""
        self.palavra_certa_atual = ""
