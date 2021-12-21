from random import randint, choice

TASK = 'What number is missing in the progression?'
MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_STEP = 1
MAX_STEP = 10
MIN_NUM = 1
MAX_NUM = 100


def get_game_data():
    length = randint(MIN_LENGTH, MAX_LENGTH)
    step = randint(MIN_STEP, MAX_STEP)
    first_num = randint(MIN_NUM, MAX_NUM)
    last_num = first_num + (step * length)
    progression = list(range(first_num, last_num, step))
    correct_answer = str(choice(progression))
    progression = ' '.join(map(str, progression))
    question = progression.replace(correct_answer, '..')
    return question, correct_answer
