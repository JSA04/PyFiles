def h1(txt: str):
    print(f"\033[1;4m"
          f"{txt}"
          f"\033[m")


def h2(txt: str):
    print(f"\n"
          f"\033[4m"
          f"{txt}"
          f"\033[m")


def h3(txt: str):
    print(f"\n"
          f"\033[2m"
          f"{txt}"
          f"\033[m")


class Npnt:
    indice = 1

    def pnt(self, metodo, explicacao : str):
        if self.indice != 1:
            print('\n')

        if explicacao[-1].strip() != ".":
            explicacao += "."

        print(f"{self.indice} - \033[3m'{metodo}'\n\n\033[m{explicacao}\n")

        self.acresenta_indice()

    @classmethod
    def acresenta_indice(cls):
        cls.indice += 1


npnt = Npnt()


def noteprint(metodo, explicacao):
    npnt.pnt(metodo, explicacao)
