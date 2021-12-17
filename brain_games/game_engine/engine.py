import prompt

GREETINGS = 'Welcome to the Brain Games!'
NAME_REQUEST = 'May I have your name? '
SAY_HELLO = 'Hello, {}!'
MAX_SCORE = 3
STARTING_SCORE = 0
WIN_MESSAGE = 'Congratulations, {}!'
QUESTION = 'Question: {}'
USER_ANSWER = 'Your answer: {}'
CORRECT = 'Correct!'


def start(game):
    print(GREETINGS)
    name = prompt.string(NAME_REQUEST)
    print(SAY_HELLO.format(name))
    print(game.TASK)
    score = STARTING_SCORE

    while True:
        if score == MAX_SCORE:
            result = WIN_MESSAGE.format(name)
            break
        else:
            question, correct_answer = game.get_game_data()
            print(QUESTION.format(question))
            user_answer = input()
            print(USER_ANSWER.format(user_answer))
            if user_answer == correct_answer:
                score += 1
                print(CORRECT)
            else:
                result = f"'{user_answer}' is wrong answer ;(. " \
                         f"Correct answer was '{correct_answer}'." \
                         f"\nLet's try again, {name}!"
                break

    print(result)
