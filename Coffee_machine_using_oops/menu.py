from data import MENU

class MenuItem:
    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients

class Menu:
    def __init__(self):
        self.menu = []
        for item_name in MENU:
            item_data = MENU[item_name]
            menu_item = MenuItem(
                name=item_name,
                cost=item_data["cost"],
                ingredients=item_data["ingredients"],
            )
            self.menu.append(menu_item)

    def get_items(self):
        names = [item.name for item in self.menu]
        return "/".join(names)

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        return None