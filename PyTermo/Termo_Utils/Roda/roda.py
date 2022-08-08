def roda(cls):
    print("Seja bem vindo ao Termo!\n")

    while True:
        from Termo_Utils.Roda.acao import executa_acao

        #  O módulo "executa_acao" pergunta ao usuario o que ele deseja
        # fazer e depois executa uma função dessa classe que faz o que
        # o usuario deseja.

        executa_acao(cls)

        if cls.sair:
            break

    cls._limpa_terminal()
