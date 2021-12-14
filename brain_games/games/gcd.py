from random import randint

task = 'Find the greatest common divisor of given numbers.'


def get_game_data():
    x, y = randint(1, 100), randint(1, 100)
    question = f'{x} {y}'
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            correct_answer = str(i)
    return question, correct_answer
