friends = input().split(', ')

cmd = input()

while cmd!='Report':
    cmd = cmd.split()
    
    if cmd[0] == 'Blacklist':
        name = cmd[1]
        if name in friends:
            friends[friends.index(name)] = 'Blacklisted'
            print(f'{name} was blacklisted.')
        else:
            print(f'{name} was not found.')

    elif cmd[0] == 'Error':
        index = int(cmd[1])
        if index in range(len(friends)):
            if friends[index] not in ['Blacklisted', 'Lost']:
                print(f'{friends[index]} was lost due to an error.')
                friends[index] = 'Lost'

    elif cmd[0] == 'Change':
        index = int(cmd[1])
        if index in range(len(friends)):
            new_name = cmd[2]
            print(f'{friends[index]} changed his username to {new_name}.')
            friends[index] = new_name
            
    cmd = input()

print(f'Blacklisted names: {len([i for i in friends if i == "Blacklisted"])}')
print(f'Lost names: {len([i for i in friends if i == "Lost"])}')
print(' '.join(friends))