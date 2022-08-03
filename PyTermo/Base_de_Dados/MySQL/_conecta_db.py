from mysql import connector as conector


def retorna_base():
    global base

    from Base_de_Dados.dados._json_utils import retorna_json

    dados = retorna_json()

    try:
        base = conector.connect(host=dados["MySQL_Host"],
                                user=dados["MySQL_User"],
                                password=dados["MySQL_PW"])

    except Exception as err:
        _atualiza_base()

    else:
        base.close()
        return base


def _atualiza_base():
    from Base_de_Dados.dados._json_utils import retorna_json, escreve_json
    while True:
        try:
            dados = retorna_json()

            base = conector.connect(host=dados["MySQL_Host"],
                                    user=dados["MySQL_User"],
                                    password=dados["MySQL_PW"])

        except conector.errors.DatabaseError:

            print("\033[31mBase De Dados Não Encontrada.\033[m")

            dados = retorna_json()
            novos_dados = _pede_dados_da_base()

            dados["MySQL_Host"] = novos_dados["host"]
            dados["MySQL_User"] = novos_dados["user"]
            dados["MySQL_PW"] = novos_dados["passwd"]

            escreve_json(dados)

        else :

            return base


def _pede_dados_da_base() -> dict:
    from getpass import getpass

    print("\033[31mNão é possivel salvar esses dados utilizado o terminal 'RUN' "
          "do pycharm.\033[m")

    host = input("Qual é o host do banco de dados? (vazio para 'localhost')\n"
             "R: ").strip()

    if not host:
        host = "localhost"

    user = input("Qual é o usuário? (vazio para 'root') \nR: ").strip()

    if not user:
        user = "root"

    print("Qual a senha do usuário?")

    while True:
        passwd = getpass("R:").strip()
        if not passwd:
            print("\033[31mDigite uma senha.\033[m")
            continue
        break
    return {"host": host, "user": user, "passwd": passwd}


db = retorna_base()
