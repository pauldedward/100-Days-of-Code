import random
import os
clear = lambda: os.system('cls')

logo = '''
_________                              ______  ___            _____   __                 ______              
__  ____/___  _____________________    ___   |/  /____  __    ___  | / /___  ________ ______  /______________
_  / __ _  / / /  _ \_  ___/_  ___/    __  /|_/ /__  / / /    __   |/ /_  / / /_  __ `__ \_  __ \  _ \_  ___/
/ /_/ / / /_/ //  __/(__  )_(__  )     _  /  / / _  /_/ /     _  /|  / / /_/ /_  / / / / /  /_/ /  __/  /    
\____/  \__,_/ \___//____/ /____/      /_/  /_/  _\__, /      /_/ |_/  \__,_/ /_/ /_/ /_//_.___/\___//_/     
                                                 /____/                                                      
'''

clear()
print("Hello, welcome to the guessing game.\n")

def guess():
    return random.randint(1,100)

def calculateChances(difficulty):
    if difficulty == 1:
        return 15
    elif difficulty == 2:
        return 12
    elif difficulty == 3:
        return 10
    elif difficulty == 4:
        return 8
    elif difficulty == 5:
        return 6
    else:
        return 0

def initialize():
    difficulty = int(input("Please choose a difficulty level (1-5): "))
    chances = calculateChances(difficulty)
    print("You have", chances, "chances to guess the number.")
    number_in_mind = guess()
    return number_in_mind, chances

def play(number_in_mind, chances):
    guess_count = 0
    while True:
        guess_count += 1
        guess = int(input("Please guess a number between 1 and 100: "))
        if guess == number_in_mind:
            print("You got it! It took you", guess_count, "guesses.")
            break
        elif guess > number_in_mind:
            print("Too high.")
        elif guess < number_in_mind:
            print("Too low.")
        if guess_count == chances:
            print("You ran out of guesses.")
            break
        print("You have", chances - guess_count, "guesses left.")

while input("Want to play guessthe number? (y/n): ") == "y":
    clear()
    print(logo)
    number_in_mind, chances = initialize()
    play(number_in_mind, chances)