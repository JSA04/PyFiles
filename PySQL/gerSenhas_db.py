import mysql.connector as mysql
from senha import senha


class Gerenciador:
    def __init__(self):
        self.db = mysql.connect(host='localhost', user='root', password=senha)
        self._open_cursor()
        self.executar("use gsdb")

    def _open_cursor(self):
        self.cursor = self.db.cursor()

    def executar(self, query, query2=()):
        if query2:
            self.cursor.execute(query, query2)
        else:
            self.cursor.execute(f"{query};")

    def cadastrar(self, usuario, servico, passwd, id=()):
        cadastro = [usuario, servico, passwd]
        self.executar(f"INSERT INTO main(usuario, servico, senha) VALUES (%s, %s, %s)", cadastro)
        self.db.commit()

    def fechar(self):
        self.db.commit()
        self.cursor.close()
        self.db.close()

