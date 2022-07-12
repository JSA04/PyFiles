from typing import Union
from estatisticas import EstatisticaResumida, EstatisticaDetalhada

CODIGO_PRIORITARIO: str = "PR"
CODIGO_NORMAL: str = "NM"

TAMANHO_PADRAO_MINIMO: int = 000
TAMANHO_PADRAO_MAXIMO: int = 300

TIPO_FILA_NORMAL: str = "normal"
TIPO_FILA_PREFERENCIAL: str = "preferencial"

TIPO_ESTATISTICA = Union[EstatisticaDetalhada, EstatisticaResumida]
