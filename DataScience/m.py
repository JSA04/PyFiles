import utils._preenche_bairros
from utils.utils import DataFrame_Aluguel_Utils as dau

df = dau()

df.cria_tabela_inteira()

print(df.df)
