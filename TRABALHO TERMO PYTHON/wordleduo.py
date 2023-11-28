import clearconsole
import menu


def playduo(firstword, secondword):
    hits1 = 0
    hits2 = 0
    clearconsole.clearscreen(1)
    chances = 6
    menu.menuduo()
    while chances > 0:
        try:
            attempt = input(
                "\033[34;3mTente adivinhar as duas palavras de 5 letras: \033[0m"
            ).upper()

            if len(attempt) != 5:
                raise ValueError(
                    "\033[31mA palavra deve ter exatamente 5 letras!\033[0m"
                )

            if hits1 == 5 and hits2 == 5:
                clearconsole.clearscreen(1)
                print("\033[32mParabéns, você ganhou!!\033[0m")
                print(f"As palavras eram: {firstword}, {secondword}")
                clearconsole.clearscreen(1)
                break

            if attempt.isspace():
                print("\033[31mNÃO TENTE QUEBRAR O CÓDIGO\033[0m")
                clearconsole.clearscreen(1)
                continue

            elif hits1 < 5 and hits1 > 0:
                hits1 = 0

            elif hits2 < 5 and hits2 > 0:
                hits2 = 0

            print(f"\033[36;3mVocê tem {chances} chances disponíveis\33[0m")
            print("\n")

            checked_indices = set()
            checked_indices2 = set()
            if hits1 < 5:
                for index in range(min(len(attempt), len(firstword))):
                    if (
                        attempt[index].upper() == firstword[index].upper()
                        and index not in checked_indices
                    ):
                        print(
                            "\033[32m" + attempt[index].upper() + "\033[0m", end="|  "
                        )
                        hits1 += 1

                    elif attempt[index].upper() in firstword.upper():
                        print(
                            "\033[33m" + attempt[index].upper() + "\033[0m", end=" | "
                        )

                    else:
                        print(attempt[index].upper(), end=" | ")

                    if hits1 == 5:
                        break

            print(end="         ")

            if hits2 < 5:
                for index in range(min(len(attempt), len(secondword))):
                    if (
                        attempt[index].upper() == secondword[index].upper()
                        and index not in checked_indices2
                    ):
                        print(
                            "\033[32m" + attempt[index].upper() + "\033[0m", end="|  "
                        )
                        hits2 += 1
                    elif attempt[index].upper() in secondword.upper():
                        print(
                            "\033[33m" + attempt[index].upper() + "\033[0m", end=" | "
                        )

                    else:
                        print(attempt[index].upper(), end=" | ")

                    if hits2 == 5:
                        break

            print("\n")

            chances -= 1

            if chances == 0:
                print("\n")
                print(
                    f"\033[31mVocê perdeu! As palavras eram {firstword, secondword} \033[0m"
                )
                clearconsole.clearscreen(2)
            print("\n")
        except ValueError as error:
            print(error)
            continue
