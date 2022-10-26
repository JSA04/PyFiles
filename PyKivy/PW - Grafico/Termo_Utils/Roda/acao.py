from typing import Union

from Termo_Utils.Termo import Termo


def executa_acao(cls: Termo) -> Union[str, None]:

    while True:

        print("1 - Começar")
        print("2 - Ver Meus Status")
        print("3 - Configurações Da Base De Dados")
        print("3 - Sair\n")

        acao = input("O Que Quer Fazer? ").strip()

        if acao == "1":
            return cls._play()

        elif acao == "2":
            return cls._status()

        elif acao == "3":
            return cls._leave()

        elif acao.isnumeric():
            print("\033[31mDigite um desses números!\033[m")
            continue
        else:
            print("\033[31mDigite um número!\033[m")
            continue
