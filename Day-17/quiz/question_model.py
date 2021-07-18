from typing import Text


class Question:
    '''class for a question'''
    def __init__(self, text, answer) -> None:
        self.question = text
        self.answer = answer
