endereco = "Rua dos Patos 84, Jd. Quaqua, Frio de Janeiro, RS, 20220-150"

import re

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)
