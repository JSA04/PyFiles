from random import randint

pc = randint(1, 10)
pl = 0

tentativas = 0
while pl != pc:
    pl = int(input("Tente Adivinhar o número, de 1 a 10, em que estou pensando: "))
    if pl != pc:
        print("\033[31;1mVocê ERROU! tente mais uma vez.")
    tentativas += 1
    if pl > pc:
        print("O número que estou pensando é menor.\033[m")
    elif pl < pc:
        print("O número que estou pensando é maior.\033[m")

print("""\033[32;1mPARABENS! Você acertou, pois eu pensei no número {}.
E você precisou de {} tentativas para acertar. \033[m""".format(pc, tentativas))

