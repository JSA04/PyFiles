from Termo import Termo


def confere(jogo : Termo) -> bool:
    if not jogo.tentativa_atual:
        print("\033[31mVocê deve digitar uma palavra\033[m")

    elif len(jogo.tentativa_atual) != 5:
        print("\033[31mVocê deve digitar uma palavra com 5 letras\033[m")
        return False

    elif not jogo.base.verifica_palavra_no_db(jogo.tentativa_atual):
        print("\033[31mA palavra que você digitou não está na nossa base de dados\033[m")
        return False

    return True
