
from gameData import data
from art import logo, vs
import random
import os
clear = lambda: os.system('cls')

def resetScreen():
    clear()
    print(logo)

def displayGameplay(personA, personB, score, isRight):
    if isRight:
        print(f"You are right Yourscore is {score}")
        print(f'Compare A: {personA["name"]}, {personA["description"]}, from {personA["country"]}')
        print(vs)
        print(f'With : {personB["name"]}, {personB["description"]}, from {personB["country"]}')
    else:
        print(f"You are wrong Your final score is {score}")


def getPerson():
    person = random.choice(data)
    data.remove(person)
    return person

def initializeGame():
    if len(data) >= 2:
        personA = getPerson()
        personB = getPerson()
        
        resetScreen()
        print(f'Compare A: {personA["name"]}, {personA["description"]}, from {personA["country"]}')
        print(vs)
        print(f'With : {personB["name"]}, {personB["description"]}, from {personB["country"]}')
        
        return personA, personB
    else:
        return None,None

def play():
    
    personA, personB = initializeGame()
    
    if personA == None or personB == None:
        print("Data curopt")
        return
    
    isRight = True
    score = 0
    while isRight:
        user_choice = input("Who has more followers? choose (A/B) : ").lower()
        
        if personA["follower_count"] > personB["follower_count"]:
            answer = "a"
        elif personA["follower_count"] < personB["follower_count"]:
            answer = "b"
        else:
            answer = user_choice
        
        resetScreen()
        print(f'{personA["name"]} has {personA["follower_count"]} followers')
        print(f'{personB["name"]} has {personB["follower_count"]} followers')
        
        if user_choice == answer:
            score += 1
            personA = personB
            personB = getPerson() 
        else:
            isRight = False
        
        displayGameplay(personA, personB, score, isRight)



while input("Want to play higher or lower ? (y/n) ") == "y":
    play()