import prompt

GREETINGS = 'Welcome to the Brain Games!'
NAME_REQUEST = 'May I have your name? '
SAY_HELLO = 'Hello, {}!'
WIN_SCORE = 3
WIN_MESSAGE = 'Congratulations, {}!'
QUESTION_MSG = 'Question: {}'
USER_ANSWER = 'Your answer: '
CORRECT = 'Correct!'
WRONG_ANSWER = "'{}' is wrong answer ;(. " "Correct answer was '{}'." \
               "\nLet's try again, {}!"


def start(game):
    print(GREETINGS)
    name = prompt.string(NAME_REQUEST)
    print(SAY_HELLO.format(name))
    print(game.TASK)
    scores = 0

    while scores < WIN_SCORE:
        question, correct_answer = game.get_game_data()
        print(QUESTION_MSG.format(question))
        user_answer = prompt.string(USER_ANSWER)
        if user_answer == correct_answer:
            scores += 1
            print(CORRECT)
        else:
            result = WRONG_ANSWER.format(user_answer, correct_answer, name)
            break
    if scores == WIN_SCORE:
        result = WIN_MESSAGE.format(name)

    print(result)
