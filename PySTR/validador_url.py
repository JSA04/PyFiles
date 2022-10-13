url = "http://www.bytebank.com.br/cambio"

import re

padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
padrao = padrao_url.match(url)

if padrao:
    print("URL Valida!")
else:
    raise ValueError("\033[34mURL Invalida!")
