cmd = input()
while cmd!='End':
    if cmd!='SoftUni':
        for x in cmd:
            print(f'{x*2}', end='')
        print()
    cmd  = input()