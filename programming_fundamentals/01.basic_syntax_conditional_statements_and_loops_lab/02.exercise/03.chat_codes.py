lines = int(input())
for x in range(lines):
    cmd = int(input())
    if cmd == 88: print('Hello')
    elif cmd == 86: print('How are you?')
    elif cmd < 88: print('GREAT!')
    else: print('Bye.')