from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'

START_OF_RANGE = 2
END_OF_RANGE = 100


def get_game_data():
    question = randint(START_OF_RANGE, END_OF_RANGE)
    if question == 2:
        correct_answer = 'yes'
    else:
        for i in range(2, question):
            if question % i == 0:
                correct_answer = 'no'
                break
            else:
                correct_answer = 'yes'
    return question, correct_answer
