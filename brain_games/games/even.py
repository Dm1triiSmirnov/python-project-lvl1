from random import randrange


def get_game_data():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    num = randrange(1, 101)
    correct_answer = ('no', 'yes')[num % 2 == 0]
    return task, num, correct_answer
