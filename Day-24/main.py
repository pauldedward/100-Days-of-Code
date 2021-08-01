#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import os

ROOT_PATH = os.getcwd()

with open(f"{ROOT_PATH}/Day-24/Input/Letters/starting_letter.txt", "r") as file:
    starting_letter = file.read()

with open(f"{ROOT_PATH}/Day-24/Input/Names/invited_names.txt", "r") as file:
    invited_people = file.readlines()

for person in invited_people:
    name = person.strip()
    letter = starting_letter.replace("[name]", name)
    
    with open(f"{ROOT_PATH}/Day-24/Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        file.write(letter)
