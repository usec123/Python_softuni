def check(contest,username):
    for participant in all_participations:
        if participant[0] == contest and participant[1] == username:
            return all_participations.index(participant)
    return True

cmd = input()

contest_participants = dict() # contest : { username : pts }
all_participations = []

while cmd!='no more time':
    cmd = cmd.split(' -> ')
    username = cmd[0]
    contest = cmd[1]
    pts = int(cmd[2])
    
    ch = check(contest,username)
    if type(ch)==bool:
        all_participations.append([contest,username,pts])
    elif pts>all_participations[ch][2]:
        all_participations[ch][2] = pts
    
    if contest in contest_participants.keys():
        if username in contest_participants[contest].keys():
            if pts > contest_participants[contest][username]:
                contest_participants[contest][username] = pts
        else:
            contest_participants[contest][username] = pts
    else:
        contest_participants[contest] = {username:pts}
    cmd = input()
        
for cont,participants in contest_participants.items():
    print(f'{cont}: {len(participants)} participants')
    
    sorted_participants = {key:value for key,value in sorted(participants.items(), key= lambda x: (-x[1],x[0]))}
    
    for x in range(len(list(sorted_participants.keys()))):
        print(f'{x+1}. {list(sorted_participants.keys())[x]} <::> {list(sorted_participants.values())[x]}')

print('Individual standings:')
new_participations = []
while len(all_participations) > 0:
    total_pts = 0
    current_username = all_participations[0][1]
    for x in range(len(all_participations)-1,-1,-1):
        if all_participations[x][1] == current_username:
            total_pts += all_participations[x][2]
            all_participations.pop(x)
    new_participations.append([current_username,total_pts])
    
new_participations = sorted(new_participations,key= lambda x: (-x[1],x[0]))

for x in range(len(new_participations)):
    print(f'{x+1}. {new_participations[x][0]} -> {new_participations[x][1]}')