from random import randint

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game_data():
    question = randint(2, 100)
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
