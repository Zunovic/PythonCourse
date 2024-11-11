print("Tip Calculator in €")
bill = float(input("Bitte den Betrag eingeben: € "))
tip = int(input("Wie  viel % an Trinkgeld möchtet ihr geben?: "))
people = int(input("Wie viele Personen beteiligen sich an der Rechnung?:  "))


tipping = bill / 100 * tip
each_payment = (bill + tipping) / people

print(f"Wenn ihr {bill} durch {people} aufteilen wollt und {tip} % Trinkgeld geben wollt"
      f"dann bezahlt jeder {each_payment}€")
