import random

word_list = ["zunovic", "skydiving", "backflip", "train", "python", "gaming", "blender"]

chosen_word = random.choice(word_list)
# print(chosen_word) # for debugging
lives = 8
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']
    game_state = True
    while game_state:
        guess = input("Guess a letter: ").lower()
        stage = 0
        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print(display)

        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                game_over = True
                print("Du hast verloren!")

        if "_" not in display:
            game_over = True
            print("Du hast das Wort erraten!")
