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

gameChoices = [rock, paper, scissors]

userChoice = int(input("Enter your choice: 1. Rock, 2. Paper, 3. Scissors\n"))

compChoice = random.randint(1, 3)

if userChoice == compChoice:
    winner = "nobody"
elif userChoice > compChoice:
    if (userChoice - compChoice) == 1:
        winner = "player"
    else:
        winner = "computer"
elif compChoice > userChoice:
    if (compChoice - userChoice) == 1:
        winner = "computer"
    else:
        winner = "player"

if userChoice >= 1 and userChoice <= 3:
    print("\nComputer chose :\n")
    print(gameChoices[compChoice - 1])
    print("\nYou chose :\n")
    print(gameChoices[userChoice - 1])

    if winner == "nobody":
        print("\nIt's a tie!")
    elif winner == "player":
        print("\nYou won!")
    elif winner == "computer":
        print("\nYou lost!")
else:
    print("\nInvalid choice!")
