import flask_mysqldb

from models import Jogo, Usuario

SQL_DELETA_JOGO = 'delete from jogo where id = %s limit 1'
SQL_DELETA_USUARIO = 'DELETE from usuario where id = %s limit 1'
SQL_JOGO_POR_ID = 'SELECT id, nome, categoria, console from jogo where id = %s'
SQL_USUARIO_POR_ID = 'SELECT id, nome, senha from usuario where id = %s'
SQL_USUARIO_POR_NOME = 'SELECT id, nome, senha from usuario where nome = %s'
SQL_ATUALIZA_JOGO = 'UPDATE jogo set nome=%s ,categoria=%s, console=%s ' \
                    'where id=%s limit 1'
SQL_BUSCA_JOGOS = 'SELECT id, nome, categoria, console from jogo'
SQL_CRIA_USUARIO = 'INSERT INTO usuario (nome, senha) values (%s, %s)'
SQL_CRIA_JOGO = 'INSERT into jogo (nome, categoria, console) values ' \
                '(%s, %s, %s)'


class JogoDao:
    def __init__(self, db) -> None:
        self.__db: flask_mysqldb.MySQL = db

    def salvar(self, jogo: Jogo) -> Jogo:
        cursor = self.__db.connection.cursor()

        if jogo.id:
            cursor.execute(SQL_ATUALIZA_JOGO, (jogo.nome, jogo.categoria,
                                               jogo.console, jogo.id))
        else:
            cursor.execute(SQL_CRIA_JOGO, (jogo.nome, jogo.categoria,
                                           jogo.console))

        self.__db.connection.commit()
        return jogo

    def listar(self) -> list:
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_JOGOS)
        jogos = traduz_jogos(cursor.fetchall())
        return jogos

    def busca_por_id(self, id) -> Jogo:
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_JOGO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def deletar(self, id) -> None:
        self.__db.connection.cursor().execute(SQL_DELETA_JOGO, (id, ))
        self.__db.connection.commit()


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def criar(self, nome, senha) -> bool:
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_NOME, (nome, ))
        existe = cursor.fetchone()
        if not existe:
            cursor.execute(SQL_CRIA_USUARIO, (nome, senha))
            self.__db.connection.commit()
            return True
        self.__db.connection.commit()
        return False

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario

    def buscar_por_nome(self, nome) -> Usuario:
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_NOME, (nome,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario

    def deletar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETA_USUARIO, (id, ))
        self.__db.connection.commit()


def traduz_jogos(jogos) -> list:
    def cria_jogo_com_tupla(tupla):
        return Jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_jogo_com_tupla, jogos))


def traduz_usuario(tupla: tuple) -> Usuario:
    return Usuario(tupla[0], tupla[1], tupla[2])
