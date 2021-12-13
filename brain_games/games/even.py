from random import randrange


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_data():
    num = randrange(1, 101)
    correct_answer = ('no', 'yes')[num % 2 == 0]
    return num, correct_answer
