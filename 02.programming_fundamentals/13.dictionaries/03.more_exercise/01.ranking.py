cmd = input()

contest_passwords = {}
user_participations = {} # username : {contest : pts}

while cmd!='end of contests':
    cmd = cmd.split(':')
    contest = cmd[0]
    password = cmd[1]
    contest_passwords[contest] = password
    cmd = input()

cmd = input()

while cmd!='end of submissions':
    cmd = cmd.split('=>')
    contest = cmd[0]
    password = cmd[1]
    username = cmd[2]
    pts = int(cmd[3])
    
    if contest in contest_passwords.keys():
        if password == contest_passwords[contest]:
            if username in user_participations.keys():
                if contest in user_participations[username].keys():
                    if user_participations[username][contest] < pts:
                        user_participations[username][contest] = pts
                else:
                    user_participations[username][contest] = pts
            else:
                user_participations[username] = {contest:pts}
    cmd = input()

total_pts_max = 0
user_max = ''

for user,participations in user_participations.items():
    current_pts = 0
    for points in participations.values():
        current_pts+=points
    if current_pts > total_pts_max:
        total_pts_max = current_pts
        user_max = user

user_participations = dict(sorted(user_participations.items()))

print(f'Best candidate is {user_max} with total {total_pts_max} points.\nRanking:')
for user,participations in user_participations.items():
    print(user)
    sorted_participations = {}
    while len(participations) > 0:
        maximum_value = max(list(participations.values()))
        index = list(participations.values()).index(maximum_value)
        sorted_participations[list(participations.keys())[index]] = list(participations.values())[index]
        participations.pop(list(participations.keys())[index])
    
    for key,value in sorted_participations.items():
        print(f'#  {key} -> {value}')