rows,columns = list(map(int,input().split()))

matrix = [list(map(int,input().split()[:columns:])) for _ in range(rows)]

cmd = input()
while cmd!='END':
    invalid = False
    
    cmd = cmd.split()
    
    if cmd[0] == 'swap' and len(cmd) == 5:
        cmd = list(map(int,cmd[1::]))
        for x in range(0,len(cmd),2):
            if cmd[x] > rows or cmd[x+1] > columns or cmd[x] < 0 or cmd[x+1] < 0:
                invalid = True
                break
        if not invalid:
            matrix[cmd[0]][cmd[1]],matrix[cmd[2]][cmd[3]] = \
                matrix[cmd[2]][cmd[3]],matrix[cmd[0]][cmd[1]]
            print('\n'.join([' '.join(list(map(str,row))) for row in matrix]))
    else:
        invalid = True
    
    if invalid:
        print('Invalid input!')
                
    cmd = input()