class Jogo:
    def __init__(self, nome: str, categoria: str,
                 console: str, id=None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.console = console


class Usuario:
    def __init__(self, id, nome, senha, ):
        self.id: int = id
        self.nome: str = nome
        self.senha: str = senha
