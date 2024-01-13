from collections import deque

water = int(input())

people = deque()

cmd = input()
while cmd!='Start':
    people.append(cmd)
    cmd = input()

cmd = input()
while cmd!='End':
    if cmd.startswith('refill '):
        water += int(cmd.split()[1])
    
    else:
        needed_water = int(cmd)
        if needed_water <= water:
            print(f'{people.popleft()} got water')
            water -= needed_water
        else:
            print(f'{people.popleft()} must wait')
    
    cmd = input()

print(f'{water} liters left')