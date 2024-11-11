from art import logo


# Plus
def add(n1, n2):
    return n1 + n2


# Minus
def subtract(n1, n2):
    return n1 - n2


# Multiplizieren
def multiply(n1, n2):
    return n1 * n2


# Teilen
def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    num1 = float(input("Was ist die erste Zahl?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Wie möchtest du rechnen?: ")
        num2 = float(input("Was ist die nächste Zahl?: "))
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Möchtest du mit dem Ergebnis weiter rechnen? 'y' oder 'n' ? : ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
