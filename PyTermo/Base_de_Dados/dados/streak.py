from Base_de_Dados.json_utils import retorna_json, escreve_json


def acresenta_streak() -> None:

    dados: dict = retorna_json()
    dados["Streak"] += 1
    escreve_json(dados)


def reseta_streak() -> None:

    dados: dict = retorna_json()
    dados["Streak"]: int = 0
    escreve_json(dados)


def retorna_streak() -> str:

    dados: dict = retorna_json()
    streak = dados["Streak"]
    return streak
