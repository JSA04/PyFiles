class Termo:
    def __init__(self, tipo_base_de_dados):

        from utils import escolhe, database

        self.base = database(tipo_base_de_dados)

        self.tentativas = []
        self.rodada = 0
        self.palavra_certa = escolhe(self)
        self.tentativa_atual = ""
        print(self.palavra_certa)

    def start(self):

        from utils import pede_e_confere_tentativa, Conferidor


        for round in range(0, 6):

            self.rodada = round

            tentativa = pede_e_confere_tentativa(self)


            conferidor = Conferidor(
               tentativa, self.palavra_certa
            )


            self.tentativas.append(
                conferidor.retorna_obj_Tentativa()
            )

            for obj in self.tentativas:
                obj.imprime_tentativa()

            if conferidor.esta_correto:
                break
