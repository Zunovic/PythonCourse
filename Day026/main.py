import pandas as pd

alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
df = pd.DataFrame(alphabet)

# Mit der pandas Methode können wir durch das Dataframe iterieren.
# Um ein Dictionary zu erstellen, müssen wir auf die rows zugreifen.

# new_key:new_value for (key, value) in Dataframe loop von pandas
alphabet_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(alphabet_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

active = 1
while active:
    user_input = input("Was möchtest du ins NATO-Alphabet übersetzen?:")
    # translation =  [user_input for word in alphabet_dict.values()]
    print(translation)