import beback
from datetime import date


def sell_quantity(stock_shop, sales_topics, stock_history):
    product_name = input("Digite o nome do produto:").capitalize()
    if product_name in stock_shop:
        print("-=" * 22)
        print("Produto:", product_name)
        print("Quantidade:", stock_shop[product_name]["Quantidade"])
        print("Valor Unitário:", "R$", stock_shop[product_name]["Preço"])
        print("Categoria:", stock_shop[product_name]["Categoria"])
        print("-=" * 22)

        if stock_shop[product_name]["Quantidade"] > 0:
            how_many = int(
                input("Digite a quantidade do produto que deseja vender do estoque:")
            )
            stock_shop[product_name]["Quantidade"] -= how_many
            print(
                "Quantidade atual do produto:", stock_shop[product_name]["Quantidade"]
            )
            sales_topics.append(
                {
                    "Operação": "Relatório de Vendas",
                    "Produto": product_name,
                    "Quantidade": stock_shop[product_name]["Quantidade"],
                    "Preço": stock_shop[product_name]["Preço"],
                    "Categoria": stock_shop[product_name]["Categoria"],
                    "Data": date.today(),
                }
            )

            stock_history.append(
                {
                    "Operação": "Venda do produto",
                    "Produto": product_name,
                    "Quantidade": stock_shop[product_name]["Quantidade"],
                    "Preço": stock_shop[product_name]["Preço"],
                    "Categoria": stock_shop[product_name]["Categoria"],
                }
            )

            beback.be_back(sell_quantity, [stock_shop, sales_topics, stock_history])
        else:
            print("\033[31mSem estoque disponível do produto para venda!\033[0m")
            beback.be_back(sell_quantity, [stock_shop, sales_topics, stock_history])
    else:
        print("\033[31m Não existe o produto informado!\033[0m")
        beback.be_back(sell_quantity, [stock_shop, sales_topics, stock_history])


def show_everything(sales_topics):
    for product in sales_topics:
        print("-=" * 22)
        print("Produto:", product["Produto"] if product["Produto"] else "Não informado")
        print(
            "Quantidade:",
            product["Quantidade"] if product["Quantidade"] else "Não informado",
        )
        print(
            "Valor Unitário:",
            "R$",
            product["Preço"] if product["Preço"] else "Não informado",
        )
        print(
            "Categoria:",
            product["Categoria"] if product["Categoria"] else "Não informado",
        )
        print("Data:", product["Data"])
    beback.be_back(show_everything, [sales_topics])
