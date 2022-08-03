from Termo_Utils.Termo import Termo


def confere(cls : Termo) -> bool:
    if cls.tentativa_atual == "PTCPA":
        return True

    if not cls.tentativa_atual:
        print("\033[31mVocê deve digitar uma palavra\033[m")
        return False

    elif len(cls.tentativa_atual) != 5:
        print("\033[31mVocê deve digitar uma palavra com 5 letras\033[m")
        return False

    elif not cls.base_de_dados.verifica_palavra_no_db(cls.tentativa_atual):
        print("\033[31mA palavra que você digitou não está na nossa base de dados\033[m")
        return False

    return True
