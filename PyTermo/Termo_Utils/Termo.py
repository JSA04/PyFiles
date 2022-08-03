class Termo:
    def __init__(self):
        from .utils import retorna_base_de_dados

        self._limpa_terminal()

        # Guarda dados do jogo para ser acessado por outro módulo.
        self.tentativas = []
        self.rodada = 0
        self.tentativa_atual = ""
        self.palavra_certa_atual = ""

        # Guarda objeto da Base de Dados para efetuar para outros módulos executar querys e afins.
        self.base_de_dados = retorna_base_de_dados()

        self._limpa_terminal()

    def roda(self):

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

            self._limpa_terminal()

    def _play(self):

        from .utils import (Conferidor_de_Tentativa, trata_input, escolhe_palavra,
                            acresenta_streak, retorna_streak, reseta_streak)

        self.palavra_certa_atual = escolhe_palavra(self)

        self._limpa_terminal()

        if self.tentativas:
            self.reseta_dados()

        print(self.palavra_certa_atual)
        for round in range(0, 6):

            self.rodada = round

            trata_input(self)
            conferidor = Conferidor_de_Tentativa(self)
            conferidor.add_tentativa_a_lista(self)

            for obj in self.tentativas:
                obj.imprime_tentativa()

            if conferidor.esta_correto:
                acresenta_streak()
                print("\033[32mParabens! Você Venceu!")
                print(f"Seu Streak É De {retorna_streak()}.\033[m")
                break

            elif not conferidor and self.rodada == 6:
                print("\033[31mGAME OVER!\033[m")
                reseta_streak()

        self.reseta_dados()
        self._pausa()
        self._limpa_terminal()

    def _streak(self):
        from .utils import retorna_streak

        stk = retorna_streak()

        print(f"Seu Streak É De {stk}")

        self._pausa()
        self._limpa_terminal()

    def _configuracao_base(self):

        self._limpa_terminal()

        tipo = str(type(self.base_de_dados))
        base = "Pandas" if "Pandas" in tipo else "MySQL"
        print(f"Base_de_Dados_Atual: {base}\n")

        self._pede_e_muda_db()

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

    def _pede_e_muda_db(self):
        from Base_de_Dados.database import database_mysql_termo, database_pandas_termo
        from Base_de_Dados.dados._json_utils import Leitor_JSON

        resp = ""

        while resp not in ["SIM", "S", "NAO", "N"]:
            resp = input("Deseja Mudar A Base De Dados? ").upper()

            json = Leitor_JSON.retorna_json()

            if resp in ["SIM", "S"]:
                if json["Base"] == "MySQL":
                    json["Base"] = "Pandas"
                    self.base_de_dados = database_pandas_termo()
                else:
                    json["Base"] = "MySQL"
                    self.base_de_dados = database_mysql_termo()
            elif resp not in ["NAO", "N"]:
                print("\033[31mDigite SIM ou NAO:\033[m")

    def reseta_dados(self):
        self.tentativas = []
        self.rodada = 0
        self.tentativa_atual = ""
        self.palavra_certa_atual = ""
