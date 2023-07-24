key = input()
cmd = input()
while cmd!='Generate':
    cmd = cmd.split('>>>')
    
    if cmd[0] == 'Contains':
        substring = cmd[1]
        if substring in key:
            print(f'{key} contains {substring}')
        else:
            print('Substring not found!')
    
    elif cmd[0] == 'Flip':
        type = cmd[1]
        start_index = int(cmd[2])
        end_index = int(cmd[3])
        key = key[:start_index:]+\
            (key[start_index:end_index:].upper() if type=='Upper' else key[start_index:end_index:].lower())\
                +key[end_index::]
        print(key)
    
    elif cmd[0] == 'Slice':
        start_index = int(cmd[1])
        end_index = int(cmd[2])
        key = key[:start_index:] + key[end_index::]
        print(key)
    
    cmd = input()

print(f'Your activation key is: {key}')