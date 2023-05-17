cmd = input()
while cmd != 'Welcome!':
    if cmd == 'Voldemort':break
    house = ''
    if len(cmd)<5: house = 'Gryffindor'
    elif len(cmd)==5: house = 'Slytherin'
    elif len(cmd)==6: house = 'Ravenclaw'
    else: house = 'Hufflepuff'
    print(f'{cmd} goes to {house}.')
    cmd = input()
if cmd == 'Welcome!': print('Welcome to Hogwarts.')
else: print('You must not speak of that name!')