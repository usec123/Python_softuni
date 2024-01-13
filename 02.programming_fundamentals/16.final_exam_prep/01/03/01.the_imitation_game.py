encrypted_message = input()

cmd = input()
while cmd!='Decode':
    cmd = cmd.split('|')
    
    if cmd[0]=='Move':
        n = int(cmd[1])
        encrypted_message = encrypted_message[n::]+encrypted_message[:n:]
    
    elif cmd[0]=='Insert':
        index = int(cmd[1])
        value = cmd[2]
        encrypted_message = encrypted_message[:index:] + value + encrypted_message[index::]
    
    elif cmd[0]=='ChangeAll':
        substring = cmd[1]
        replacement = cmd[2]
        encrypted_message = encrypted_message.replace(substring,replacement)
    
    cmd = input()

print(f'The decrypted message is: {encrypted_message}')