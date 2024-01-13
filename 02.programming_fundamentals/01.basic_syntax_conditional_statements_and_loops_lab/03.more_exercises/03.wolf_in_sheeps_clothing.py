cmd = input().split(', ')
if cmd.pop() == 'wolf': print('Please go away and stop eating my sheep')
else: 
    while len(cmd)>0:
        if cmd[0] == 'wolf':
            print(f'Oi! Sheep number {len(cmd)}! You are about to be eaten by a wolf!')
            break
        cmd.pop(0)