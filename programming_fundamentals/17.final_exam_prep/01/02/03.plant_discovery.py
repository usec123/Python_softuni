n = int(input())

plant_info = {}
ratings = {}

for _ in range(n):
    info = input().split('<->')
    plant_info[info[0]] = info[1]

cmd = input()
while cmd!='Exhibition':
    cmd = cmd.split(': ')
    
    if cmd[0]=="Rate":
        cmd = cmd[1].split(' - ')
        if cmd[0] in ratings:
            ratings[cmd[0]].append(int(cmd[1]))
        else:
            if cmd[0] in plant_info:
                ratings[cmd[0]] = [int(cmd[1])]
            else:
                print('error')
    
    elif cmd[0]=='Update':
        cmd = cmd[1].split(' - ')
        if cmd[0] in plant_info:
            plant_info[cmd[0]] = cmd[1]
        else:
            print('error')
    
    elif cmd[0]=='Reset':
        cmd = cmd[1]
        if cmd in ratings:
            ratings[cmd] = []
        else:
            print('error')
    
    cmd = input()

print('Plants for the exhibition:')
for plant in plant_info.keys():
    print(f'- {plant}; Rarity: {plant_info[plant]}; Rating: {((sum(ratings[plant])/(len(ratings[plant]) if len(ratings[plant])>0 else 1)) if plant in ratings else 0):.2f}')