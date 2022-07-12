from Termo_Utils.tentativa import Tentativa
from Termo_Utils.confere_igualdade import Igualdade


class Conferidor:
    def __init__(self, tentativa: str, palavra: str):
        self.tentativa = tentativa
        self.palavra = palavra

    @property
    def esta_correto(self) -> bool:
        return self.palavra == self.tentativa

    def retorna_obj_Tentativa(self) -> Tentativa:
        igualdade = Igualdade(self.tentativa, self.palavra)

        return Tentativa(self.tentativa, igualdade.verifica_igualdade())


