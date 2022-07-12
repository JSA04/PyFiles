from typing import List, Dict, Union


class EstatisticaResumida:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: List[str]) -> Dict:
        estatistica: Dict[str, Union[List[str], str, int]] = {
            "dia": self.dia,
            "agencia": self.agencia,
            "clientes_atendidos": clientes_atendidos,
            "quantidade_clientes_atendidos": (
                len(clientes_atendidos)
            )}

        return estatistica
