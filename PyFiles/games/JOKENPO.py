from random import randint
from time import sleep

print("=" * 15)
print("    Jokenpô    ")
print("=" * 15)
print("( 1 ) PEDRA")
print("( 2 ) PAPEL")
print("( 3 ) TESOURA")

pl = int(input("Sua opçao: "))
pc = randint(1, 3)

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1.1)

if pl == 1:
    print("Você escolheu PEDRA.")
elif pl == 2:
    print("Você escolheu PAPEL.")
elif pl == 3:
    print("Você escolheu TESOURA.")

if pc == 1:
    print("Eu escolhi PEDRA.")
elif pc == 2:
    print("Eu escolhi PAPEL.")
elif pc == 3:
    print("Eu escolhi TESOURA.")

if pc == pl:
    print("Deu empate! ")
elif pc == 1 and pl == 2 or pc == 2 and pl == 3 or pc == 3 and pl == 1:
    print("VOCÊ VENCEU! ")
elif pl == 1 and pc == 2 or pl == 2 and pc == 3 or pl == 3 and pc == 1:
    print("EU VENCI!")
