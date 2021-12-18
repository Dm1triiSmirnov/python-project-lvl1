from random import randint
import math

TASK = 'Find the greatest common divisor of given numbers.'


def get_game_data():
    x, y = randint(1, 100), randint(1, 100)
    question = f'{x} {y}'
    correct_answer = str(math.gcd(x, y))
    return question, correct_answer
