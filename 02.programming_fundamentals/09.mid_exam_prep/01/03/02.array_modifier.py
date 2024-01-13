array = list(map(int,input().split()))

cmd = input()
while cmd!='end':
    cmd = cmd.split()
    if cmd[0] == 'swap':
        index1 = int(cmd[1])
        index2 = int(cmd[2])
        array[index1], array[index2] = array[index2],array[index1]
    
    elif cmd[0] == 'multiply':
        index1 = int(cmd[1])
        index2 = int(cmd[2])
        array[index1] *= array[index2]
        
    else:
        for x in range(len(array)): array[x]-=1
    
    cmd=input()

print(', '.join(str(i) for i in array))