import clearconsole

import menu


def playsolo(word):
    acertos = 0

    clearconsole.clearscreen(1)
    menu.menusolo()
    chances = 6
    while chances > 0:
        attempt = input(
            "\n\033[34;3mTente adivinhar a palavra de 5 letras:\033[0m "
        ).upper()

        if len(attempt) != 5:
            print("\033[31mTente novamente com 5 letras\033[0m")
            continue

        if attempt.isspace():
            print("\033[31mNÃO TENTE QUEBRAR O CÓDIGO\033[0m")
            clearconsole.clearscreen(1)
            continue

        checked_indices = set()

        for index in range(min(len(attempt), len(word))):
            if (
                attempt[index].upper() == word[index].upper()
                and index not in checked_indices
            ):
                print("\033[32m" + attempt[index].upper() + "\033[0m", end=" | ")
                acertos += 1
                checked_indices.add(index)
            elif attempt[index].upper() in word.upper():
                print("\033[33;3m" + attempt[index].upper() + "\033[0m", end=" | ")
            else:
                print(attempt[index].upper(), end=" | ")
        if acertos > 0 and acertos < 5:
            acertos = 0
        if acertos == 5:
            clearconsole.clearscreen(1)
            print("\n")
            print("\033[32mPARABÉNS, VOCÊ GANHOU!\033[0m")
            print("\n")
            clearconsole.clearscreen(2)
            with open("excluedword.txt", "a") as my_file:
                my_file.write(word)

            with open("wordsintxt.txt", "r") as file:
                lines = file.readlines()

            modified_lines = [line.strip() for line in lines if line.strip() != word]

            with open("wordsintxt.txt", "w") as file:
                for linha in lines:
                    palavras = linha.split(word)
                    palavras_sem_palavra = [p for p in palavras if p != word]
                    nova_linha = " ".join(palavras_sem_palavra)
                    file.writelines(nova_linha)

            break

        chances -= 1
        print("\n")
        print(f"\33[36;3mVocê tem {chances} chances disponíveis\33[0m")

    if chances == 0:
        clearconsole.clearscreen(1)
        print(
            f"\033[31mSUAS CHANCES ACABARAM, TENTE NOVAMENTE. A PALAVRA ERA: \033[32m{word}\033[0m"
        )
        clearconsole.clearscreen(2)
