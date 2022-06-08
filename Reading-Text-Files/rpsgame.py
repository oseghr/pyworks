#Rock Paper Scissors

import random

# Rules
# Rock wins scissors
# Scissors wins paper
# Paper wins rock

R = 'Rock'
P = 'Paper'
S = 'Scissors'

#List of options
game_options = [R, S, P]

#Get user choice
user_choice = input("Choose R - Rock, S - Scissors, P - Paper \n")
user = user_choice.upper()

while True:
  if user == "R":
    user = R
    break
  elif user == "S":
    user = S
    break
  elif user == "P":
    user = P
    break
  else:
    print("------- Invalid option. Try again!  ------------")
  user_choice = input("Choose R - Rock, S - Scissors, P - Paper \n")
  user = user_choice.upper()

#Get computer choice
computer = random.choice(game_options)

try:
  
  print(f"Player ({user}) : CPU ({computer})")
  #conditions for comparing user and computer choice.
  if user == "Rock" and computer == "Scissors":
    print("------- You Win!  ------------")
  elif user == "Scissors" and computer == "Paper":
    print("------- You Win!  ------------")
  elif user == "Paper" and computer == "Rock":
    print("------- You Win!  ------------")
  elif user == computer:
    print("------- It's a Draw!  ------------")
  else:
    print("------- You Lose ------------")
  
