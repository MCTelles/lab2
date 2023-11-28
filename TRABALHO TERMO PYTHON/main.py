import menu
import words
import wordlesolo
import wordleduo
import os
import time
import clearconsole
import wordlequad


def main():
    while True:
        menu.display_menu()
        try:
            choice = int(input("\033[34;3mQual opção você escolhe:\033[0m"))

            if choice == 1:
                clearconsole.clearscreen(1)
                menu.press1()
                menuchoice = int(input("\033[34;3mQual opção você escolhe:\033[0m "))

                if menuchoice == 1:
                    word = words.pullwords()
                    wordlesolo.playsolo(word)

                elif menuchoice == 2:
                    firstword, secondword = words.pulltwoWords()
                    wordleduo.playduo(firstword, secondword)

                elif menuchoice == 3:
                    amount = 4
                    playforgame = words.pullForWords(amount)
                    # print(playforgame)
                    if playforgame:
                        clearconsole.clearscreen(1)
                        wordlequad.quadruple_game(playforgame)
                        clearconsole.clearscreen(1)
            elif choice == 2:
                print("Você resetou todas as palavras.")

                with open("excluedword.txt", "r") as arquivo_origem:
                    conteudo = arquivo_origem.readlines()

                with open("wordsintxt.txt", "a") as arquivo_destino:
                    for linha in conteudo:
                        arquivo_destino.write(linha + "\n")

                with open("excluedword.txt", "w") as arquivo_origem:
                    arquivo_origem.write("")

                print("Processo concluído!")

            else:
                os.system("cls") and os.system("clear")
                print("")
                print("")
                print("")
                print("\033[31mOPÇÃO INVALIDA! TENTE NOVAMENTE.\033[0m")
                clearconsole.clearscreen(1)
        except ValueError:
            clearconsole.clearscreen(1)
            print("\033[31mDIGITE A PALAVRA CORRETA\033[0m")
            clearconsole.clearscreen(1)
            continue


main()
