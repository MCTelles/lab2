def be_back(function, args):
    print("-="*22)
    return_or_not = input("Você deseja voltar (S e N):").upper()
    if return_or_not == "S":
        return
    elif return_or_not == "N":
        function(*args)
    else:
        print("\033[1;32mERRO\033[1;32m")
