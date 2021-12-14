from random import randrange, choice


task = 'What is the result of the expression?'


def get_game_data():
    symbol = choice(['+', '-', '*'])
    question = str(randrange(1, 101)) + symbol + str(randrange(1, 101))
    correct_answer = str(eval(question))
    return question, correct_answer
