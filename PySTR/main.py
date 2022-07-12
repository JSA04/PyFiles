# url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

url = "   ".strip()

if url == "":
    raise ValueError("A URL está vazia.")

interrogacao = url.find("?")

url_base = url[:interrogacao]
url_param = url[interrogacao+1:]

parametro = "quantidade"
busca_parametro = url_param.find(parametro)
inicio_valor = busca_parametro + len(parametro) + 1

tem_outro_parametro = url_param.find("&", inicio_valor)
if tem_outro_parametro == -1:
    parametro = url_param[inicio_valor:]
else:
    parametro = url_param[inicio_valor:tem_outro_parametro]

print(parametro)
