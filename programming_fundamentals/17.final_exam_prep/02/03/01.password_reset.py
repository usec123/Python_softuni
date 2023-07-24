password = input()

cmd = input()
while cmd!='Done':
    cmd = cmd.split()
    
    if cmd[0] == 'TakeOdd':
        password = ''.join([password[index] for index in range(1,len(password),2)])
        print(password)
    
    elif cmd[0] == 'Cut':
        index = int(cmd[1])
        length = int(cmd[2])
        substring = password[index:index+length:]
        password = password.replace(substring,'',1)
        print(password)
    
    elif cmd[0] == 'Substitute':
        substring = cmd[1]
        new_string = cmd[2]
        if substring in password:
            password = password.replace(substring,new_string)
            print(password)
        else:
            print('Nothing to replace!')

    cmd = input()
   
print(f'Your password is: {password}')