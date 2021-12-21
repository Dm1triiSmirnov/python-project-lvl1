from random import randint, choice


TASK = 'What is the result of the expression?'
START_OF_RANGE = 1
END_OF_RANGE = 100


def get_game_data():
    symbol = choice(['+', '-', '*'])
    num1 = randint(START_OF_RANGE, END_OF_RANGE)
    num2 = randint(START_OF_RANGE, END_OF_RANGE)
    question = str(num1) + ' ' + symbol + ' ' + str(num2)
    if symbol == '+':
        correct_answer = str(num1 + num2)
    elif symbol == '-':
        correct_answer = str(num1 - num2)
    elif symbol == '*':
        correct_answer = str(num1 * num2)
    return question, correct_answer
