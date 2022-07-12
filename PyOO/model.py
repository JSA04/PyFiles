class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._likes}% Gostaram"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.duracao} min - " \
               f"{self.likes}% Gostaram"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporadas} - " \
               f"{self.likes}% Gostaram"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


filme1 = Filme("vingadores", 2018, 240)
serie1 = Serie("atlanta", 2018, 2)
filme2 = Filme("todo mundo em pânico", 1999, 100)
serie2 = Serie("Demolidor", 2016, 2)


filmes_e_series = [filme1, serie1, serie2, filme2]
playlist_fim_de_semana = Playlist("Fim de Semana", filmes_e_series)

print(f"Tamanho da playlist {len(playlist_fim_de_semana)}")

for programa in playlist_fim_de_semana:
    print(programa)
