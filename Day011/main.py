import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def create_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def solve_game(player_card, dealer_card):
    if sum(player_card) > 21:
        return "Der Dealer hat gewonnen!\n"
    elif sum(dealer_card) > 21:
        return "Du hast gewonnen!\n"
    elif sum(player_card) == sum(dealer_card):
        return "Unentschieden!\n"
    elif sum(player_card) > sum(dealer_card):
        return "Du hast gewonnen!\n"
    else:
        return "Der Dealer hat gewonnen!\n"


def check_blackjack(player_card, dealer_card):
    if sum(player_card) == 21 and sum(dealer_card) == 21:
        print("Ihr habt beide einen BlackJack! Das Spiel wird ausgewertet!\n")
        print(f"Die Hand des Dealers: {dealer_card[0],dealer_card[1]} Gesamt: {sum(dealer_card)}\n")
        print(f"Deine Hand : {player_card[0],player_card[1]} Gesamt: {sum(player_card)}\n")
        return solve_game(player_card, dealer_card)

    elif sum(dealer_card) == 21:
        print("Der Dealer hat einen BlackJack! Das Spiel wird ausgewertet!\n")
        print(f"Die Hand des Dealers: {dealer_card[0],dealer_card[1]} Gesamt: {sum(dealer_card)}\n")
        print(f"Deine Hand : {player_card[0],player_card[1]} Gesamt: {sum(player_card)}\n")
        return solve_game(player_card, dealer_card)

    elif sum(player_card) == 21:
        print("Du hast einen BlackJack! Das Spiel wird ausgewertet!\n")
        print(f"Die Hand des Dealers: {dealer_card[0],dealer_card[1]} Gesamt: {sum(dealer_card)}\n")
        print(f"Deine Hand : {player_card[0],player_card[1]} Gesamt: {sum(player_card)}\n")
        return solve_game(player_card, dealer_card)

    else:
        print(f"Der Dealer hat: {dealer_card[0]} + eine verdeckte Karte\n")
        print(f"Du hast {player_card[0],player_card[1]} Gesamt: {sum(player_card)}\n")
        return None


def start_game():
    game_state = True
    while game_state:
        if input("Möchtest du eine Runde BlackJack spielen? 'y' oder 'n': ").lower() == "y":
            print(logo)
            player_card = []
            dealer_card = []

            for _ in range(2):
                dealer_card.append(create_card())
                player_card.append(create_card())

            result = check_blackjack(player_card, dealer_card)
            if result:
                print(result)
                continue

            while input("Möchtest du eine weitere Karte erhalten? 'y' oder 'n': ").lower() == "y":
                player_card.append(create_card())
                print(f"Der Dealer hat : {dealer_card[0]} + eine verdeckte Karte.\n")
                print(f"Du hast {player_card} Gesamt: {sum(player_card)}\n")
                if sum(player_card) > 20:
                    break

            print("Das Spiel wird ausgewertet!\n")
            print(f"Der Dealer hat : {dealer_card} Gesamt: {sum(dealer_card)}")
            while sum(dealer_card) < 17:
                dealer_card.append(create_card())
                print(f"Der Dealer zieht eine Karte und hat nun {dealer_card} Gesamt: {sum(dealer_card)}\n")

            print(solve_game(player_card, dealer_card))

        else:
            print("\nBis zum nächsten Mal!")
            game_state = False


start_game()
