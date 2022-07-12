from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO, TIPO_ESTATISTICA


class FilaPreferencial(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_preferencial_atendidos.append(cliente_atual)
        return f"Cliente atual: {cliente_atual}, digirija-se ao caixa {caixa}."

    def estatistica(self, retorna_estatistica: TIPO_ESTATISTICA) -> dict:
        return retorna_estatistica.roda_estatistica(
            self.clientes_preferencial_atendidos
        )
