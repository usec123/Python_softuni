# DOESNT WORK

loot = input().split('|')

cmd = input()

while cmd!='Yohoho!':
    cmd = cmd.split()
    
    if cmd[0] == 'Loot':
        loot = [item for item in cmd[1::] if item not in loot] + loot
    
    elif cmd[0] == 'Drop':
        index = int(cmd[1])
        if index in range(len(loot)):
            loot.append(loot.pop(index))
    
    else:
        print(', '.join(loot[-int(cmd[1])::]))
        loot = loot[:-int(cmd[1]):]
    
    cmd = input()

loot=[len(item) for item in loot]
print(f'Average treasure gain: {sum(loot)/len(loot):.2f} pirate credits.')\
    if len(loot)>0 else\
    print('Failed treasure hunt.')