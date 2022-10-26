from random import randint
from cryptography.fernet import Fernet
from conf import conf
from datetime import date

def randomStr():
    val_char = "ABCDEFGHJabcdefghj1234567890"
    tot_chars = len(val_char) - 1

    retorno = ""
    for _ in range(0, 10):
        char = val_char[randint(0, tot_chars)]
        retorno += char

    return retorno


def addKey(key_bytes:bytes):
    while True:
        try:
            pathname = randomStr()
            key = key_bytes.decode("utf-8")
            with open(f"C:\\Users\\f72823\\PWKs\\{pathname}.key", mode="w") as pathname_ref:
                pathname_ref.write(f"{key}")
                pathname_ref.close()

        except FileExistsError:
            continue

        else:
            return pathname


def Enc(pw):
    key = Fernet.generate_key()
    enc = Fernet(key)

    return addKey(key), enc.encrypt(bytes(pw, "utf-8"))


def PW(username, password, creation=date.today()):

    kl, pw = Enc(str(password))
    con = conf("4dd")

    cursor = con.cursor()

    cursor.execute("INSERT INTO INFO (username, passwd, creation, kl) VALUES (%s, %s, %s, %s);",
    (username, pw, creation, kl))

    con.commit()
    con.close()
