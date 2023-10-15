import os
FILE_PATH = os.path.dirname(os.path.abspath(__file__))

cmd = input()
while cmd!='End':
    cmd = cmd.split('-')
    
    if cmd[0] == 'Create':
        with open(os.path.join(FILE_PATH,cmd[1]),'w') as file:
            pass
    
    if cmd[0]=='Add':
        with open(os.path.join(FILE_PATH,cmd[1]),'a') as file:
            file.write(f'{cmd[2]}\n')
        
    if cmd[0]=='Replace':
        try:
            with open(os.path.join(FILE_PATH,cmd[1]),'r') as f:
                lines = f.readlines()
            
            with open(os.path.join(FILE_PATH,cmd[1]),'w') as f:
                for line in lines:
                    f.write(line.replace(cmd[2],cmd[3]))

        except FileNotFoundError:
            print('An error occurred')

    if cmd[0]=='Delete':
        try:
            os.remove(os.path.join(FILE_PATH,cmd[1]))
        except FileNotFoundError:
            print('An error occurred')
    
    cmd = input()