def find_element(lista, indice):
    try:
        elemento = lista[indice]
        return elemento
    except IndexError:
        raise IndexError("O índice fornecido é inválido para a lista.")

def main():
    my_list = [10, 20, 30, 40, 50]

    try:
        indice = int(input(f"Digite um índice (0-{len(my_list)-1}): "))
        resultado = find_element(my_list, indice)
        print(f"O elemento na posição {indice} é: {resultado}")
    except ValueError:
        print("Índice inválido. Forneça um número inteiro.")
    except IndexError as e:
        print(e)