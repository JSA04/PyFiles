from .Termo import Termo


class Igualador:

    def __init__(self, cls : Termo):
        self.tentativa : str = cls.tentativa_atual
        self.palavra : str = cls.palavra_certa_atual

    def verifica_igualdade(self) -> list:
        lista = []


        for i in range(0, 5):
            letra_certa, letra_tentativa = self.palavra[i], self.tentativa[i]
            if letra_tentativa == letra_certa:
                lista.append("\033[32m")

            elif letra_tentativa in self.palavra:
                if self._confere_em_outra_posicao(letra_tentativa):
                    lista.append("\033[33m")
                else:
                    lista.append("\033[31m")
            else:
                lista.append("\033[31m")

        return lista


    def _confere_em_outra_posicao(self, letra):
        letras_iguais_na_palavra = self.palavra.count(letra)
        letras_conferidas = 0

        for i in range(0, 5):
            letra_certa, letra_tentativa = self.palavra[i], self.tentativa[i]
            if letra_certa == letra and letra_certa == letra_tentativa:
                letras_conferidas += 1
            if letras_conferidas == letras_iguais_na_palavra:
                return False
        return True
