from typing import Text


class Question:
    '''class for a question'''
    def __init__(self, q_text, q_answer) -> None:
        self.text = q_text
        self.answer = q_answer
