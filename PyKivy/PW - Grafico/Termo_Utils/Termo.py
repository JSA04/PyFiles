class Termo:
    def __init__(self):
        from Termo_Utils.utils import Base

        # A função reseta dados, inicialmente cria alguns dados do jogo atual.
        self._reseta_dados()

        #  Guarda objeto da Base de Dados para outros módulos
        # executar queries e afins.
        self.base_de_dados = Base

        self.sair = False

        self._limpa_terminal()

    def roda(self) -> None:
        from Termo_Utils.utils import roda
        
        roda(self)

    def _play(self):
        from Termo_Utils.utils import play
        
        play(self)
        
    def _status(self) -> None:
        from Termo_Utils.utils import status

        status(self)

    def _leave(self) -> None:
        self._limpa_terminal()

        print("Até Mais!")

        self.sair = True

        self._pausa()

    @staticmethod
    def _pausa() -> None:
        from os import system

        print()
        system("pause")

    @staticmethod
    def _limpa_terminal() -> None:
        from os import system

        print()
        system("cls")

    def _reseta_dados(self):
        self.tentativas = []
        self.rodada = 0
        self.tentativa_atual = ""
        self.palavra_certa_atual = ""
