from typing import Union

from fila_normal import FilaNormal
from fila_preferencial import FilaPreferencial
from constantes import TIPO_FILA_PREFERENCIAL, TIPO_FILA_NORMAL


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila: str) -> Union[FilaNormal, FilaPreferencial]:
        tipo_fila = tipo_fila.lower().strip()
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PREFERENCIAL:
            return FilaPreferencial()
        else:
            raise NotImplementedError()
