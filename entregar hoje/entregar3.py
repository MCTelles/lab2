# Escreva uma função calculate_square_root que aceite um número como entrada e
# retorne a raiz quadrada desse número. Se o número for negativo, lance uma exceção
# personalizada chamada NegativeNumberError com uma mensagem indicando que a
# raiz quadrada de números negativos não é real. Para calcular a raiz utilize o operador
# de exponenciação **. Exemplo: raiz = 81 ** (1/2)
class NegativeNumberError(Exception):
    pass
def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError("A raiz quadrada de números negativos não é real.")
    else:
        square_root = number ** (1/2)
        print(square_root)
    
def main():
    try:
        number = int(input("Qual número você quer saber a raiz quadrada:"))
        calculate_square_root(number)
    except ValueError as error:
        print(error)
main()