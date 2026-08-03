class MoneyMachine:
    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: ${self.profit}")

    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        self.money_received = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
        return self.money_received

    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False