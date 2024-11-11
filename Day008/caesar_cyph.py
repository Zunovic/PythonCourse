import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cryptic_caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:

        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Du möchtest den Text als {encode_or_decode}d ausgeben. Hier ist dein Ergebnis:\n\n"
          f" {output_text}")


running = True

while running:
    direction = input("Wähle zwischen 'encode' oder 'decode'\n:").lower()
    text = input("Schreibe deine Nachricht\n").lower()
    shift = int(input("Wie viele Stellen soll verschoben werden?\n"))

    cryptic_caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Möchtest du noch mehr ver- oder entschlüsseln? Schreibe 'y' oder 'n'\n").lower()
    if restart == "n":
        running = False
        print("Bis zum nächsten Mal!")
    elif restart == "y":
        running = True

