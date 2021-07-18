
class QuizBrain:
    '''Brain of quiz'''
    def __init__(self, question_list):
        self.score = 0
        self.question_list = question_list
        self.question_list_length = len(question_list) # length of question list
        self.question_list_index = 0 # index of question list
        self.current_question = self.question_list[self.question_list_index]


    def process_current_question(self):
        
        answer = input(f"Q.{self.question_list_index + 1}: {self.current_question.text} (True/False)").lower()
        if answer == self.current_question.answer.lower():
            self.score += (self.question_list_index + 1 * 5) 
            return True
            
        else:
            return False


    def quiz_ended(self):
        
        if self.question_list_index >= self.question_list_length - 1:
            return True
        else:
            return False


    def get_next_question(self):

            self.question_list_index += 1
            self.current_question = self.question_list[self.question_list_index]
