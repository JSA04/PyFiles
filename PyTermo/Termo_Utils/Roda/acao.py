from typing import Union

from Termo_Utils.Termo import Termo


def executa_acao(cls: Termo) -> Union[str, None]:

    while True:

        print("1 - Começar")
        print("2 - Ver Meus Status")
        print("3 - Configurações Da Base De Dados")
        print("4 - Sair\n")

        acao = input("O Que Quer Fazer? ").strip()

        if acao == "1":

            if cls.base_de_dados is not None:
                return cls._play()
            else:
                cls._limpa_terminal()
                print("\033[31mÉ Preciso Uma Base De Dados Para Continuar."
                      "\033[m")

        elif acao == "2":
            return cls._status()

        elif acao == "3":
            return cls.muda_configuracao_DB()

        elif acao == "4":
            return cls._leave()

        elif acao.isnumeric():
            print("\033[31mDigite um desses números!\033[m")
            continue
        else:
            print("\033[31mDigite um número!\033[m")
            continue
