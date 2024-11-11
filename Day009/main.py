from art import logo
print(logo)


def highest_bidder(bidding_dict):
    # Das höchste Gebot wird aus dem Dict gesucht und ausgegeben
    highest_bid = 0
    winner = ""
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Die Auktion wurde von {winner} gewonnen! Es wurden {highest_bid}€ geboten!")

bids = {}
auction_running = True

# Loop für die Auktion
while auction_running:
    name = input("Wie ist dein Name?: ")
    pays = int(input("Wie viel möchtest du bieten?: "))
    bids[name] = pays
    continue_auction = input("Sind noch andere bietende anwesend? 'y', 'n': ").lower()
    if continue_auction == "n":
        auction_running = False
        highest_bidder(bids)
    elif continue_auction == "y":
        print("\n" * 20)