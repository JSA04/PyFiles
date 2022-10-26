from Termo_Utils.utils import retorna_json
from Termo_Utils.Termo import Termo


def status(cls: Termo):
    cls._limpa_terminal()

    dados = retorna_json()  
    print("Seu Status\n")
    print(f"Ganhas: {dados['Partidas_Ganhas']}")
    print(f"Perdidas: {dados['Partidas_Perdidas']}")
    print(f"Total: {dados['Total_Partidas']}")
    print(f"Streak: {dados['Streak']}")

    cls._pausa()
    cls._limpa_terminal()
