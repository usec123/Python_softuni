n = int(input())

ships = []

for x in range(n):
    ships.append(list(map(int,input().split())))

attacks = input().split()
destroyed = 0

for attack in attacks:
    cmd = list(map(int,attack.split('-')))
    if ships[cmd[0]][cmd[1]] > 0:
        ships[cmd[0]][cmd[1]] -= 1
        if ships[cmd[0]][cmd[1]] == 0:
            destroyed+=1

print(destroyed)