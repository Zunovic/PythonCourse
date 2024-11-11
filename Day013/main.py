from art import logo
from game_data import data
from art import vs
import random

points = 0

print(logo)


# Accountdaten werden separiert und gespeichert
def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        a_wins = True
        return
    elif b_followers > a_followers:
        a_wins = False
        return
    else:
        print("Fehler!")


# RandomNummer die aus dem Dict einen Account aussucht
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f"A: {format_data(account_a)}.")
print(vs)
print(f"B: {format_data(account_b)}.")

guess = input("Wer hat mehr Follower auf Instagram A oder B?: ").lower()

a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]

check_answer(guess, account_a, account_b)
