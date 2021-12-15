from random import randint, choice

task = 'What number is missing in the progression?'


def get_game_data():
    length = randint(5, 10)
    step = randint(1, 10)
    first_num = randint(1, 100)
    last_num = first_num + (step * length)
    progression = list(range(first_num, last_num, step))
    correct_answer = str(choice(progression))
    progression = ' '.join(map(str, progression))
    question = progression.replace(correct_answer, '..')
    return question, correct_answer
