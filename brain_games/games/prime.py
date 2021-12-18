import random

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'

START_OF_RANGE = 2
END_OF_RANGE = 100


def get_game_data():
    question = random.randint(START_OF_RANGE, END_OF_RANGE)
    if question == START_OF_RANGE:
        correct_answer = 'yes'
    else:
        for i in range(START_OF_RANGE, question):
            if question % i == 0:
                correct_answer = 'no'
                break
            else:
                correct_answer = 'yes'

    return question, correct_answer
