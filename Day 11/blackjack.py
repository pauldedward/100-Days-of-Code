import os
import random
def clear(): return os.system('cls')


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

clear()
print(logo)


def deal_card():
    return random.choice(cards)


user_cards = []
computer_cards = []
is_game_done = False


def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer has blackjack. You lose."
    elif user_score == 0:
        return "You scored blackjack. You win"
    elif user_score > 21:
        return "You lose, you overflowed"
    elif computer_score > 21:
        return "You win, computer overflowed"
    elif user_score > computer_score:
        return "You win"
    elif computer_score > user_score:
        return "You lose"


def show_cards(user_cards, computer_cards):
    print(
        f"Your cards: {user_cards} total score : {calculate_score(user_cards)}")
    print(f"Computer's first card is: {computer_cards[0]}")


def play():
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    is_game_done = False

    while is_game_done == False:
        clear()
        show_cards(user_cards, computer_cards)
        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            is_game_done = True
            continue

        if input("Do you want another card? (y/n) ").lower() == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            if computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
        else:
            is_game_done = True

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    clear()
    print(f"Your score: {user_score} Yourcards: {user_cards}")
    print(
        f"Computer's score: {computer_score} Computer's cards: {computer_cards}")
    print(compare(user_score, computer_score))


while input("Do you want to play a Blackjack Game ? (y/n) ").lower() == "y":
    user_cards = []
    computer_cards = []
    play()
