class Mysql_Base:
    def __init__(self):
        from Base_de_Dados.MySQL.Conecta_MySQL.conecta_mysql import retorna_base
        self.db = retorna_base()

    def cria_tabela_palavras(self) -> None:
        self.reconecta_db()

        cursor = self.db.cursor()

        cursor.execute("DROP DATABASE if exists termo")
        cursor.execute("CREATE DATABASE termo")
        cursor.execute("USE termo")
        cursor.execute("CREATE TABLE palavras ("
                       " id int auto_increment,"
                       " palavra char(5),"
                       " primary key(id))")

        self.fecha_db()

    def adiciona_palavras(self) -> None:

        from Base_de_Dados.dados.palavras_dao import retorna_palavras

        self.reconecta_db()

        palavras = retorna_palavras()

        cursor = self.db.cursor()
        cursor.execute("use termo")

        for p in palavras:
            cursor.execute("INSERT INTO palavras (palavra) value (%s)", (p, ))

        self.fecha_db()

    def retorna_palavra_por_id(self, id) -> str:
        self.reconecta_db()

        cursor = self.db.cursor()

        cursor.execute("use termo")
        cursor.execute("SELECT palavra from palavras where id = %s", (id,))

        for id in cursor:
            self.fecha_db()
            return id[0]

    def verifica_palavra_no_db(self, palavra_a_conferir) -> bool:
        self.reconecta_db()

        cursor = self.db.cursor()

        cursor.execute("use termo")
        cursor.execute("SELECT palavra from palavras where palavra = %s",
                       (palavra_a_conferir,))

        existe = False

        for palavra in cursor:
            existe = True

        self.fecha_db()
        return existe

    def qtd_linhas(self):
        self.reconecta_db()

        cursor = self.db.cursor()

        cursor.execute("use termo")
        cursor.execute("SELECT count(palavra) from palavras")

        for count in cursor:
            self.fecha_db()
            return count[0]

    def reconecta_db(self) -> None:
        self.db.reconnect()

    def fecha_db(self) -> None:
        self.db.commit()
        self.db.close()
