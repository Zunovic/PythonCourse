print("Willkommen in der Freizeitparkwarteschlange!")
height = int(input("Bitte Größe in cm eingeben: "))
bill = 0

if height >= 120:
    print("Hier ist dein Ticket. Viel Spaß")
    age = int(input("Wie alt bist du?: "))
    if age < 12:
        bill = 5
        print("Kinder Tickets kosten 5€")
    elif age <= 18:
        bill = 7
        print("Jugendtickets kosten 7€")
    elif age in range(45, 55):
        bill = 0
        print("Dein Ticket ist kostenlos. Eltern haben freien Eintritt")
    else:
        bill = 12
        print("Erwachsenentickets kosten 12€")

    print("Fotos kosten 3€ zusätzlich.")
    wants_photo = input("Möchtest du während der Fahrt fotografiert werden? Y oder N: ").lower()
    if wants_photo == "y":
        bill += 3

    print(f"Dein Ticketpreis ist: {bill}€")

else:
    print("Sorry, du musst mindestens 120 cm groß sein.")
