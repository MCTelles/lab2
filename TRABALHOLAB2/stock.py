import time
import os
import beback
from datetime import date


def product_add(stock_shop, stock_history):
    add_product = input("Digite o produto a ser adicionado:").capitalize()
    amount_product = int(input("Quanto do produto será adicionado:"))
    price_product = int(input("Qual será o preço do produto:"))
    category_product = input("Digite a categoria do produto:").capitalize()

    if add_product in stock_shop:
        stock_shop[add_product]["Quantidade"] += amount_product
        stock_shop[add_product]["Preço"] = price_product
        stock_shop[add_product]["Categoria"] = category_product
        print("\033[33mProduto já em estoque, novamente registrado\033[0m")

    else:
        new_product = {
            "Quantidade": amount_product,
            "Preço": price_product,
            "Categoria": category_product,
        }

        stock_shop[add_product] = new_product
        print("\033[1;32mProduto adicionado com sucesso!")
    time.sleep(2)

    stock_history.append(
        {
            "Operação": "Adicionar",
            "Produto": add_product,
            "Quantidade": amount_product,
            "Preço": price_product,
            "Categoria": category_product,
            "Data": date.today(),
        }
    )


def print_stock(stock_shop):
    for product, check in stock_shop.items():
        print("---------------------")
        print("Produto:", product if product else "Não informado")
        print(
            "Quantidade:",
            check["Quantidade"] if check["Quantidade"] else "Não informado",
        )
        print(
            "Valor Unitário:",
            "R$",
            check["Preço"] if check["Preço"] else "Não informado",
        )
        print(
            "Categoria:", check["Categoria"] if check["Categoria"] else "Não informado"
        )

    beback.be_back(print_stock, [stock_shop])


def search_products(stock_shop):
    os.system("cls")
    print("-=" * 25)
    search_product = input("Digite o nome do produto:").capitalize()

    if search_product in stock_shop:
        print("\033[1;32mProduto:", search_product, "\033[0m")
        print("Quantidade:", stock_shop[search_product]["Quantidade"])
        print("Valor Unitário:", "R$", stock_shop[search_product]["Preço"])
        print("Categoria:", stock_shop[search_product]["Categoria"])

    else:
        print("\033[31mProduto não encontrado\033[0m")

    beback.be_back(search_products, [stock_shop])


def change_product(stock_shop, stock_history):
    product_change = input("Digite o produto que deseja alterar o preço:").capitalize()
    print("\033[36m-=\033[0m" * 22)
    print("Valor Unitário:", "R$", stock_shop[product_change]["Preço"])
    print("\033[36m-=\033[0m" * 22)

    new_price = int(input("Qual valor será o produto:"))
    stock_shop[product_change]["Preço"] = new_price
    print("\033[1;32mPreço atualizado!\033[0m")

    stock_history.append(
        {
            "Operação": "Troca de preço",
            "Produto": product_change,
            "Preço": new_price,
            "Data": date.today(),
        }
    )


def delete_product(stock_shop, stock_history):
    print("-=" * 22)
    which_delete = input("Qual produto deseja remover:").capitalize()
    if which_delete in stock_shop:
        deleted_product = stock_shop[which_delete]
        del stock_shop[which_delete]
        print("Deletado com sucesso!")
        stock_history.append(
            {
                "Operação": "Remoção do produto",
                "Produto": which_delete,
                "Data": date.today(),
            }
        )
    else:
        print("Esse produto não existe!")
    beback.be_back(delete_product, [stock_shop, stock_history])


def search_by_category(stock_shop):
    category = input("Digite a categoria que deseja visualizar: ").capitalize()

    found = False
    for product, details in stock_shop.items():
        if details["Categoria"] == category:
            found = True
            print("---------------------")
            print("Produto:", product)
            print("Quantidade:", details["Quantidade"])
            print("Valor Unitário:", details["Preço"])
            print("Categoria:", details["Categoria"])
    beback.be_back(search_by_category, [stock_shop])
    if not found:
        print("Nenhum produto encontrado para a categoria informada.")
        beback.be_back(search_by_category, [stock_shop])
