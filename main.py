from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
order = Menu()
items = order.get_items()
coffee_maker_status = CoffeeMaker()
money_status = MoneyMachine()

while machine_on:

    key = input(f"What would you like ({items}) ?\n").lower()
    if key == "cappuccino":
        item = "cappuccino"
    elif key == "espresso":
        item = "espresso"
    elif key == "latte":
        item = "latte"
    elif key == "report":
        ingr_status = coffee_maker_status.report()
        money_stat = money_status.report()
        print(ingr_status)
        print(money_stat)
        continue
    elif key == "off":
        machine_on = False
        continue

# find selected item
    selection = order.find_drink(item)

    # Check if ingredients are sufficient
    sufficient = coffee_maker_status.is_resource_sufficient(selection)

    if sufficient:
        coffee_maker_status.make_coffee(selection)

    # Requested and check if sufficient coins have been inserted
    payment_status = False

    while not payment_status:
        payment_status = money_status.make_payment(selection.cost)
        if not payment_status:
            prompt = input("Insufficient coins , would you like to reinsert coins [Y] or cancel order [Q] ?").upper()
            if prompt == "Y":
                continue
            if prompt == "Q":
                print("Goodbye")
                quit()
