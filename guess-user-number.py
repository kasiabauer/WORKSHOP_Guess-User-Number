from random import randint


print('Think about a number in a range of 1 - 1000.')
print('I will guess it in 10 tries.')

min_guess = 0
max_guess = 1000

guess = int(max_guess / 2 + min_guess)
print(f'My guess {guess}')

user_response = input('Have I guessed? \n1. No, computer is too low\n2. No, computer is too high \n3. Yes, computer guessed.'
                      ' \nWrite 1, 2 or 3 as your answer: ')

RESPONSES = {'1': 'low', '2': 'high', '3': 'guessed'}

print(RESPONSES[user_response])

if RESPONSES[user_response] == 'low':
    min_guess = guess - 1
elif RESPONSES[user_response] == 'high':
    max_guess = guess - 1
elif RESPONSES[user_response] == 'guessed':
    print('I won - thank you for playing')

print(max_guess)

guess = int(max_guess / 2 + min_guess)

print(f'My guess is {guess}')

user_response = input('Have I guessed? \n1. No, computer is too low\n2. No, computer is too high \n3. Yes, computer guessed.'
                      ' \nWrite 1, 2 or 3 as your answer: ')


