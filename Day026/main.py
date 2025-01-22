import pandas as pd

alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
df = pd.DataFrame(alphabet)

# Mit der pandas Methode können wir durch das Dataframe iterieren.
# Um ein Dictionary zu erstellen, müssen wir auf die rows zugreifen.

# new_key:new_value for (key, value) in Dataframe loop von pandas
alphabet_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(alphabet_dict)

active = 1
while active:
    user_input = input("Was möchtest du ins NATO-Alphabet übersetzen?:").upper()
    if user_input == "EXIT":
        active = 0
    else:
        # Der Input wird Buchstabe für Buchstabe in eine Liste gepackt.
        to_translate = [n for n in user_input]
        # Im alphabet_dict wird nach dem Buchstaben geguckt und die Value aus dem Dict wird in einer Liste gespeichert.
        translation = [alphabet_dict[n] for n in user_input]
        print(translation)
        print('\n Um aufzuhören tippe "exit"\n ')
