from art import logo, vs
from game_data import data
import random


# Accountdaten werden separiert und gespeichert
def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


# Nimmt die Antwort und prüft, welcher Account mehr Follower hat.
def check_answer(u_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
points = 0
game_running = True
# RandomNummer die aus dem Dict einen Account aussucht
account_b = random.choice(data)

# Loop der das Spiel weiter laufen lässt, wenn nicht falsch geantwortet wurde.
while game_running:
    # Account A wird Account Bs
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"A: {format_data(account_a)}.")
    print(vs)
    print(f"B: {format_data(account_b)}.")

    guess = input("Wer hat mehr Follower? 'A' oder 'B': ").lower()

    # Screen wird geleert.
    print("\n" * 20)
    print(logo)

    # Follower Anzahl wird sich geholt aus dem Dict
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Übergabe an die Funktion zum Prüfen, ob die Antwort richtig ist.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # User bekommt Feedback
    if is_correct:
        points += 1
        print(f"Du hast die richtige Antwort gegeben! Punktestand: {points}")
    else:
        print(f"Du hast die falsche Antwort gegeben! Punktestand:  {points}")
        game_running = False
