#Rock Paper Scissors

import random

# Rules

# Rock wins scissors
# Scissors wins paper
# Paper wins rock

# # test_seed = int(input("Create a seed: "))
# # random.seed(test_seed)
# # print(random.randint(1, 20))


rock = 'R'

paper = 'P'

scissors = 'S'

#List of options
game_images = ["R", "S", "P"]

#Get user choice
user_choice = int(input("Choose 0 rock, 1 scissors, 2 paper \n"))
computer = random.randint(0, 2)

try:

  #displays the users choice
  print(f"User choice is: {user_choice}")
  print(game_images[user_choice])

  #displays the computer's choice
  print(f"Computer choice is: {computer}")
  print(game_images[computer])

  #conditions for comparing user and computer choice.
  if user_choice == 0 and computer == 1:
    print("------- You Win!  ------------")
  elif user_choice == 1 and computer == 2:
    print("------- You Win!  ------------")
  elif user_choice == 2 and computer == 0:
    print("------- You Win!  ------------")
  elif user_choice == computer:
    print("------- It's a Draw!  ------------")
  else:
    print("------- You Lose ------------")

#displays error for invalid entries
except IndexError:
  print("------- Invalid option. Try again!  ------------")