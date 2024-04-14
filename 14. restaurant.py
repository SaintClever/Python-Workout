MENU = {
    "burger": 10.50,
    "pizza": 12.75,
    "salad": 8.25,
    "fries": 5.95,
    "sandwich": 9.80,
    "soup": 6.60,
    "pasta": 11.35,
    "steak": 15.45,
    "fish": 13.20,
}


def restaurant(menu):
    _menu_ = "".join(
        f"\n{meal.capitalize()}: ${price:.2f}" for meal, price in menu.items()
    )
    print("\n==== MENU ====", _menu_)

    total = 0

    while True:
        order = input("\nOrder: ").strip()

        if order in menu:
            print(f"{order}: ${float(menu[order]):.2f}")
            total += menu[order]

        if order not in menu and order != "":
            print("\n==== MENU ====", _menu_)

        if order == "":
            print(f"Order total: ${total:.2f}\n")
            break


restaurant(MENU)
