from core.executor import get_fibonacci_sequence, get_located

cmd = input()

while cmd!='Stop':
    cmd = cmd.split()
    if cmd[0] == 'Create':
        count = int(cmd[2])
        print(get_fibonacci_sequence(count))
    
    else:
        number = int(cmd[1])
        print(get_located(number))
    
    cmd = input()