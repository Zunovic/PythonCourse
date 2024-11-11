import random

logo = '''
  /$$$$$$                                                 /$$     /$$                       /$$   /$$                         /$$                          
 /$$__  $$                                               | $$    | $$                      | $$$ | $$                        | $$                          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$       /$$$$$$  | $$$$$$$   /$$$$$$       | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/      |_  $$_/  | $$__  $$ /$$__  $$      | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$         | $$    | $$  \ $$| $$$$$$$$      | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$        | $$ /$$| $$  | $$| $$_____/      | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/        |  $$$$/| $$  | $$|  $$$$$$$      | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 \______/  \______/  \_______/|_______/|_______/          \___/  |__/  |__/ \_______/      |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      

'''


def choose_level(difficulty):
    difficulty = input('Wähle einen Schwierigkeitsgrad! "easy" oder "hard": ').lower()
    if difficulty == "hard":
        return "hard"
    elif difficulty == "easy":
        return "easy"
    else:
        input("Ungültige eingabe! Probiere es noch ein mal!\n Drücke eine beliebige Taste")
        start_game()


def start_game():
    number_to_guess = random.randint(1, 100)
    # print(f"Debug: Die nummer ist: {number_to_guess}")
    guesses = 0
    print(logo)
    print("Kannst du die Zahl erraten?")
    difficulty = choose_level(input)
    if difficulty == "hard":
        guesses = 5
    elif difficulty == "easy":
        guesses = 10
    while guesses > 0:
        player_guess = int(input(f"Du hast {guesses} versuche die Nummer zu erraten! : "))
        if player_guess == number_to_guess:
            break
        elif player_guess > number_to_guess:
            print("\nZu hoch!\n")
            guesses -= 1
        elif player_guess < number_to_guess:
            print("\nZu niedrig!\n")
            guesses -= 1
    if guesses > 0:
        print(f"\nDu hast die Zahl erraten! Es war die [{number_to_guess}] Super gemacht!\n")
    else:
        print(f"\nDu hast deine Züge aufgebraucht! Es war die Nummer [{number_to_guess}] Versuche es noch einmal!")
    if input("\nMöchtest du noch einmal spielen? 'y' oder 'n' : ").lower() == "y":
        start_game()
    else:
        print("\nBis zum nächsten Mal! :)")


start_game()
