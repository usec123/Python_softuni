cmd = input()

players = {} # username : { positions : skill }

while cmd!='Season end':
    if ' -> ' in cmd:
        cmd = cmd.split(' -> ')
        player = cmd[0]
        position = cmd[1]
        skill = int(cmd[2])
        
        if player in players.keys():
            if position in players[player].keys():
                if skill > players[player][position]:
                    players[player][position] = skill
            else:
                players[player][position] = skill        
        else:
            players[player] = {position:skill}
    
    elif ' vs ' in cmd:
        cmd = cmd.split(' vs ')
        player1 = cmd[0]
        player2 = cmd[1]
        
        if player1 in players and player2 in players:
            valid = False
            skill1 = 0
            skill2 = 0
            for pos in list(players[player1].keys()):
                if pos in list(players[player2].keys()):
                    valid = True
                    skill1 = players[player1][pos]
                    skill2 = players[player2][pos]
                    break
            if valid:
                if skill1 > skill2:
                    players.pop(player2)
                elif skill2 > skill1:
                    players.pop(player1)

    cmd = input()

total_skill = {username:sum(list(user_skill.values())) for username,user_skill in players.items()} # username : skill

total_skill = dict(sorted(total_skill.items(),key= lambda x: (-x[1],x)))

players = {key:dict(sorted(value.items(), key= lambda x: (-x[1],x))) for key,value in players.items()}

for player in total_skill.keys():
    print(f'{player}: {total_skill[player]} skill')
    for key,value in players[player].items():
        print(f'- {key} <::> {value}')