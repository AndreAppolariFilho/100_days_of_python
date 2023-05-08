from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while coffee_maker.is_on():
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == "off":
        coffee_maker.turn_off()
        break
    elif user_input.lower().strip() in ["espresso", "latte", "cappuccino"]:
        item = menu.find_drink(user_input.lower().strip())
        is_sufficient = coffee_maker.is_resource_sufficient(item)
        if is_sufficient:
            is_payment_successful = money_machine.make_payment(item.cost)
            if is_payment_successful:
                coffee_maker.make_coffee(item)
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        print("Invalid command")