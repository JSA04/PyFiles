import json

arq_local : str = r".\Base_de_Dados\dados\data.json"


def retorna_json() -> dict:
    with open(arq_local) as arq:
        return json.load(arq)


def atualiza_json(json_syntax : dict) -> None:

    json_atualizado = json.dumps(json_syntax)

    with open(arq_local, mode="w") as arq:
        arq.write(json_atualizado)
