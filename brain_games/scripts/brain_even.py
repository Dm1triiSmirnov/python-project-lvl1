from brain_games.scripts.brain_games import main
from brain_games.cli import welcome_user
from random import randrange


def brain_even():
    main()
    name = welcome_user
    print('Answer "yes" if the number is even, otherwise answer "no".')
    score = 0
    while score < 3:
        num = randrange(1, 101)
        if num % 2 == 0:
            correct = 'yes'
        else:
            correct = 'no'
        print('Question: ', num)
        answer = input('Your answer: ')
        if answer == correct:
            score += 1
            print('Correct!')
        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            break
    if score == 3:
        print(f'Congratulations, {name}')


brain_even()


