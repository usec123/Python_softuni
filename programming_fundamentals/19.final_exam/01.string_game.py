text = input()

cmd = input()
while cmd!='Done':
    cmd = cmd.split()
    
    if cmd[0] == 'Change':
        char = cmd[1][0]
        replacement = cmd[2]
        
        text = text.replace(char,replacement)
        print(text)
    
    elif cmd[0] == 'Includes':
        substring = cmd[1]
        
        print(substring in text)
    
    elif cmd[0] == 'End':
        substring = cmd[1]
        
        print(text.endswith(substring))
    
    elif cmd[0] == 'Uppercase':
        text = text.upper()
        print(text)
    
    elif cmd[0] == 'FindIndex':
        char = cmd[1][0]
        print(text.find(char))
    
    elif cmd[0] == 'Cut':
        startIndex = int(cmd[1])
        count = int(cmd[2])
        
        text = text[startIndex:startIndex+count:]
        print(text)
    
    cmd = input()