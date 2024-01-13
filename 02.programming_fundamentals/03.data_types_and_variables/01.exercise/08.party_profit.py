from math import floor
group_size = int(input())
days = int(input())
coins = 0
for x in range(1,days+1):
    if x%10==0:group_size-=2
    if x%15==0:group_size+=5
    coins+=50
    coins-=2*group_size
    if x%3==0: coins-=3*group_size
    if x%5==0: 
        coins+=20*group_size
        if x%3==0: coins-=2*group_size
print(f'{group_size} companions received {floor(coins/group_size)} coins each.')