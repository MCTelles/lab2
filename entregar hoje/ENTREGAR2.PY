# Imagine que você está implementando um sistema para avaliação de um produto. O
# produto pode através de números inteiros de 0 até 10. Crie uma função que, ao ser
# chamada, solicite ao usuário um número inteiro e verifique através da declaração
# assert se o número está dentro do range permitido. Se não estiver, lance uma exceção
# AssertionError com uma mensagem indicando que o número está fora do intervalo
# permitido.


def function(avaliation):
    assert avaliation > 0, "O número está fora do intervalo permitido"
    assert avaliation < 11, "O número está fora do intervalo permitido"


def main():
    Insatisfeito = 0
    Satisfeito = 0
    MuitoSatisfeito = 0
    try:
        print("QUAL SUA GRAU DE SATISFAÇÃO COM NOSSA LOJA (0,10)")
        avaliation = int(input("Qual a sua avaliação para nosso atendimento:"))
        function(avaliation)
        if avaliation >= 0 and avaliation <= 4:
            Insatisfeito += 1
        if avaliation > 4 and avaliation <= 7:
            Satisfeito += 1
        if avaliation >= 8 and avaliation <= 10:
            MuitoSatisfeito += 1

        print(f"\033[41mInsatifeito:{Insatisfeito}\033[0m")
        print(f"\033[43mSatisfeito:{Satisfeito}\033[0m")
        print(f"\033[42mMuito Satisfeito:{MuitoSatisfeito}\033[0m")
    except ValueError as error:
        print(f"Voçê digitou errado{error}")
        main()


main()
