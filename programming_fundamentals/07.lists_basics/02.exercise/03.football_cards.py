team_A = list(range(1,12))
team_B = list(range(1,12))

cmd = input().split()
terminated = False

for item in cmd:
    command = item.split('-')
    if command[0] == 'A' and int(command[1]) in team_A:
        team_A.pop(team_A.index(int(command[1])))
    elif command[0] == 'B' and int(command[1]) in team_B:
        team_B.pop(team_B.index(int(command[1])))
    if len(team_A)<7 or len(team_B)<7:
        terminated = True
        break
print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')
if terminated: print('Game was terminated')