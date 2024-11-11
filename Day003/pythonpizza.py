print("Willkommen bei PythonPizza")
size = input("Welche Größe möchtest du bestellen? S,M oder L: ").lower()
pepperoni = input("Möchtest du Peperoni auf deine Pizza? Y, N: ").lower()
extra_cheese = input("Möchtest du extra Käse?: Y, N ").lower()

if extra_cheese == "y":
    price = 1
else:
    price = 0

if size == "s":
    price += 15
    if pepperoni == "y":
        price += 2
    else:
        price = price
elif size == "m":
    price += 20
    if pepperoni == "y":
        price += 3
elif size == "l":
    price += 25
    if pepperoni == "y":
        price += 3
else:
    print("Du hast eine falsche Angabe gemacht")

print(f"Deine Pizza kostet: {price}€")
