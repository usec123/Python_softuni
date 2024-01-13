hidden_message = input()

cmd = input()
while cmd!='Reveal':
    cmd = cmd.split(':|:')
    
    if cmd[0] == 'InsertSpace':
        index = int(cmd[1])
        hidden_message = hidden_message[:index:] + ' ' + hidden_message[index::]
        print(hidden_message)
    
    elif cmd[0] == 'Reverse':
        substring = cmd[1]
        if substring in hidden_message:
            hidden_message = hidden_message.replace(substring,'',1)
            hidden_message += substring[::-1]
            print(hidden_message)
        else:
            print('error')
    
    elif cmd[0] == 'ChangeAll':
        substring = cmd[1]
        new_string = cmd[2]
        hidden_message = hidden_message.replace(substring,new_string)
        print(hidden_message)
    
    cmd = input()

print(f'You have a new text message: {hidden_message}')