import clearconsole
import menu


def quadruple_game(words):
    trys = 10
    five_attempts = 0
    hits = 0
    hits1 = 0
    hits2 = 0
    hits3 = 0
    hits4 = 0
    menu.menuquad()

    while five_attempts != 9 and hits < 4:
        trys -= 1
        if hits1 == 5 and hits2 == 5 and hits3 == 5 and hits4:
            clearconsole.clearscreen(1)
            print("\033[32mParabéns, você ganhou!!\033[0m")
            print(f"\033[34;3mAs palavras eram: {words}\033[0m")
            clearconsole.clearscreen(2)
            break
        print(f"\033[36;3mVocê tem {trys} tentativas\033[0m")
        try:
            attempt = input(
                "\033[34;3mTente adivinhar as quatro palavras de 5 letras: \033[0m"
            )
            five_attempts += 1
            if len(attempt) != 5:
                raise ValueError("\033[31mSua palavra deverá ser com 5 letras.\033[0m")
            if attempt.isspace():
                print("\033[31mNÃO TENTE QUEBRAR O CÓDIGO\033[0m")
                clearconsole.clearscreen(1)
                continue
        except ValueError as e:
            print(e)
            continue
        if hits1 < 5:
            if attempt.upper() == words[0].upper():
                hits += 1
                hits1 += 5
                print(
                    f"\033[32m{'|'.join(attempt.upper())}\033[0m" + "|",
                    end="\n",
                )
            else:
                for index in range(len(words[0])):
                    if attempt[index].upper() == words[0][index].upper():
                        print(
                            "\033[32m" + attempt[index].upper() + "\033[0m", end=" | "
                        )
                    elif attempt[index].upper() in words[0].upper():
                        print(
                            "\033[33m" + attempt[index].upper() + "\033[0m", end=" | "
                        )
                    else:
                        print(attempt[index].upper(), end=" | ")

            print(end="         ")
        if hits2 < 5:
            if attempt.upper() == words[1].upper():
                hits += 1
                hits2 += 5
                print(
                    f"\033[32m{'|'.join(attempt.upper())}\033[0m" + "|",
                    end="\n",
                )
            else:
                for index in range(len(words[1])):
                    if attempt[index].upper() == words[1][index].upper():
                        print(
                            "\033[32m" + attempt[index].upper() + "\033[0m", end=" | "
                        )
                    elif attempt[index].upper() in words[1].upper():
                        print(
                            "\033[33m" + attempt[index].upper() + "\033[0m", end=" | "
                        )
                    else:
                        print(attempt[index].upper(), end=" | ")

            print(end="         ")

        if hits3 < 5:
            if attempt.upper() == words[2].upper():
                hits += 1
                hits3 += 5
                print(
                    f"\033[32m{'|'.join(attempt.upper())}\033[0m" + "|",
                    end="\n",
                )
            else:
                for index in range(len(words[0])):
                    if attempt[index].upper() == words[2][index].upper():
                        print(
                            "\033[32m" + attempt[index].upper() + "\033[0m", end=" | "
                        )
                    elif attempt[index].upper() in words[2].upper():
                        print(
                            "\033[33m" + attempt[index].upper() + "\033[0m", end=" | "
                        )
                    else:
                        print(attempt[index].upper(), end=" | ")

            print(end="         ")
        if hits4 < 5:
            if attempt.upper() == words[3].upper():
                hits += 1
                hits4 += 5
                print(
                    f"\033[32m{'|'.join(attempt.upper())}\033[0m" + "|",
                    end="\n",
                )
            else:
                for index in range(len(words[0])):
                    if attempt[index].upper() == words[3][index].upper():
                        print(
                            "\033[32m" + attempt[index].upper() + "\033[0m", end=" | "
                        )
                    elif attempt[index].upper() in words[3].upper():
                        print(
                            "\033[33m" + attempt[index].upper() + "\033[0m", end=" | "
                        )
                    else:
                        print(attempt[index].upper(), end=" | ")

            print(end="         ")

        print()
    clearconsole.clearscreen(2)
    print("\033[32mAs palavras eram\033[0m", words)
    clearconsole.clearscreen(2)
