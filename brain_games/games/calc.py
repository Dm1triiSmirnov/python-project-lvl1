from random import randrange, choice


TASK = 'What is the result of the expression?'


def get_game_data():
    symbol = choice(['+', '-', '*'])
    num1 = str(randrange(1, 101))
    num2 = str(randrange(1, 101))
    question = num1 + ' ' + symbol + ' ' + num2
    correct_answer = str(eval(question))
    return question, correct_answer
