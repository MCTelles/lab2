import clearconsole


def playsolo(word):
    acertos = 0

    clearconsole.clearscreen()

    print("\033[33;1mMODO SOLO\033[0m")
    print("\033[34mADIVINHE A PALAVRA DE 5 LETRAS\033[0m")
    print("")
    print(" _ | _ | _ | _ | _ ")
    chances = 6
    while chances > 0:
        attempt = input("\nTente adivinhar a palavra de 5 letras: ").upper()
        if len(attempt) != 5:
            print("\033[31mTente novamente com 5 letras\033[0m")
            clearconsole.clearscreen()
            continue
        if attempt.isspace():
            print("\033[31mNÃO TENTE QUEBRAR O CODIGO\033[0m")
            clearconsole.clearscreen()
            continue

        checked_indices = set()

        for index in range(min(len(attempt), len(word))):
            if (
                attempt[index].upper() == word[index].upper()
                and index not in checked_indices
            ):
                print("\033[32m" + attempt[index].upper() + "\033[0m", end="|  ")
                acertos += 1
                checked_indices.add(index)

            elif attempt[index].upper() in word.upper():
                print("\033[33m" + attempt[index].upper() + "\033[0m", end=" | ")

            else:
                print(attempt[index].upper(), end=" | ")

        if acertos == 5:
            print("")
            print("PARABÉNS, VOCÊ GANHOU!")
            print("")
            clearconsole.clearscreen()
            break

        chances -= 1
        print("\n")
        print(f"\33[36;3mVocê tem {chances} chances disponíveis\33[0m")

    if chances == 0:
        clearconsole.clearscreen()
        print(
            f"\033[31mSUAS CHANCES ACABARAM, TENTE NOVAMENTE. A PALAVRA ERA: \033[32m{word}\033[0m"
        )
        clearconsole.clearscreen()


def playduo(word):
    clearconsole.clearscreen()
