import json


arq_local = r".\Base_de_Dados\dados\data.json"


def retorna_json() -> dict:

    with open(arq_local) as arq:
        return json.load(arq)


def escreve_json(json_syntax) -> str:

    json_syntax = json.dumps(json_syntax)
    with open(arq_local, mode="w") as arq:
        arq.write(json_syntax)

    return json_syntax
