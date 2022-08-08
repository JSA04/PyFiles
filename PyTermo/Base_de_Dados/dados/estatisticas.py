from Base_de_Dados.dados.json_utils import retorna_json, atualiza_json


def acresenta_partida(resultado_partida: str) -> None:
    dados = retorna_json()

    if resultado_partida.upper() == "P":
        dados["Partidas_Perdidas"] += 1
        _reseta_streak()

    elif resultado_partida.upper() == "G":
        dados["Partidas_Ganhas"] += 1
        _acresenta_streak()

    dados["Total_Partidas"] += 1
    atualiza_json(dados)


def _acresenta_streak() -> None:
    dados: dict = retorna_json()
    dados["Streak"] += 1
    atualiza_json(dados)


def _reseta_streak() -> None:
    dados: dict = retorna_json()
    dados["Streak"]: int = 0
    atualiza_json(dados)


def retorna_streak() -> str:
    dados: dict = retorna_json()
    streak = dados["Streak"]
    return streak
