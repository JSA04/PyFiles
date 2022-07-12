import mysql.connector as mysql_base


class Mysql_Base:


    def __init__(self, host="localhost",
                 user="root",
                 password="senha_mysql_juan"):

        try:
            self.db = mysql_base.connect(user=user,
                                    password=password,
                                    host=host)
            self.cursor = self.db.cursor()
            self.qtd_palavras = 0

        except Exception as err:
            print(f"\033[31mHouve um erro ao se conectar com o banco de dados."
                  f"ID do ERRO:{err}\033[m")

        else:
            self.cursor.close()
            self.db.close()


    def cria_tabela_palavras(self) -> None:
        self.conecta_db()

        cursor = self.db.cursor()

        cursor.execute("DROP DATABASE if exists termo")
        cursor.execute("CREATE DATABASE termo")
        cursor.execute("USE termo")
        cursor.execute("CREATE TABLE palavras ("
                       " id int auto_increment,"
                       " palavra char(5),"
                       " primary key(id))")

        self.fecha_db()

    def adiciona_palavras(self, lista_de_palavras) -> None:
        self.conecta_db()

        cursor = self.db.cursor()

        cursor.execute("use termo")
        for p in lista_de_palavras:

            self.qtd_palavras += 1
            if p:
                cursor.execute("INSERT INTO palavras (palavra) value (%s)", p)

        self.fecha_db()

    def pega_palavra_por_id(self, id) -> str:
        self.conecta_db()

        cursor = self.db.cursor()

        cursor.execute("use termo")
        cursor.execute("SELECT palavra from palavras where id = %s", (id,))

        for id in cursor:
            self.fecha_db()
            return id[0]

    def verifica_palavra_no_db(self, palavra_a_conferir) -> bool:
        self.conecta_db()

        cursor = self.db.cursor()

        cursor.execute("use termo")
        cursor.execute("SELECT palavra from palavras where palavra = %s", (palavra_a_conferir,))

        for palavra in cursor:
            return True
        return False

    def qtd_linhas(self):
        self.conecta_db()

        cursor = self.db.cursor()

        cursor.execute("use termo")
        cursor.execute("SELECT count(palavra) from palavras")

        for count in cursor:
            self.fecha_db()
            return count[0]

    def conecta_db(self) -> None:
        self.db.reconnect()

    def fecha_db(self) -> None:
        self.cursor.close()
        self.db.commit()
        self.db.close()


def database_mysql_termo():
    # from Palavras.palavras_dao import palavras

    database = Mysql_Base()

    # database.adiciona_palavras(palavras)
    # Descomentar para adicionar palavras ao banco de dados.

    return database
