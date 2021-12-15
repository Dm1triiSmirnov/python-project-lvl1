from random import randint

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game_data():
    question = randint(1, 100)
    if question == 1:
        correct_answer = 'no'
    else:
        for i in range(1, question):
            if question % i == 0 and i != 1:
                correct_answer = 'no'
                break
            else:
                correct_answer = 'yes'
    return question, correct_answer


print(get_game_data())
