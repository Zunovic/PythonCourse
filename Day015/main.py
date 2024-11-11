MENU = {
    "espresso": {
        "ingredients":{
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

money_inside = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_enough_rsc(order):
    # Checkt, ob genug vorhanden ist
    is_enough = True
    for item in order:
        if order[item] >= resources[item]:
            print(f"Nicht genug {item}")
            is_enough = False
    return is_enough


def check_coins():
    # Gibt die Endsumme des eingeworfenen Gelds wieder
    print("Bitte Kleingeld einwerfen")
    total = int(input("Wie viele 2€ Münzen?: ")) * 2
    total += int(input("Wie viele 1€ Münzen?: "))
    total += int(input("Wie viele 50 Cent Münzen: ")) * 0.5
    total += int(input("Wie viele 20 Cent Münzen: ")) * 0.2
    total += int(input("Wie viele 10 Cent Münzen: ")) * 0.1
    return total


def transaction(money_given, drink_cost):
    # Gibt True oder False aus, nachdem gecheckt wurde, ob genug Geld eingeworfen ist
    if money_given >= drink_cost:
        change = round(money_given - drink_cost, 2)
        print(f"Dein Rückgeld beträgt: {change} €")
        global money_inside
        money_inside += drink_cost
        return True
    else:
        print("Du hast nicht genug Geld eingeworfen")
        return False


def brew_coffee(drink_wanted, ingredients):
    # Zieht die Zutaten aus dem dict ab
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Dein {drink_wanted} wird zubereitet! ☕")

machine_on = True

while machine_on:
    choice = input("Was möchtest du trinken? (espresso,latte,cappuccino): ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Wasser: {resources['water']} ml")
        print(f"Milch: {resources['milk']} ml")
        print(f"Kaffee: {resources['coffee']} g")
        print(f"Einnahmen: {money_inside} €")
    else:
        drink = MENU[choice]
        if is_enough_rsc(drink["ingredients"]):
            payment = check_coins()
            if transaction(payment, drink["cost"]):
                brew_coffee(choice, drink["ingredients"])
