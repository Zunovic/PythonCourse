import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

opponent_pick = random.randint(0, 2)
player_pick = int(input("Was wählst du? 0 = Stein, 1 = Papier, 2 = Schere"))
choose_list = [rock, paper, scissors]

print("Du hast gewählt:")
print(choose_list[player_pick])

print("Computer wählt:")
print(choose_list[opponent_pick])

if player_pick > 2:
    print("Error")
elif opponent_pick > player_pick:
    print(f"Der Computer gewinnt")
elif player_pick > opponent_pick:
    print("Du hast gewonnen")
elif player_pick == opponent_pick:
    print("Unentschieden!")
