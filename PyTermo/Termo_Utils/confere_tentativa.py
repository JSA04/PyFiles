from Termo_Utils.Tentativa import Tentativa
from Termo_Utils.confere_igualdade import Igualador
from .Termo import Termo


class Conferidor_de_Tentativa:
    def __init__(self, cls : Termo):
        self.tentativa = cls.tentativa_atual
        self.palavra = cls.palavra_certa_atual

    @property
    def esta_correto(self) -> bool:
        return self.palavra == self.tentativa or self.tentativa == "PTCPA"

    @staticmethod
    def add_tentativa_a_lista(cls: Termo):
        igualdade = Igualador(cls)

        obj_tentativa = Tentativa(cls.tentativa_atual, igualdade.verifica_igualdade())

        cls.tentativas.append(obj_tentativa)

