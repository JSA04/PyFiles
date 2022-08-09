class Tentativa:
    def __init__(self, tentativa, verificacao: list):
        self.tentativa = tentativa
        self.verificacao = verificacao

    def imprime_tentativa(self) -> None:
        for i in range(0, 5):
            print(f"{self.verificacao[i]}{self.tentativa[i]}\033[m", end="")

        print()

    def __str__(self):
        return self.tentativa
