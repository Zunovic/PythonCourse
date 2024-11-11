from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Aufgabe: Nicht in die menu.py, money_machine.py und coffee_maker.py schauen
# und nur anhand der gegebenen Dokumentation die vom Projekt von gestern Coffee Machine zu bauen

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_active = True

while machine_active:
    options = menu.get_items()
    choice = input(f"Was möchtest du trinken? ({options}): ")
    if choice == "off":
        machine_active = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)