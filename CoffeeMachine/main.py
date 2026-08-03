from menu import MENU, resources

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def refill():
    resources["water"] += 300
    resources["milk"] += 200
    resources["coffee"] += 100
    print("Resources refilled.")


def print_menu():
    for drink in MENU:
        print(f"{drink}: ${MENU[drink]['cost']}")

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = money_received - drink_cost
        if change > 0:
            print(f"Here is ${round(change, 2)} in change.")
        resources["money"] += drink_cost
        return True

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

is_on = True

print_menu()
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        report()
    elif choice == "refill":
        refill()
    else:
        if choice in MENU:
            order = MENU[choice]
            order_ingredients = order["ingredients"]

            if is_resource_sufficient(order_ingredients):
                payment = process_coins()
                if is_transaction_successful(payment, order["cost"]):
                    make_coffee(choice, order_ingredients)
        else:
            print("Sorry, that's not a valid option. Please choose espresso, latte, or cappuccino.")