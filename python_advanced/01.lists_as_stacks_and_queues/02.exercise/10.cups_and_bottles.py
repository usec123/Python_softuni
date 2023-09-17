from collections import deque

cups_capacity = deque(map(int,input().split()))
bottles_capacity = list(map(int,input().split()))

wasted_water = 0

while cups_capacity and bottles_capacity:
    cup = cups_capacity.popleft()
    bottle = bottles_capacity.pop()
    
    cup -= bottle
    
    if cup > 0:
        cups_capacity.appendleft(cup)
    else:
        wasted_water += abs(cup)

if not cups_capacity:
    print(f'Bottles: {" ".join([str(item) for item in bottles_capacity])}')
    
else:
    print(f'Cups: {" ".join([str(item) for item in cups_capacity])}')

print(f'Wasted litters of water: {wasted_water}')