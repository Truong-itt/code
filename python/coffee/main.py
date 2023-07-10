from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


coffee_maker.report()
money_machine.report()
# print(money_machine)
# print(coffee_maker)

menu = Menu()
while True:
    option = menu.get_items()
    choice = input(f"what wwould you like? ({option})")
    if choice == "off":
        break
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else :
        # xac nhan ten nhap vao co dung  hay kkhong
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        # coffee_maker.is_resource_sufficient(drink)