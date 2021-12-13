import prompt

def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.task)
    score = 0

    while True:
        if score == 3:
            result = f'Congratulations, {name}'
            break
        else:
            correct_answer = game.correct_answer
            print('Question: ', game.num)
            user_answer = input('Your answer: ')
            if user_answer == correct_answer:
                score += 1
                print('Correct!')
            else:
                result = f"'{user_answer}' is wrong answer ;(. " \
                         f"Correct answer was '{correct_answer}'." \
                         f"\nLet's try again, {name}!"
                break

    print(result)