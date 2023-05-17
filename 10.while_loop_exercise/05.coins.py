change = float(input())

OPTIONS = [2,1,0.5,0.2,0.1,0.05,0.02,0.01]

coins = 0

while change!=0:
    for x in OPTIONS:
        if change-x>=0:
            coins+=1
            change = float(f'{change-x:.2f}')
            break

print(coins)