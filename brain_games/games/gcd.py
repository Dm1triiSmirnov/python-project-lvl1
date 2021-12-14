from random import randint
from math import gcd

task = 'Find the greatest common divisor of given numbers.'


def get_game_data():
    x, y = randint(1, 100), randint(1, 100)
    question = f'{x} {y}'
    correct_answer = gcd(x, y)
    return question, correct_answer
