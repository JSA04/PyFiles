class Igualdade:

    def __init__(self, tentativa, palavra_certa):
        self.letras_corretas = []
        self.tentativa : str = tentativa
        self.palavra : str = palavra_certa

    def verifica_igualdade(self) -> list:
        lista = []


        for letra in range(0, 5):
            if self.tentativa[letra] == self.palavra[letra]:
                lista.append("\033[32m")

            elif (self.tentativa[letra] in self.palavra and
                  self._confere_em_outra_posicao(self.tentativa[letra])):
                lista.append("\033[33m")
            else:
                lista.append("\033[31m")

        return lista


    def _confere_em_outra_posicao(self, letra):

        qtd_letras_iguais = self.palavra.count(letra)
        letras_semelhantes_atual = 0

        for i in range(0, 5):
            if self.tentativa[i] == self.palavra[i]:
                letras_semelhantes_atual += 1
                if qtd_letras_iguais == letras_semelhantes_atual:
                    return False

        return True
