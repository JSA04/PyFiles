from cryptography.fernet import Fernet
from conf import conf


def pega_chave_e_senha(usuario):
    con = conf("s3l")
    cursor = con.cursor()

    cursor.execute("select kl, passwd from info where username = %s", (usuario,))

    local = None
    pswd = None

    for row in cursor:
        local = row[0]
        pswd = row[1]

    con.close()

    try:
        with open(f"C:\\Users\\f72823\\PWKs\\{local}.key") as arq:
            key = arq.read()
            arq.close()
            return bytes(key, "utf-8"), bytes(pswd, "utf-8")
    except FileNotFoundError:
        return None, None


def confere_senha(usuario="", tentativa=""):
    log = ""
    if not usuario or not tentativa:

        if not usuario:
            log += "Usuario não informado.\n"
        if not tentativa:
            log += "Senha não informada."
        return log

    key, senha = pega_chave_e_senha(usuario)

    if key is None or senha is None:
        return "Senha ou Usuário Incorreto."

    if Fernet(key).decrypt(senha) == bytes(tentativa, "utf-8"):
        return True
    else:
        return "Senha ou Usuário Incorreto."


