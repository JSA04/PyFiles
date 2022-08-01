from Termo_Utils.Termo import Termo


def executa_acao(jogo : Termo):
    while True:
        acao = input("O Que Quer Fazer? ").strip()

        if acao == "1":
            jogo._play()
            return 1
        elif acao == "2":
            jogo._streak()
            return 2
        elif acao == "3":
            jogo._leave()
            return 3

        if acao.isnumeric():
            print("\033[31mDigite um desses números!\033[m")
            continue
        else:
            print("\033[31mDigite um número!\033[m")
            continue


