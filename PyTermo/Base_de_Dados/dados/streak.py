arq_local = r"C:\Users\f72823\Documentos\PyFiles\PyTermo\Base_de_Dados\dados\stk"


def atualiza_e_retorna_streak():
    stk = None
    with open(arq_local, "r") as arq:
        stk = int(arq.readline()) + 1
        with open(arq_local, "w") as arq2:
            arq2.write(str(stk))

        arq.close()
    return stk


def retorna_streak():
    with open(arq_local, "r") as arq:
        stk = int(arq.readline())
        arq.close()

    return stk


a = retorna_streak()
