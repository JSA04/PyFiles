from typing import Union

from Termo_Utils.Termo import Termo


def executa_acao(cls : Termo) -> Union[str, None]:

    print("1 - Começar")
    print("2 - Ver Streak")
    print("3 - Configurações Da Base De Dados")
    print("4 - Sair\n")

    while True:

        acao = input("O Que Quer Fazer? ").strip()

        if acao == "1":

            if cls.base_de_dados is not None:
                cls._play()
                return None
            else:
                return "SEM_DB"

        elif acao == "2":
            cls._streak()
            return None

        elif acao == "3":
            cls.muda_configuracao_DB()
            return None

        elif acao == "4":
            cls._leave()
            return "LEAVE"

        if acao.isnumeric():
            print("\033[31mDigite um desses números!\033[m")
            continue
        else:
            print("\033[31mDigite um número!\033[m")
            continue


