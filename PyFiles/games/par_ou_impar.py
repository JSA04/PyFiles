from random import randint
print('""""""""""""""')
print(" PAR OU IMPAR ")
print('""""""""""""""')

pi = str(input("Par ou Impar?[P , I] "))

plganhador = 0
while True:
    pc = randint(0, 10)
    pl = int(input("Digite um número: "))
    ganhador = (pc + pl) % 2

    print("=" * 20)
    if pi in "Pp":
        if ganhador == 0:
            print(f"Eu escolhi {pc} e você escolheu {pl}. {pc + pl} é PAR.")
            print("Parabens! Você GANHOU!")
            print("Vamos Jogar novamente...")
            plganhador += 1
        else:
            print(f"Eu escolhi {pc} e você escolheu {pl}. {pc + pl} é IMPAR.")
            print("GAME OVER! Você venceu {} rodadas".format(plganhador))
            break
    if pi in "Ii":
        if ganhador == 1:
            print(f"Eu escolhi {pc} e você escolheu {pl}. {pc + pl} é IMPAR.")
            print("Parabens! Você GANHOU!")
            print("Vamos Jogar novamente...")
            plganhador += 1
        else:
            print(f"Eu escolhi {pc} e você escolheu {pl}. {pc + pl} é PAR.")
            print("GAME OVER! Você venceu {} rodadas".format(plganhador))
            print("=" * 20)
            break
    print("=" * 20)