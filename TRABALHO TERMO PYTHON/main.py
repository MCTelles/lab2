import menu
import words
import wordle
import os
import time
import clearconsole


def main():
    while True:
        menu.display_menu()
        try:
            choice = int(input("\033[34;3mQual opção você escolhe:\033[0m"))

            if choice == 1:
                clearconsole.clearscreen()
                menu.press1()
                menuchoice = int(input("Qual opção você escolhe: "))

                if menuchoice == 1:
                    clearconsole.clearscreen()
                    word = words.pullwords()
                    wordle.playsolo(word)

                elif menuchoice == 2:
                    a = a

            elif choice == 2:
                print("Você resetou todas as palavras.")
                # RESETAR AS PALAVRAS

            else:
                os.system("cls") and os.system("clear")
                print("")
                print("")
                print("")
                print("\033[31mOPÇÃO INVALIDA! TENTE NOVAMENTE.\033[0m")
                time.sleep(1)
                os.system("cls") and os.system("clear")
        except ValueError:
            clearconsole.clearscreen()
            print("\033[31mDIGITE A PALAVRA CORRETA\033[0m")
            clearconsole.clearscreen()
            continue


main()
