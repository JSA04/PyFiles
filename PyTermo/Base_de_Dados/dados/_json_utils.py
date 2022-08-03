import json



class Leitor_JSON:
    arq_local = r"Base_de_Dados\dados\data.json"

    @classmethod
    def retorna_json(cls) -> dict:
        with open(cls.arq_local) as arq:
            return json.load(arq)

    @classmethod
    def escreve_json(cls, json_syntax) -> str:
        json_syntax = json.dumps(json_syntax)

        with open(cls.arq_local, mode="w") as arq:
            arq.write(json_syntax)

        return json_syntax
