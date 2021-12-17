import prompt

GREETINGS = 'Welcome to the Brain Games!'
NAME_REQUEST = 'May I have your name? '
SAY_HELLO = 'Hello, {}!'

def start(game):
    print(GREETINGS)
    name = prompt.string(NAME_REQUEST)
    print(SAY_HELLO.format(name))
    print(game.TASK)
    score = 0

    while True:
        if score == 3:
            result = f'Congratulations, {name}!'
            break
        else:
            question, correct_answer = game.get_game_data()
            print('Question:', question)
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
