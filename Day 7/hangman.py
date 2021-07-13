import random

random = random.randint(0, 2)
print(random)
word_list = ["aardvark", "baboon", "camel"]

randWord = word_list[random]

letter = input("Guess the letter :")

for i in range(len(randWord)):
    if letter == randWord[i]:
        print("right")
    else:
        print("wrong")


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
