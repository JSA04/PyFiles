from mysql import connector as conector


def retorna_base():
    from Base_de_Dados.dados.json_utils import retorna_json, atualiza_json

    dados: dict = retorna_json()

    while True:

        try:
            database = conector.connect(host=dados["MySQL_Host"],
                                    user=dados["MySQL_User"],
                                    password=dados["MySQL_PW"])

        except conector.errors.DatabaseError:
            if dados["MySQL_User"]:
                print("\033[31mNão foi possivel se conectar.\033[m")

                continuar = input("Tentar Novamente?"
                                  "\nR:")

                if continuar.upper() in ["NAO", "N", "NA", "NÃO", "NÃ", "NO"]:
                    dados["Base"] = dados["MySQL_Host"] = \
                        dados["MySQL_User"] = \
                        dados["MySQL_PW"] = ""
                    atualiza_json(dados)
                    return None

            novos_dados = _pede_dados_da_base()

            dados["MySQL_Host"] = novos_dados["host"]
            dados["MySQL_User"] = novos_dados["user"]
            dados["MySQL_PW"] = novos_dados["passwd"]

        else:
            dados["Base"] = "MySQL"
            atualiza_json(dados)
            return database


def _pede_dados_da_base() -> dict:
    from getpass import getpass

    print("\nQual é o host do banco de dados? (vazio para 'localhost')")
    host = input("R: ").strip()

    if not host:
        host = "localhost"

    print("\nQual é o usuário? (vazio para 'root') ")
    user = input("R: ").strip()

    if not user:
        user = "root"

    print("\nQual a senha do usuário?")

    while True:
        passwd = getpass("R:").strip()
        if not passwd:
            print("\033[31mDigite uma senha.\033[m")
            continue
        break

    return {"host": host, "user": user, "passwd": passwd}
