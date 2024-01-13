items = input().split()

moves = 0

cmd = input()
while cmd!='end':
    moves+=1
    index = list(map(int,cmd.split()))
    if index[0] == index[1] or index[0] not in range(len(items)) or index[1] not in range(len(items)):
        print('Invalid input! Adding additional elements to the board')
        for _ in range(2):items.insert(int(len(items)/2),f'-{moves}a')
    else:
        if items[index[0]] == items[index[1]]:
            print(f'Congrats! You have found matching elements - {items[index[0]]}!')
            if index[1]>index[0]:
                items.pop(index[1])
                items.pop(index[0])
            else:
                items.pop(index[0])
                items.pop(index[1])
            if len(items) == 0:
                print(f'You have won in {moves} turns!')
                break
        else:
            print('Try again!')
    cmd = input()

if cmd == 'end': print(f"Sorry you lose :(\n{' '.join(items)}")