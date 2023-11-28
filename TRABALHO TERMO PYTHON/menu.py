def display_menu():
    print("\033[35;4m-=\033[0m" * 45)
    print("\033[34mBEM VINDO AO TERMO.OOO!\033[0m\n")
    print("1 - COMEÇAR JOGO")
    print(" ")
    print("2 - RESETAR PALAVRAS")
    print(" ")
    print("\033[35;4m-=\033[0m" * 45)


def press1():
    print("\033[35;4m-=\033[0m" * 45)
    print("\033[36;1mMODO DE JOGO!\033[0m")
    print("\033[32m1 - SOLO \033[0m")
    print("")
    print("\033[33m2 - DUETO\033[0m")
    print("")
    print("\033[31m3 - QUARTETO\033[0m")
    print("")
    print("\033[35;4m-=\033[0m" * 45)


def menusolo():
    print("\033[35;4m-=\033[0m" * 45)
    print("\033[33;1mMODO SOLO\033[0m")
    print("\033[34mADIVINHE A PALAVRA DE 5 LETRAS\033[0m")
    print("\n")
    print(" _ | _ | _ | _ | _ ")
    print("\033[35;4m-=\033[0m" * 45)


def menuduo():
    print("\033[35;4m-=\033[0m" * 45)
    print("\033[33;1mMODO DUO\033[0m")
    print("\033[34mADIVINHE AS DUAS PALAVRAS DE 5 LETRAS\033[0m")
    print("\n")
    print(
        "Primeira palavra:  _ | _ | _ | _ | _         Segunda palavra:   _ | _ | _ | _ | _"
    )
    print("         ")
    print("\033[35;4m-=\033[0m" * 45)


def menuquad():
    print("\033[35;4m-=\033[0m" * 45)
    print("\033[31mMODO INSANO\033[0m")
    print("\n")
    print("\033[34mADIVINHE AS QUATRO PALAVRAS DE 5 LETRAS\033[0m")
    print("\n")
    print(
        "Primeira palavra: _ | _ | _ | _ | _      Segunda palavra:  _ | _ | _ | _ | _      Terceira palavra: _ | _ | _ | _ | _      Quarta palavra:   _ | _ | _ | _ | _"
    )
    print("\n")
    print("\033[35;4m-=\033[0m" * 45)
