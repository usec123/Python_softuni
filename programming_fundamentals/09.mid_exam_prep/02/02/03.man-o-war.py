status_pirates = list(map(int,input().split('>')))
status_warship = list(map(int,input().split('>')))
max_hp = int(input())

stop = False

cmd = input()
while cmd!='Retire':
    cmd = cmd.split()
    
    if cmd[0] == 'Fire':
        index = int(cmd[1])
        dmg = int(cmd[2])
        if index in range(len(status_warship)):
            status_warship[index]-=dmg
            if status_warship[index] <= 0:
                print('You won! The enemy ship has sunken.')
                stop = True
    
    elif cmd[0]=='Defend':
        start_index = int(cmd[1])
        end_index = int(cmd[2])
        dmg = int(cmd[3])
        if start_index in range(len(status_pirates)) and end_index in range(len(status_pirates)):
            for x in range(start_index, end_index+1):
                status_pirates[x]-=dmg
                if status_pirates[x]<=0:
                    print('You lost! The pirate ship has sunken.')
                    stop = True
                    break
    
    elif cmd[0]=='Repair':
        index = int(cmd[1])
        hp = int(cmd[2])
        if index in range(len(status_pirates)):
            status_pirates[index] += hp
            if status_pirates[index] > max_hp: status_pirates[index] = max_hp
    
    elif cmd[0]=='Status':
        print(f'{len([i for i in status_pirates if i < 0.2*max_hp])} sections need repair.')
    
    if stop:
        break
    
    cmd = input()

if not stop:
    print(f'Pirate ship status: {sum(status_pirates)}')
    print(f'Warship status: {sum(status_warship)}')