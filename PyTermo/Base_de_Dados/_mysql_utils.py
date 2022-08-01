class Mysql_Base:

    def __init__(self, host="localhost",
                 user="root",
                 password="senha_mysql_juan"):

        import mysql.connector as mysql_base

        try:

            print("Carregando Base De Palavras...")

            self.db = mysql_base.connect(user=user,
                                    password=password,
                                    host=host)
            self.qtd_palavras = 0

        except Exception as err:
            print(f"\033[31mHouve um erro ao se conectar com o banco de dados."
                  f"ID do ERRO:{err}\033[m")

        else:
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

    def adiciona_palavras(self) -> None:

        from Base_de_Dados.dados.palavras_dao import retorna_palavras

        self.conecta_db()

        cursor = self.db.cursor()
        cursor.execute("use termo")

        for p in retorna_palavras():
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


        existe = False

        for palavra in cursor:
            existe = True

        self.fecha_db()
        return existe



    def qtd_linhas(self) -> int:
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
        self.db.commit()
        self.db.close()

