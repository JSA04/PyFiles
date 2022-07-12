import random


def play() -> None:

    print("***********************************")
    print("**** Welcome to the guess Game ****")
    print("***********************************")

    # Cria um número aleatório e adiciona na variavel "NUMERO_SECRETO".
    # Define número inicial de pontos

    secret_number: int = random.randint(1, 101)
    score: int = 1000

    print("What's the dificulty level?")
    print("(1) Easy (2) Medium (3) Hard")

    def choose_level() -> int:
        while True:
            try:
                level = int(input("Define the level: "))

            except ValueError:
                print("\033[31mYou entered an invalid number! \033[m")
            else:
                if level == 1:
                    return 20

                elif level == 2:
                    return 10

                elif level == 3:
                    return 5

    total_attempts = choose_level()

    for round in range(1, total_attempts + 1):
        print(f"Attempt {round} of {total_attempts}")
        user_try_str = input("Enter a number between 1 and 100:")

        try:
            user_try = int(user_try_str)

        except ValueError:
            print("You entered a invalid answer!")
            continue

        else:
            print(f"Você entered {user_try_str}.")

        if user_try < 1 or user_try > 100:
            print("You must enter a number between 1 and 100!")
            continue

        got = user_try == secret_number
        bigger = user_try > secret_number
        smaller = user_try < secret_number

        if got:
            print(f"You got it ! And did {score} points of score!")
            break
        else:
            if bigger:
                print(
                    "You missed! Your try was bigger than the secret number."
                )
            elif smaller:
                print(
                    "You missed! Your try was smaller than the secret number."
                      )
            lost_score = abs(secret_number - user_try)
            score = score - lost_score

    print("Game Over")


if __name__ == "__main__":
    play()
