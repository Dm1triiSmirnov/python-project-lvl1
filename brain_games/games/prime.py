import random

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'

START_OF_RANGE = 2
END_OF_RANGE = 100


def get_game_data():
    num = random.randint(START_OF_RANGE, END_OF_RANGE)
    if num == START_OF_RANGE:
        correct_answer = 'yes'
    else:
        prime_num = any([i for i in range(START_OF_RANGE, num) if num % i == 0])
        correct_answer = ('yes', 'no')[prime_num]

    return num, correct_answer
