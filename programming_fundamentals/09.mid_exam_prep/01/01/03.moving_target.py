targets = list(map(int,input().split()))

cmd = input()

while cmd!='End':
    cmd = cmd.split()
    
    if cmd[0]=='Shoot':
        index = int(cmd[1])
        if index in range(len(targets)):
            targets[index] -= int(cmd[2])
            if targets[index] <= 0: targets.pop(index)
        
    elif cmd[0]=='Add':
        index = int(cmd[1])
        if index in range(len(targets)):
            targets.insert(index,int(cmd[2]))
        else: print('Invalid placement!')
    
    else:
        index = int(cmd[1])
        radius = int(cmd[2])
        if index-radius in range(len(targets)) and index+radius in range(len(targets)):
            start_index = index - radius
            for _ in range(radius*2+1):
                targets.pop(start_index)
        else: print('Strike missed!')
    
    cmd = input()

print('|'.join([str(i) for i in targets]))