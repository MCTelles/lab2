import menu
import stock
import os
import sales
import historic


def main():
    stock_shop = {}
    sales_topics = []
    stock_history = []

    while True:
        os.system("cls")
        menu.menu()
        option = int(input("Digite sua opção:"))

        if option == 1:
            os.system("cls")
            stock.product_add(stock_shop, stock_history)
        elif option == 2:
            os.system("cls")
            stock.search_products(stock_shop)
        elif option == 3:
            os.system("cls")
            stock.print_stock(stock_shop)
        elif option == 4:
            os.system("cls")
            sales.sell_quantity(stock_shop, sales_topics, stock_history)
        elif option == 5:
            os.system("cls")
            sales.show_everything(sales_topics)
        elif option == 6:
            stock.change_product(stock_shop)
        elif option == 7:
            stock.delete_product(stock_shop, stock_history)
        elif option == 8:
            historic.show_history(stock_shop, stock_history)
        elif option == 9:
            stock.search_by_category(stock_shop)
        elif option == 10:
            os.system("cls")
            break
        else:
            os.system("cls")
            print("\03331m------------ERRO, TENTE NOVAMENTE------------\033[0m")


main()
