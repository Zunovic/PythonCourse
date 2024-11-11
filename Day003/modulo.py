print("Ist die Zahl gerade oder ungerade?")
number = int(input("Welche Zahl möchtest du überprüfen?: "))

if number % 2 == 0:
    print(f"Die Zahl {number} ist gerade.")
else:
    print(f"Die Zahl {number} ist ungerade.")
