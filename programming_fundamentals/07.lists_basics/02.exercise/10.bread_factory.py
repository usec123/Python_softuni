energy = 100
MAX_ENERGY = energy
coins = 100
cmd = input().split('|')
completed = True
for i in cmd:
    i=i.split('-')
    event = i[0]
    number = int(i[1])
    if event=='rest':
        old_energy = energy
        energy += number
        if energy>MAX_ENERGY: energy = MAX_ENERGY
        print(f'You gained {energy-old_energy} energy.')
        print(f'Current energy: {energy}.')
    elif event=='order':
        if energy >= 30:
            coins+=number
            energy-=30
            print(f'You earned {number} coins.')
        else:
            energy+=50
            print('You had to rest!')
    else:
        if coins >= number:
            coins-=number
            print(f'You bought {event}.')
        else:
            print(f'Closed! Cannot afford {event}.')
            completed = False
            break
if completed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')