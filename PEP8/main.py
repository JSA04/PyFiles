from random import randint
from datetime import datetime

from fabrica_fila import FabricaFila
from estatistica_resumida import EstatisticaResumida

hoje = datetime.now()

fila_n = FabricaFila.pega_fila("Normal")
fila_p = FabricaFila.pega_fila("Preferencial")

for n in range(0, randint(0, 200)):
    fila_n.atualiza_fila()
    fila_n.chama_cliente(randint(1, 11))

    for p in range(0, randint(0, 1)):
        fila_p.atualiza_fila()
        fila_p.chama_cliente(randint(1, 11))

e_n = fila_n.estatistica(EstatisticaResumida(f"{hoje.date()}", 212))
e_p = fila_p.estatistica(EstatisticaResumida(f"{hoje.date()}", 212))

print(f"\nNo dia {e_n['dia']}, na agencia {e_n['agencia']} houve "
      f"{e_n['quantidade_clientes_atendidos']} clientes na Fila Normal.")


print(f"\nNo dia {e_p['dia']}, na agencia {e_p['agencia']} houve "
      f"{e_p['quantidade_clientes_atendidos']} clientes na Fila Preferencial.")
