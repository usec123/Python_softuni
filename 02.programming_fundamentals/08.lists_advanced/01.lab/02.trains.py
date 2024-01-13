trains = [0]*int(input())

cmd = input().split()
while cmd[0]!='End':
    if cmd[0] == 'add':
        trains[-1] += int(cmd[1])
    
    if cmd[0] == 'insert':
        trains[int(cmd[1])] += int(cmd[2])
    
    if cmd[0] == 'leave':
        trains[int(cmd[1])] -= int(cmd[2])
    
    cmd = input().split()
print(trains)