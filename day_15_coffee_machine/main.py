MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_on = True


def _check_water(user_input):
    return MENU[user_input]["ingredients"].get("water") and \
           MENU[user_input]["ingredients"]["water"] <= resources["water"]


def _check_milk(user_input):
    return MENU[user_input]["ingredients"].get("milk") and \
           MENU[user_input]["ingredients"]["milk"] <= resources["milk"]


def _check_coffee(user_input):
    return MENU[user_input]["ingredients"].get("coffee") and \
           MENU[user_input]["ingredients"]["coffee"] <= resources["coffee"]


def check_resources_availability(user_input):
    if not _check_water(user_input):
        return False, "Sorry there is not enough water"
    if not _check_milk(user_input):
        return False, "Sorry there is not enough milk"
    if not _check_coffee(user_input):
        return False, "Sorry there is not enough coffee"
    return True, ""


def convert_coins(quarters, dimes, nickles, pennies):
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def is_enough_for_the_beverage(money, beverage):
    return money >= MENU[beverage]["cost"]


def process_order(user_input):
    if MENU[user_input]["ingredients"].get("water"):
        resources["water"] -= MENU[user_input]["ingredients"]["water"]
    if MENU[user_input]["ingredients"].get("milk"):
        resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
    if MENU[user_input]["ingredients"].get("coffee"):
        resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]


def process_payment(user_input, total):
    if MENU[user_input]["cost"] < total:
        return total - MENU[user_input]["cost"]
    return 0


while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == "off":
        break
    elif user_input in ["espresso", "latte", "cappuccino"]:
        enough_resources, error = check_resources_availability(user_input)
        if not enough_resources:
            print(error)
        quarters = int(input("how many quarters?"))
        dimes = int(input("how many dimes?"))
        nickles = int(input("how many nickles?"))
        pennies = int(input("how many pennies?"))
        total = convert_coins(quarters=quarters, dimes=dimes, nickles=nickles, pennies=pennies)
        if not is_enough_for_the_beverage(total, user_input):
            print("Sorry that's not enough money. Money refunded.")
        else:
            change = process_payment(user_input, total)
            if change > 0:
                print(f"Here is ${change:.2f} dollars in change.")
            process_order(user_input)
            print(f"Here is your {user_input}. Enjoy")
    elif user_input == "report":
        print("Water: ",resources["water"])
        print("Milk: ", resources["milk"])
        print("Coffee: ", resources["coffee"])
        print(f"Money: ${profit:.1f}")
    else:
        print("Invalid command")