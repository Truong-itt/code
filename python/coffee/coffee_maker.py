class CoffeeMaker:
    """dung luong cua may"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    def report(self):
        """in bao cao tia nguyen"""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """ktra tai nguyen du cho loai do un do khong"""
        can_make = True
        for item in drink.ingredients:
            # print(item)
            # print(drink.ingredients[item])
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """in ra lam cafe dong thoi tru vao tai nguyen da su dung"""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

