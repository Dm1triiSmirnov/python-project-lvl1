from random import randint
import math

TASK = 'Find the greatest common divisor of given numbers.'
START_OF_RANGE = 1
END_OF_RANGE = 100


def get_game_data():
    x, y = randint(START_OF_RANGE, END_OF_RANGE), randint(START_OF_RANGE, END_OF_RANGE)
    question = f'{x} {y}'
    correct_answer = str(math.gcd(x, y))
    return question, correct_answer
