import beback


def show_history(stock_shop, stock_history):
    for show in stock_history:
        print("-=" * 22)
        print("-=" * 22)
        print("Produto:", show["Produto"] if show["Produto"] else "Não informado")
        print(
            "Quantidade:",
            show["Quantidade"] if show["Quantidade"] else "Não informado",
        )
        print(
            "Valor Unitário:",
            "R$",
            show["Preço"] if show["Preço"] else "Não informado",
        )
        print(
            "Categoria:",
            show["Categoria"] if show["Categoria"] else "Não informado",
        )
        print("Operação:", show.get("Operação", "Não informada"))
        print("Data:", show.get("Data", "Não informada"))
    beback.be_back(show_history, [stock_shop, stock_history])
