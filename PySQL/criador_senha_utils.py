def deve_estar(*args, em=("S", "SS", "SIM", "N", "NN", "NAO", "NÃO")):
    r = False

    for arg in args:
        if arg.upper() in em:
            r = True
        else:
            r = False

    return r


def quantidade_digitos():
    while True:
        try:
            input_numeros = int(input("Quantos digitos terá a senha?\n"))

            if input_numeros == 0:
                raise SyntaxError

        except ValueError:
            print("\033[31mVocê deve digitar um número.\033[m")
            continue

        except SyntaxError:
            print("\033[31mVocê deve digitar um número.\033[m")
            continue

        else:
            if input_numeros < 8:
                print("\033[01mRecomendamos uma senha com pelo menos 8 digitos\033[m")
                while True:
                    dc: "Deseja Continuar" = input("Deseja continuar?\n").upper()
                    if deve_estar(dc):
                        if "S" in dc:
                            return input_numeros
                    else:
                        print("\033[31mVocê deve digitar Sim ou Não.\033[m")
                        continue
                    break
            else:
                return input_numeros


def letras():
    while True:
        input_letras = input("Quer letras na senha?\n").upper()

        if deve_estar(input_letras):
            if input_letras in "SSIM":
                input_letras = "SIM"
            else:
                input_letras = "NAO"
        else:
            print("\033[31mVocê deve digitar Sim ou Não.\033[m")
            continue
        return input_letras


def tipo_letra():
    while True:
        print("""\033[07;34m 1 - Maiúscula    \033[m
\033[07;34m 2 - Minúscula    \033[m
\033[07;34m 3 - Ambas        \033[m
        """)
        try:
            tipo = int(input("Digite o número do tipo de caracter que deseja:\n"))
        except ValueError:
            print("\033[31mVocê deve digitar um número.\033[m")
            continue
        else:
            if 0 < tipo <= 3:
                return tipo
            else:
                print(f"\033[31mO número {tipo} não existe.\033[m")


def numeros():
    while True:
        input_nums = input("Quer numeros na senha?\n").upper()

        if deve_estar(input_nums):
            if input_nums in "SSIM":
                input_nums = "SIM"
            else:
                input_nums = "NAO"
        else:
            print("\033[31mVocê deve digitar Sim ou Não.\033[m")
            continue
        return input_nums


def caracteres_especiais():
    while True:
        input_ce = input("Quer caracteres especiais na senha?\n").upper()

        if deve_estar(input_ce):
            if input_ce in "SSIM":
                input_ce = "SIM"
            else:
                input_ce = "NAO"
        else:
            print("\033[31mVocê deve digitar Sim ou Não.\033[m")
            continue

        return input_ce


def caracteres_escolhidos(estrutura):
    caracteres = []
    if estrutura["letras"] == "SIM":
        ambos = estrutura["tipo_letras"] == 3
        lista_letras = ['a', 'b', "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z"]
        if estrutura["tipo_letras"] == 1 or ambos:
            for letra in lista_letras:
                caracteres.append(letra.upper())
        if estrutura["tipo_letras"] == 2 or ambos:
            for letra in lista_letras:
                caracteres.append(letra)
    if estrutura["numeros"] == "SIM":
        nums = [num for num in range(0, 10)]
        for num in nums:
            caracteres.append(int(num))
    if estrutura["especiais"] == "SIM":
        car = ["*", "-", "!", "&", "%", "$", "#", "@"]
        for num in car:
            caracteres.append(num)
    return caracteres


def senha(estrutura, caracteres):
    from random import randint
    tot_dig = estrutura["digitos"]
    passwd = ""
    for dig in range(0, tot_dig):
        al = randint(0, len(caracteres) - 1)
        passwd += str(caracteres[al])

    return passwd


def __tem_sim(estrutura):
    items = [i for i in estrutura.values()]
    tem_sim = False
    s = ["SIM", "S"]
    for item in items:
        if str(item) in s:
            tem_sim = True
            break

    return tem_sim
