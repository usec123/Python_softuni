import random
options = ['r','p','s','e']
full_names = ['Rock','Paper','Scissors']

while True:
    player_input = input('Choose [r]ock, [p]aper or [s]cissors: ').lower()
    
    if player_input not in options:
        raise SystemExit('Invalid Input. Try again...')
    else:
        if player_input == 'e':
            break
        
        player_input = options.index(player_input)
        computer_input = random.randint(0,2)
        print(f'The computer chose {full_names[computer_input]}')
        
        if computer_input==player_input: print('Draw!')
        else:
            player_input-=1
            if player_input < 0: player_input = 2
            
            if player_input == computer_input: print('Player wins!')
            else: print('Computer wins!')
            
print('Thank you for playing!')