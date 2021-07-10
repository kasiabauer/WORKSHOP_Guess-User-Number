
print('Think about a number in a range of 1 - 1000.')
print('I will guess it in 10 tries.')

min_guess = 0
max_guess = 1000
guess = int(max_guess / 2 + min_guess)


def guess_func():
    guess = int(max_guess / 2 + min_guess)
    return guess


def give_answer(guess):
    return f'My guess is {guess}'


def ask_response():
    result = input(
        'Have I guessed? \n1. No, computer is too low\n2. No, computer is too high \n3. Yes, computer guessed.'
        ' \nWrite 1, 2 or 3 as your answer: ')
    return result


print(f'My guess {guess}')

user_response = input('Have I guessed? \n1. No, computer is too low\n2. No, computer is too high \n3. Yes, computer guessed.'
                      ' \nWrite 1, 2 or 3 as your answer: ')

RESPONSES = {'1': 'low', '2': 'high', '3': 'guessed'}
print(RESPONSES[user_response])

while True:
    if RESPONSES[user_response] == 'low':
        min_guess = guess - 1
        print(min_guess)
        give_answer(guess)
        break
    elif RESPONSES[user_response] == 'high':
        max_guess = guess - 1
        print(max_guess)
        guess = int(max_guess / 2 + min_guess)
        print(guess)
        give_answer(guess)
        print(ask_response())
        break
    elif RESPONSES[user_response] == 'guessed':
        print('I won - thank you for playing')
        break

