import forca
import guess_game


def escolhe_jogo() -> None:
    print("*****************************")
    print("***** Choose your Game! *****")
    print("*****************************")

    print("(1) Forca (2) Guess game")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        print("Jogando forca")
        forca.play()
    elif jogo == 2:
        print("Jogando adivinhação")
        guess_game.play()


if __name__ == "__main__":
    escolhe_jogo()
