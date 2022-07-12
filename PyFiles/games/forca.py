from typing import List


def play() -> None:
    print_startup_message()
    secret_word = select_word()

    right_letters: List[str] = inicialize_right_letters(secret_word)
    print(right_letters)

    errors: int = 0

    enforcou: bool = False
    acertou: bool = False

    while not enforcou and not acertou:
        user_try: str = ask_for_try()

        if len(user_try) != 1 or user_try.isnumeric():
            print("\033[31mYou entered more than one letter or a invalid character.\033[m")
            continue

        if user_try in secret_word:
            right_try(secret_word, user_try, right_letters)
        else:
            errors += 1
            draw_forca(errors)

        enforcou: bool = errors == 7
        acertou: bool = "_" not in right_letters

        print(right_letters)
        print("jogando...")

    if acertou:
        print_winner_message()
    else:
        print_loser_message(secret_word)

    print("The end.")


def print_startup_message() -> None:
    print("**********************************")
    print("*** Welcome to the Forca Game! ***")
    print("**********************************")


def select_word() -> str:
    from random import randint
    with open("words", "r") as archive:
        words = []

        for line in archive:
            line = line.strip()
            words.append(line)

        num = randint(0, len(words))
        secret_word = words[num].upper()
        archive.close()

    return secret_word


def inicialize_right_letters(word) -> List[str]:
    return ["_" for _ in word]


def ask_for_try() -> str:
    return input("What letter? ").upper().strip()


def right_try(word, user_try, letters) -> None:
    index = 0
    for letter in word:
        if user_try == letter:
            letters[index] = letter
        index += 1


def print_winner_message() -> None:
    print("Congratulations! You won!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_loser_message(palavra_secreta) -> None:
    print("GAME OVER!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def draw_forca(errors) -> None:
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    play()
