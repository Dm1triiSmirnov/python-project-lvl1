from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
START_OF_RANGE = 1
END_OF_RANGE = 100


def get_game_data():
    num = randint(START_OF_RANGE, END_OF_RANGE)
    correct_answer = ('no', 'yes')[num % 2 == 0]
    question = num
    return question, correct_answer
