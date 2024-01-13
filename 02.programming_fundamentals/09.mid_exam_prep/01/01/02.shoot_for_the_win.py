targets = list(map(int, input().split()))

cmd = input()

while cmd!='End':
    index = int(cmd)
    if index in range(len(targets)):
        value = targets[index]
        if value==-1:continue
        targets[index]=-1
        for x in range(len(targets)):
            if targets[x]!=-1:
                if targets[x] > value: targets[x]-=value
                else: targets[x]+=value
    cmd = input()
print(f'Shot targets: {len([str(i) for i in targets if i == -1])} -> {" ".join([str(item) for item in targets])}')