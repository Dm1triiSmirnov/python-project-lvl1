from random import randrange
import prompt


def brain_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    score = 0
    while True:
        if score == 3:
            result = f'Congratulations, {name}'
            break
        else:
            num = randrange(1, 101)
            correct_answer = ('no', 'yes')[num % 2 == 0]
            print('Question: ', num)
            user_answer = input('Your answer: ')
            if user_answer not in ('yes', 'no'):
                result = f"Answer only 'yes' or 'no'. Any other answer will be rejected.\nLet's try again, {name}!"
                break
            elif user_answer == correct_answer:
                score += 1
                print('Correct!')
            else:
                result = f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!"
                break
    print(result)

if __name__ == '__main__':
    brain_even()
