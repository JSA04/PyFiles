from flask import (Flask, flash, redirect, url_for,
                   session, render_template, request)
import os

from models import Jogo
from dao import JogoDao, UsuarioDao
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "sec"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "flask"
app.config["MYSQL_PASSWORD"] = "PythonFlask@2022"
app.config["MYSQL_DB"] = "jogoteca"
app.config["MYSQL_PORT"] = 3306
app.config["UPLOAD_PATH"] = (
    os.path.dirname(os.path.abspath(__file__)) + "/uploads")

db = MySQL(app)

jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)


def confere_login(retorna):
    if "usuario_logado" not in session:
        session["usuario_logado"] = None

    usuario_nao_esta_logado = not session['usuario_logado']

    if usuario_nao_esta_logado:
        flash("Você precisa estar logado para acessar este site.")
        return redirect(url_for('login'))
    return retorna


@app.route('/')
def index():
    session["site_atual"] = "index"
    gamelist = jogo_dao.listar()
    return confere_login(render_template('lista.html', title="Jogos",
                                         jogos=gamelist))


@app.route("/novo")
def novo():
    session["site_atual"] = "novo"
    return confere_login(render_template('novo.html', title="Novo Jogo"))


@app.route("/criar", methods=["POST", ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    imagem = request.files["arquivo"]
    jogo = Jogo(nome, categoria, console)
    jogo_dao.salvar(jogo)

    extencao = imagem.filename[imagem.filename.find("."):]
    upload_path = app.config['UPLOAD_PATH']
    imagem.save(f"{upload_path}/{jogo.nome}.{extencao}")

    return redirect(url_for("index"))


@app.route("/vizualizar/<int:id>")
def vizualizar(id):
    session["site_atual"] = "vizualizar"
    jogo = jogo_dao.busca_por_id(id)
    return confere_login(render_template('vizualizar.html', jogo=jogo,
                                         title="Vizualização do Jogo"))


@app.route("/editar/<int:id>")
def editar(id):
    session["site_atual"] = "editar"
    jogo = jogo_dao.busca_por_id(id)
    return confere_login(render_template('editar.html', jogo=jogo,
                                         title="Editando jogo"))


@app.route("/atualizar", methods=["POST", ])
def atualizar_jogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    id = request.form['id']
    jogo = Jogo(nome, categoria, console, id=id)
    jogo_dao.salvar(jogo)
    return redirect(url_for("index"))


@app.route("/deletar_jogo/<int:id>")
def deletar_jogo(id):
    jogo = jogo_dao.busca_por_id(id)
    jogo_dao.deletar(jogo.id)
    flash(f"Jogo {jogo.nome} deletado com sucesso.")
    return confere_login(redirect(url_for("index")))


@app.route("/login")
def login():
    if not session["usuario_logado"]:
        return render_template("login.html", title="Login")
    else:
        return redirect(url_for("index"))


@app.route("/authenticate", methods=["POST", ])
def authenticate():
    usuario = request.form["username"]
    senha = request.form["password"]

    procura_usuario = usuario_dao.buscar_por_nome(usuario)

    if procura_usuario:
        confirma_senha = procura_usuario.senha == senha

        if confirma_senha:
            session["usuario_logado"] = {"id": procura_usuario.id,
                                         "nome": procura_usuario.nome,
                                         "senha": procura_usuario.senha}
            flash(f"Usuario {session['usuario_logado']['nome']} foi logado"
                  f" com sucesso")

            return redirect(url_for(session["site_atual"]))

    flash("Usuario não existe ou a senha esta incorreta.")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session['usuario_logado'] = None
    flash("Logout efetuado com sucesso.")
    return redirect(url_for("login"))


@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar.html", title="Cadastrar")


@app.route("/cadastra", methods=["POST", ])
def cadastra():
    usuario = request.form["username"].strip()
    senha = request.form["password"].strip()
    senha2 = request.form["confirma_password"].strip()
    confimacao_senha = senha == senha2

    if usuario and senha and senha2:
        if confimacao_senha:
            if len(senha) < 6:
                flash("Sua senha deve ter no minimo 6 digitos.")
                return redirect(url_for("cadastrar"))
            criacao = usuario_dao.criar(usuario, senha)
            if criacao:
                flash("Usuario criado com sucesso")
                return redirect(url_for("login"))
            else:
                flash("Já existe um usuario com este nome.")
        else:
            flash("As senhas não conferem")
    else:
        flash("Você deve preencher, totalmente, o formulario.")
    return redirect(url_for("cadastrar"))


@app.route("/configuracoes")
def configuracoes():
    return confere_login(render_template("configuracoes.html",
                                         conta=session["usuario_logado"],
                                         title="Configurações"))


@app.route("/deletar_usuario")
def deletar_usuario():
    id = str(session["usuario_logado"]["id"])
    usuario_dao.deletar_por_id(id)
    flash("Usuario deletado com sucesso.")
    return confere_login(redirect(url_for("logout")))


@app.route("/confirma_delecao")
def confirma_delecao():
    session["site_atual"] = "confirma_delecao"
    return confere_login(render_template("confirma_delecao.html",
                                         title="Confirmar deleção"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4444, debug=True)
