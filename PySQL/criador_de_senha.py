from random import randint
from senha_utils import *
from senha_utils import __tem_sim as ts

print("-" * 20 + " Cria Senha " + "-" * 20)


def __estrutura_senha():
    digs = quantidade_digitos()
    while True:
        lets = letras()
        let_tipo = ""
        if lets == "SIM":
            let_tipo = tipo_letra()
        nums = numeros()
        scar = caracteres_especiais()
        estrutura = {"digitos": digs, "letras": lets, "tipo_letras": let_tipo, "numeros": nums, "especiais": scar}
        if ts(estrutura):
            return estrutura
        print(f'\033[31mPara criar a senha precisamos que você digite "SIM" em pelo menos uma pergunta.\033[m')


def cria_senha():
    estrutura = __estrutura_senha()
    caracteres = caracteres_escolhidos(estrutura)
    pss = senha(estrutura=estrutura, caracteres=caracteres)
    print(f"A senha é \033[01m{pss}\033[m")


cria_senha()
