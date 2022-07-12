class ExtratorURL:
    def __init__(self, url: str):
        self.url: str = self.sanitiza_url(url)
        self._valida_url()

    @staticmethod
    def sanitiza_url(url: str):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def _valida_url(self):
        import re

        padrao = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")

        if not self.url:
            raise ValueError("A URL está vazia.")

        if not padrao.match(self.url):
            raise ValueError("A URL não é valida.")

    @property
    def get_url_base(self):
        comeco_query: int = self.url.find("?")
        return self.url[: comeco_query]

    @property
    def get_url_parametros(self):
        comeco_query: int = self.url.find("?")
        return self.url[comeco_query + 1:]

    def get_valor_parametro(self, parametro: str):
        url_parametros: str = self.get_url_parametros

        busca_parametro: int = url_parametros.find(parametro)
        inicio_valor: int = busca_parametro + len(parametro) + 1

        tem_outro_parametro: int = url_parametros.find("&", inicio_valor)
        if tem_outro_parametro == -1:
            parametro: str = url_parametros[inicio_valor:]
        else:
            parametro: str = url_parametros[inicio_valor:tem_outro_parametro]

        return parametro

    def __len__(self):
       return len(self.url)

    def __str__(self):
        return f"URL Atual: {self.url}\nBase: {self.get_url_base}\nParâmetros: {self.get_url_parametros}"

    def __eq__(self, other):
        return self.url == other.url


url = "https://www.bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
ext = ExtratorURL(url)
ext2 = ExtratorURL(url)

print(ext == ext2)
