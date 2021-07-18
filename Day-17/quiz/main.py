from question_model import Question
from data import q_bank,question_data
from quiz_brain import QuizBrain
from art import logo
import os
import random

clear = lambda: os.system('cls')


question_bank = []

# for question in question_data:
#     question_bank.append(Question(question["text"], question["answer"]))

for q in q_bank:
    question_bank.append(Question(q["question"], q["correct_answer"]))
    
random.shuffle(question_bank)

quiz_brain = QuizBrain(question_bank)

while True:
    
    clear()
    print(logo)
    if quiz_brain.process_current_question():
        print(f"You got it Right ! : Yourscore is {quiz_brain.score}")
        
        if not quiz_brain.quiz_ended():
            quiz_brain.get_next_question()
        else:
            print(f"\nYou beat the Quiz finalscore: {quiz_brain.score}")
            break
        
        if input("Next question (y/n)?") == 'y':
            continue
        else:
            print(f"You chose to quit the quiz with final score: {quiz_brain.score}")
            break
    else:
        print(f"\nOOPS!!!You got it Wrong ! : Yourscore is {quiz_brain.score}")
        break
