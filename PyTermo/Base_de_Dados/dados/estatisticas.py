from Base_de_Dados.dados.json_utils import retorna_json, atualiza_json


def altera_estatisticas(resultado_partida: str) -> None:
    dados = retorna_json()

    if resultado_partida.upper() == "P":
        dados["Partidas_Perdidas"] += 1
        dados["Streak"] = 0

    elif resultado_partida.upper() == "G":
        dados["Partidas_Ganhas"] += 1
        dados["Streak"] += 1


    dados["Total_Partidas"] += 1
    atualiza_json(dados)


def retorna_streak():
    dados = retorna_streak()
    return dados["Streak"]
