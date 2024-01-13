gifts = input().split()

cmd = input()
while cmd!='No Money':
    cmd = cmd.split()
    if cmd[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == cmd[1]:
                gifts[i] = None
    elif cmd[0] == 'Required':
        index = int(cmd[2])
        if 0<=index<len(gifts):
            gifts[index] = cmd[1]
    elif cmd[0] == 'JustInCase':
        gifts[-1] = cmd[1]
    cmd = input()
while None in gifts: gifts.remove(None)
print(' '.join(gifts))