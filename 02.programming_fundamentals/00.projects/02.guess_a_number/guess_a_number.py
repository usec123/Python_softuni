from random import randint

NUMBER = randint(1,100)
guess = None
attempts = 0

while guess != NUMBER:
    try:
        guess = int(input('Guess the number (1-100): '))
    except ValueError: 
        print('You must enter a number!')
        continue
    
    attempts += 1
    
    if guess > NUMBER: print('Too High!')
    elif guess < NUMBER: print('Too Low!')
    else:
        print('You guessed it!')
        print(f'Attempts: {attempts}')
        break