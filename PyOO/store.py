from bank_account import Account

Items = [[["Economic Car", 26000],
          ["Comfortable Car", 53000],
          ["Lux Car", 130000],
          ["Sportive Car", 890000]],
         [["Small House", 80000],
          ["Apartament", 180000],
          ["Big House", 350000],
          ["Mansion", 1100000]],
         [["Economic Android", 800],
          ["Good Android", 1400],
          ["Potent Android", 3200],
          ["iPhone", 4000]],
         [['32" FHD Smart TV', 800],
          ['32" 4K Smart TV', 1200],
          ['40" FHD Smart TV', 1500],
          ['40" 4K Smart TV', 2000],
          ['52" 4K Smart TV', 3500]],
         [["Economic Motorcycle", 8000],
          ["Lux Motorcycle", 23000],
          ["Sportive Motorcycle", 50000]],
         [["Comum Smart Watch", 200],
          ["Good Smart Watch", 500],
          ["Potent Smart Watch", 1000],
          ["Apple Watch", 3900]]]

products = ["Cars", "Houses", "Celphones",
            "Tvs", "Motorcycles", "SmartWatches"]


def _print_categories():
    print(f"\033[1;34m{'Item':<22}{'Price'}\033[m")
    for i in range(0, len(Items)):
        for item in Items[i]:
            print(f"\033[31m{item[0]:<22}\033[mR${item[1]}")


def print_items(category="None"):
    category = category.upper() if category.isalpha() else str(category)

    if category in "CARS" or category == "0":
        category = 0

    elif category in "HOUSES" or category == "1":
        category = 1

    elif category in "CELPHONES" or category == "2":
        category = 2

    elif category in "SMARTTVS" or category == "3":
        category = 3

    elif category in "MOTORCYCLES" or category == "4":
        category = 4

    elif category in "SMARTWACHES" or category == "5":
        category = 5

    try:
        index = 0
        print(f"    \033[31m{'Product':<20}{'Price':>10}\033[m")
        for i in Items[category]:
            print(f"\033[31m{index} - \033[m{i[0]:<20}{i[1]:>10}")
            index += 1
    except IndexError:
        _print_categories()


def buy(conta: Account):
    for i in range(0, len(Items)):
        print(f"{i} - {products[i]}")

    category_answer = None

    try:
        category_answer = input("Enter the category number you wish. ")

    except Exception as Error:
        print(f"You didn't enter a number. "
              f"Error Code: {Error}")

    try:
        print_items(category_answer)

        item_answer = input("Enter the product number you wish: ")
        item = Items[int(category_answer)][int(item_answer)]

        if conta.can_withdraw(item[1]):
            conta.withdraw(item[1])
            conta.propertys.append(item[0])
    except Exception as Error:
        print(f"We couldn't find the product you entered."
              f"Error Code: {Error}")
    else:
        print(f"Congratulations, You acquired a(an) {item[0]}.")
        print(f"Your new balance is {conta.balance}.")
